from __future__ import annotations

import gzip
import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
RAW_DIR = ROOT / "data" / "raw"

EVENT_SCHEMA_VERSION = "1"
OBJECT_SCHEMA_VERSION = "1"


@dataclass(frozen=True)
class PreparedObject:
    dataset: str
    object_key: str
    body: bytes
    content_type: str
    observed_start: str
    observed_end: str
    available_start: str
    available_end: str
    row_count: int
    sha256: str
    event_types: tuple[str, ...]
    data_class: str


@dataclass
class SyncPlan:
    objects: list[PreparedObject]
    ledger_events: list[dict[str, Any]]
    quality: dict[str, Any]


class StorageSyncError(RuntimeError):
    pass


def build_sync_plan(
    profile: str,
    since: datetime,
    now: datetime | None = None,
    repo: str | None = None,
    run_id: str | None = None,
    code_sha: str | None = None,
) -> SyncPlan:
    now = ensure_utc(now or datetime.now(timezone.utc))
    since = ensure_utc(since)
    repo = repo or os.getenv("TD_REPO", "hyperliquid-bot-test")
    run_id = run_id or default_run_id(profile, now)
    code_sha = code_sha or os.getenv("GITHUB_SHA") or "local"
    normalized_profile = profile.strip().lower().replace("-", "_")
    if normalized_profile not in {"context", "flow_alert", "macro"}:
        raise StorageSyncError(f"Unsupported collector profile: {profile}")

    events_by_dataset: dict[str, list[dict[str, Any]]] = {}
    quality: dict[str, Any] = {
        "profile": normalized_profile,
        "window": {
            "since": since.isoformat(),
            "until": now.isoformat(),
        },
        "datasets": {},
        "warnings": [],
    }

    if normalized_profile == "context":
        _collect_context_events(events_by_dataset, quality, since, now)
    elif normalized_profile == "flow_alert":
        _collect_flow_events(events_by_dataset, quality, since, now)
    else:
        _collect_macro_events(events_by_dataset, quality, since, now)

    objects = [
        make_event_object(dataset, events, repo)
        for dataset, events in sorted(events_by_dataset.items())
        if events
    ]
    objects.extend(collect_raw_objects(normalized_profile, since, now))

    manifest_events = [
        make_manifest_event(
            prepared=prepared,
            repo=repo,
            run_id=run_id,
            profile=normalized_profile,
            code_sha=code_sha,
        )
        for prepared in objects
    ]
    quality_event = make_ledger_event(
        event_type="collector.data_quality",
        dataset="data_quality",
        source_id=f"{normalized_profile}:{run_id}",
        event_time=now,
        available_at=now,
        payload={
            **quality,
            "run_id": run_id,
            "repo": repo,
            "collector_code_sha": code_sha,
        },
        tags=["research", normalized_profile, "quality"],
    )
    checkpoint_event = make_ledger_event(
        event_type="collector.checkpoint",
        dataset="collector_checkpoints",
        source_id=normalized_profile,
        event_time=max_observed_at(objects, now),
        available_at=now,
        payload={
            "run_id": run_id,
            "repo": repo,
            "profile": normalized_profile,
            "collector_code_sha": code_sha,
            "object_count": len(objects),
            "row_count": sum(item.row_count for item in objects),
            "datasets": {
                item.dataset: {
                    "object_key": item.object_key,
                    "sha256": item.sha256,
                    "rows": item.row_count,
                    "observed_end": item.observed_end,
                    "available_end": item.available_end,
                }
                for item in objects
            },
        },
        tags=["research", normalized_profile, "checkpoint"],
    )
    run_event = make_ledger_event(
        event_type="collector.run",
        dataset="collector_runs",
        source_id=run_id,
        event_time=since,
        available_at=now,
        payload={
            "run_id": run_id,
            "repo": repo,
            "profile": normalized_profile,
            "status": "storage_ready",
            "collector_code_sha": code_sha,
            "window_start": since.isoformat(),
            "window_end": now.isoformat(),
            "object_count": len(objects),
            "row_count": sum(item.row_count for item in objects),
            "datasets": sorted({item.dataset for item in objects}),
        },
        tags=["research", normalized_profile, "run"],
    )
    return SyncPlan(
        objects=objects,
        ledger_events=[*manifest_events, quality_event, checkpoint_event, run_event],
        quality=quality,
    )


def _collect_context_events(
    target: dict[str, list[dict[str, Any]]],
    quality: dict[str, Any],
    since: datetime,
    now: datetime,
) -> None:
    market_rows = load_list(PROCESSED_DIR / "market_context_history.json")
    quality["datasets"]["market_context_features"] = assess_time_series(
        market_rows,
        time_field="generated_at",
        expected_minutes=15,
        now=now,
    )
    target["market_context_features"] = [
        make_data_event(
            event_type="research.feature.market_context",
            dataset="market_context_features",
            source_id="market_context",
            event_time=row.get("generated_at"),
            available_at=row.get("available_at") or row.get("generated_at"),
            payload=row,
            tags=["feature", "point_in_time"],
        )
        for row in market_rows
        if in_window(row.get("available_at") or row.get("generated_at"), since, now)
    ]

    asset_payload = load_dict(PROCESSED_DIR / "asset_price_history.json")
    asset_rows = dict_rows(asset_payload, "records")
    quality["datasets"]["asset_price_snapshots"] = assess_time_series(
        asset_rows,
        time_field="observed_at",
        expected_minutes=15,
        now=now,
    )
    target["asset_price_snapshots"] = [
        make_data_event(
            event_type="research.observation.asset_prices",
            dataset="asset_price_snapshots",
            source_id="hyperliquid_all_mids",
            event_time=row.get("observed_at"),
            available_at=row.get("collected_at") or row.get("observed_at"),
            payload=row,
            tags=["feature_source", "point_in_time"],
        )
        for row in asset_rows
        if in_window(row.get("collected_at") or row.get("observed_at"), since, now)
    ]

    polymarket_rows = load_list(PROCESSED_DIR / "polymarket_outcome_history.json")
    quality["datasets"]["polymarket_outcomes"] = assess_time_series(
        polymarket_rows,
        time_field="observed_at",
        expected_minutes=15,
        now=now,
        allow_duplicate_times=True,
    )
    target["polymarket_outcomes"] = [
        make_data_event(
            event_type="research.observation.polymarket_outcome",
            dataset="polymarket_outcomes",
            source_id=polymarket_source_id(row),
            event_time=row.get("observed_at"),
            available_at=row.get("collected_at") or row.get("observed_at"),
            payload=row,
            tags=["feature_source", "point_in_time"],
        )
        for row in polymarket_rows
        if in_window(row.get("collected_at") or row.get("observed_at"), since, now)
    ]

    hip4_rows = load_list(PROCESSED_DIR / "hip4_outcome_history.json")
    quality["datasets"]["hip4_outcome_snapshots"] = assess_time_series(
        hip4_rows,
        time_field="observed_at",
        expected_minutes=15,
        now=now,
    )
    target["hip4_outcome_snapshots"] = [
        make_data_event(
            event_type="research.observation.hip4_outcomes",
            dataset="hip4_outcome_snapshots",
            source_id="hyperliquid_hip4",
            event_time=row.get("observed_at"),
            available_at=(
                row.get("available_at")
                or row.get("generated_at")
                or row.get("observed_at")
            ),
            payload=row,
            tags=["feature_source", "point_in_time"],
        )
        for row in hip4_rows
        if in_window(
            row.get("available_at")
            or row.get("generated_at")
            or row.get("observed_at"),
            since,
            now,
        )
    ]

    day_payload = load_dict(PROCESSED_DIR / "day_swing_dataset.json")
    day_rows = dict_rows(day_payload, "records")
    day_quality = assess_time_series(
        day_rows,
        time_field="observed_at",
        expected_minutes=15,
        now=now,
    )
    feature_events, label_events, label_quality = extract_day_swing_events(
        day_rows,
        since,
        now,
    )
    day_quality.update(label_quality)
    quality["datasets"]["day_swing"] = day_quality
    target["day_swing_features"] = feature_events
    target["day_swing_labels"] = label_events

    _collect_asset_feature_events(target, quality, since, now)
    _collect_canary_events(target, quality, since, now)
    _collect_sector_price_events(target, quality, since, now)
    _append_latest_errors(quality)


def _collect_flow_events(
    target: dict[str, list[dict[str, Any]]],
    quality: dict[str, Any],
    since: datetime,
    now: datetime,
) -> None:
    rows = load_list(PROCESSED_DIR / "flow_alert_history.json")
    quality["datasets"]["flow_alert_features"] = assess_time_series(
        rows,
        time_field="generated_at",
        expected_minutes=5,
        now=now,
    )
    target["flow_alert_features"] = [
        make_data_event(
            event_type="research.feature.flow_alert",
            dataset="flow_alert_features",
            source_id="flow_alert",
            event_time=row.get("generated_at"),
            available_at=row.get("available_at") or row.get("generated_at"),
            payload=row,
            tags=["feature", "point_in_time"],
        )
        for row in rows
        if in_window(row.get("available_at") or row.get("generated_at"), since, now)
    ]
    latest = load_dict(PROCESSED_DIR / "flow_alert.json")
    if latest.get("errors"):
        quality["warnings"].extend(f"flow_alert: {item}" for item in latest["errors"])


def _collect_macro_events(
    target: dict[str, list[dict[str, Any]]],
    quality: dict[str, Any],
    since: datetime,
    now: datetime,
) -> None:
    rows = load_list(PROCESSED_DIR / "macro_indicators_history.json")
    quality["datasets"]["macro_indicator_snapshots"] = assess_time_series(
        rows,
        time_field="generated_at",
        expected_minutes=None,
        now=now,
    )
    events: list[dict[str, Any]] = []
    for snapshot in rows:
        generated_at = snapshot.get("generated_at")
        available_at = snapshot.get("available_at") or generated_at
        if not in_window(available_at, since, now):
            continue
        values = snapshot.get("values")
        if not isinstance(values, dict):
            continue
        for indicator_key, value in sorted(values.items()):
            if not isinstance(value, dict):
                continue
            payload = {
                "indicator_key": indicator_key,
                "generated_at": generated_at,
                **value,
            }
            events.append(
                    make_data_event(
                        event_type="research.observation.macro_indicator",
                        dataset="macro_indicator_snapshots",
                        source_id=stable_source_id("macro", str(indicator_key)),
                    event_time=value.get("observed_at") or generated_at,
                    available_at=available_at,
                    payload=payload,
                    tags=["feature_source", "point_in_time"],
                )
            )
    target["macro_indicator_snapshots"] = events

    latest = load_dict(PROCESSED_DIR / "macro_indicators_latest.json")
    provider_warnings = []
    for provider in latest.get("providers", []) if isinstance(latest.get("providers"), list) else []:
        if isinstance(provider, dict) and provider.get("reason"):
            provider_warnings.append(f"{provider.get('name')}: {provider.get('reason')}")
    quality["warnings"].extend(provider_warnings)


def extract_day_swing_events(
    records: list[dict[str, Any]],
    since: datetime,
    now: datetime,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    by_observed = {
        str(row.get("observed_at")): row
        for row in records
        if isinstance(row, dict) and row.get("observed_at")
    }
    feature_events: list[dict[str, Any]] = []
    label_events: list[dict[str, Any]] = []
    labels_before_features = 0
    missing_label_availability = 0
    malformed_labels = 0

    for record in records:
        if not isinstance(record, dict):
            continue
        observed_at = record.get("observed_at")
        collected_at = record.get("collected_at") or observed_at
        if in_window(collected_at, since, now):
            feature_payload = {
                key: value
                for key, value in record.items()
                if key != "symbols"
            }
            symbols = record.get("symbols")
            feature_payload["symbols"] = {}
            if isinstance(symbols, dict):
                for symbol, row in symbols.items():
                    if not isinstance(row, dict):
                        continue
                    feature_payload["symbols"][symbol] = {
                        key: value
                        for key, value in row.items()
                        if key != "labels"
                    }
            feature_events.append(
                make_data_event(
                    event_type="research.feature.day_swing",
                    dataset="day_swing_features",
                    source_id="day_swing",
                    event_time=observed_at,
                    available_at=collected_at,
                    payload=feature_payload,
                    tags=["feature", "point_in_time", "labels_excluded"],
                )
            )

        symbols = record.get("symbols")
        if not isinstance(symbols, dict):
            continue
        for symbol, symbol_row in symbols.items():
            if not isinstance(symbol_row, dict):
                continue
            labels = symbol_row.get("labels")
            if not isinstance(labels, dict):
                continue
            for horizon, label in labels.items():
                if not isinstance(label, dict):
                    malformed_labels += 1
                    continue
                target_observed_at = label.get("labeled_at")
                future_record = by_observed.get(str(target_observed_at), {})
                label_available_at = (
                    future_record.get("collected_at")
                    if isinstance(future_record, dict)
                    else None
                ) or label.get("available_at") or target_observed_at
                if not label_available_at:
                    missing_label_availability += 1
                    continue
                feature_time = parse_time(collected_at)
                available_time = parse_time(label_available_at)
                if feature_time and available_time and available_time < feature_time:
                    labels_before_features += 1
                if not in_window(label_available_at, since, now):
                    continue
                payload = {
                    "feature_observed_at": observed_at,
                    "feature_available_at": collected_at,
                    "symbol": symbol,
                    "horizon": horizon,
                    "target_observed_at": target_observed_at,
                    "label_available_at": normalize_timestamp(label_available_at),
                    "label_version": "forward_return_v1",
                    "return_pct": label.get("return_pct"),
                    "price": label.get("price"),
                    "delay_minutes": label.get("delay_minutes"),
                }
                label_events.append(
                    make_data_event(
                        event_type="research.label.day_swing_forward_return",
                        dataset="day_swing_labels",
                        source_id=stable_source_id(
                            "day_swing_label",
                            f"{observed_at}|{symbol}|{horizon}",
                        ),
                        event_time=observed_at,
                        available_at=label_available_at,
                        payload=payload,
                        tags=["label", "future_outcome", "decision_path_forbidden"],
                    )
                )
    quality = {
        "feature_rows_exported": len(feature_events),
        "label_rows_exported": len(label_events),
        "labels_before_feature_count": labels_before_features,
        "missing_label_availability_count": missing_label_availability,
        "malformed_label_count": malformed_labels,
        "feature_label_separated": True,
    }
    return feature_events, label_events, quality


def _collect_asset_feature_events(
    target: dict[str, list[dict[str, Any]]],
    quality: dict[str, Any],
    since: datetime,
    now: datetime,
) -> None:
    latest = load_dict(PROCESSED_DIR / "asset_features_latest.json")
    generated_at = latest.get("generated_at")
    available_at = latest.get("available_at") or generated_at
    observed_at = latest.get("observed_at") or generated_at
    if not in_window(available_at or observed_at, since, now):
        target["asset_feature_snapshots"] = []
        return

    use_daily_full = is_daily_snapshot(observed_at)
    source = (
        load_dict(PROCESSED_DIR / "asset_features_all.json")
        if use_daily_full
        else latest
    )
    rows = source.get("assets" if use_daily_full else "top_assets")
    if not isinstance(rows, list):
        rows = []
    events = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("symbol"):
            continue
        events.append(
            make_data_event(
                event_type="research.feature.asset",
                dataset="asset_feature_snapshots",
                source_id=stable_source_id(
                    "hyperliquid_asset",
                    str(row["symbol"]),
                ),
                event_time=observed_at,
                available_at=available_at or observed_at,
                payload={
                    "observed_at": observed_at,
                    "generated_at": generated_at,
                    "available_at": available_at,
                    "snapshot_scope": "all_daily" if use_daily_full else "top_activity",
                    **row,
                },
                tags=["feature", "point_in_time", "daily_full" if use_daily_full else "top_activity"],
            )
        )
    target["asset_feature_snapshots"] = events
    quality["datasets"]["asset_feature_snapshots"] = {
        "source_scope": "all_daily" if use_daily_full else "top_activity",
        "source_row_count": len(rows),
        "exported_row_count": len(events),
        "observed_at": normalize_timestamp(observed_at) if observed_at else None,
        "available_at": normalize_timestamp(available_at or observed_at)
        if available_at or observed_at
        else None,
    }


def _collect_canary_events(
    target: dict[str, list[dict[str, Any]]],
    quality: dict[str, Any],
    since: datetime,
    now: datetime,
) -> None:
    payload = load_dict(PROCESSED_DIR / "canary_signals.json")
    available_at = payload.get("available_at") or payload.get("updated_at")
    if not payload or not in_window(available_at, since, now):
        target["canary_signal_snapshots"] = []
        return
    target["canary_signal_snapshots"] = [
        make_data_event(
            event_type="research.signal.canary_snapshot",
            dataset="canary_signal_snapshots",
            source_id="canary_signals",
            event_time=available_at,
            available_at=available_at,
            payload=payload,
            tags=["derived", "candidate_signal", "not_live_policy"],
        )
    ]
    quality["datasets"]["canary_signal_snapshots"] = {
        "signal_count": len(payload.get("signals", []))
        if isinstance(payload.get("signals"), list)
        else 0,
        "correlation_status": payload.get("correlation_status"),
        "sample_status": payload.get("sample_status"),
    }


def _collect_sector_price_events(
    target: dict[str, list[dict[str, Any]]],
    quality: dict[str, Any],
    since: datetime,
    now: datetime,
) -> None:
    payload = load_dict(PROCESSED_DIR / "sector_price_history.json")
    source_available_at = (
        payload.get("source_refreshed_at")
        or payload.get("updated_at")
    )
    if not in_window(source_available_at, since, now):
        target["sector_price_observations"] = []
        return
    rows = dict_rows(payload, "records")
    recent_date = (now - timedelta(days=4)).date()
    events = []
    for row in rows:
        try:
            row_date = datetime.fromisoformat(str(row.get("date"))).date()
        except (TypeError, ValueError):
            continue
        if row_date < recent_date:
            continue
        events.append(
            make_data_event(
                event_type="research.observation.sector_prices",
                dataset="sector_price_observations",
                source_id=stable_source_id(
                    "sector_prices",
                    f"{payload.get('source') or 'sector_proxy'}|{row.get('date')}",
                ),
                event_time=f"{row.get('date')}T00:00:00+00:00",
                available_at=source_available_at,
                payload={
                    "date": row.get("date"),
                    "prices": row.get("prices", {}),
                    "source": payload.get("source"),
                    "source_refreshed_at": source_available_at,
                },
                tags=["feature_source", "daily_close", "availability_guarded"],
            )
        )
    target["sector_price_observations"] = events
    quality["datasets"]["sector_price_observations"] = {
        "source_record_count": len(rows),
        "exported_recent_rows": len(events),
        "source_refreshed_at": normalize_timestamp(source_available_at)
        if source_available_at
        else None,
    }


def _append_latest_errors(quality: dict[str, Any]) -> None:
    context = load_dict(PROCESSED_DIR / "market_context.json")
    for item in context.get("errors", []) if isinstance(context.get("errors"), list) else []:
        quality["warnings"].append(f"market_context: {item}")
    hip4 = load_dict(PROCESSED_DIR / "hip4_outcome_latest.json")
    for item in hip4.get("request_errors", []) if isinstance(hip4.get("request_errors"), list) else []:
        quality["warnings"].append(f"hip4: {item}")
    for item in hip4.get("request_warnings", []) if isinstance(hip4.get("request_warnings"), list) else []:
        quality["warnings"].append(f"hip4 warning: {item}")


def collect_raw_objects(
    profile: str,
    since: datetime,
    now: datetime,
) -> list[PreparedObject]:
    if not RAW_DIR.exists():
        return []
    prefixes_by_profile = {
        "context": (
            "rss_",
            "gdelt_",
            "polymarket_",
            "hip4_",
        ),
        "flow_alert": (
            "polymarket_alert_",
            "dune_large_flows_",
        ),
        "macro": (
            "macro_",
            "fred_",
            "yahoo_",
        ),
    }
    prefixes = prefixes_by_profile[profile]
    objects: list[PreparedObject] = []
    since_epoch = since.timestamp()
    until_epoch = now.timestamp() + 60
    for path in sorted(RAW_DIR.rglob("*.json")):
        if not path.name.startswith(prefixes):
            continue
        try:
            mtime = path.stat().st_mtime
        except OSError:
            continue
        if not (since_epoch <= mtime <= until_epoch):
            continue
        raw = path.read_bytes()
        logical_digest = hashlib.sha256(raw).hexdigest()
        body = deterministic_gzip(raw)
        digest = hashlib.sha256(body).hexdigest()
        observed = datetime.fromtimestamp(mtime, tz=timezone.utc)
        dataset = f"raw_{raw_family(path.name)}"
        date_path = observed.strftime("year=%Y/month=%m/day=%d")
        object_key = f"{date_path}/{path.stem}-{logical_digest[:16]}.json.gz"
        objects.append(
            PreparedObject(
                dataset=dataset,
                object_key=object_key,
                body=body,
                content_type="application/gzip",
                observed_start=observed.isoformat(),
                observed_end=observed.isoformat(),
                available_start=observed.isoformat(),
                available_end=observed.isoformat(),
                row_count=1,
                sha256=digest,
                event_types=("collector.raw_response",),
                data_class="raw",
            )
        )
    return objects


def make_event_object(
    dataset: str,
    events: list[dict[str, Any]],
    repo: str,
) -> PreparedObject:
    ordered = sorted(
        events,
        key=lambda event: (
            str(event.get("available_at")),
            str(event.get("event_time")),
            str(event.get("event_id")),
        ),
    )
    lines = [
        canonical_json(
            {
                "schema_version": EVENT_SCHEMA_VERSION,
                "repo": repo,
                **event,
            }
        )
        for event in ordered
    ]
    uncompressed = ("\n".join(lines) + "\n").encode("utf-8")
    logical_digest = hashlib.sha256(uncompressed).hexdigest()
    observed = [normalize_timestamp(event["event_time"]) for event in ordered]
    available = [normalize_timestamp(event["available_at"]) for event in ordered]
    start = min(observed)
    end = max(observed)
    # Labels can become available days after their feature timestamp. Partitioning
    # by availability keeps late-arriving outcomes in the current ingest window
    # while observed_start/end retain the original research time.
    date_path = parse_time(min(available)).strftime("year=%Y/month=%m/day=%d")
    key_start = compact_time(start)
    key_end = compact_time(end)
    object_key = f"{date_path}/{key_start}_{key_end}_{logical_digest[:16]}.jsonl.gz"
    data_classes = {
        tag
        for event in ordered
        for tag in event.get("tags", [])
        if tag in {"feature", "label", "feature_source", "derived"}
    }
    body = deterministic_gzip(uncompressed)
    return PreparedObject(
        dataset=dataset,
        object_key=object_key,
        body=body,
        content_type="application/gzip",
        observed_start=start,
        observed_end=end,
        available_start=min(available),
        available_end=max(available),
        row_count=len(ordered),
        sha256=hashlib.sha256(body).hexdigest(),
        event_types=tuple(sorted({str(event["event_type"]) for event in ordered})),
        data_class="+".join(sorted(data_classes)) or "research",
    )


def make_manifest_event(
    prepared: PreparedObject,
    repo: str,
    run_id: str,
    profile: str,
    code_sha: str,
) -> dict[str, Any]:
    return make_ledger_event(
        event_type="dataset.manifest",
        dataset="dataset_manifests",
        source_id=f"object:{prepared.dataset}:{prepared.sha256[:32]}",
        event_time=prepared.observed_end,
        available_at=prepared.available_end,
        payload={
            "run_id": run_id,
            "repo": repo,
            "profile": profile,
            "collector_code_sha": code_sha,
            "object_dataset": prepared.dataset,
            "object_key": prepared.object_key,
            "format": "jsonl" if prepared.object_key.endswith(".jsonl.gz") else "json",
            "compression": "gzip",
            "schema_version": OBJECT_SCHEMA_VERSION,
            "content_sha256": prepared.sha256,
            "row_count": prepared.row_count,
            "observed_start": prepared.observed_start,
            "observed_end": prepared.observed_end,
            "available_start": prepared.available_start,
            "available_end": prepared.available_end,
            "event_types": list(prepared.event_types),
            "data_class": prepared.data_class,
            "append_only": True,
        },
        tags=["research", profile, "manifest", prepared.data_class],
    )


def make_data_event(
    event_type: str,
    dataset: str,
    source_id: str,
    event_time: Any,
    available_at: Any,
    payload: dict[str, Any],
    tags: list[str],
) -> dict[str, Any]:
    event_time_normalized = normalize_timestamp(event_time)
    available_at_normalized = normalize_timestamp(available_at)
    event_time_value = parse_time(event_time_normalized)
    available_at_value = parse_time(available_at_normalized)
    if available_at_value < event_time_value:
        raise StorageSyncError(
            f"available_at precedes event_time for {dataset}/{source_id}"
        )
    if not re.fullmatch(r"[a-z][a-z0-9_.-]{2,127}", event_type):
        raise StorageSyncError(f"Invalid event_type: {event_type}")
    if not re.fullmatch(r"[a-z0-9][a-z0-9._-]{0,63}", dataset):
        raise StorageSyncError(f"Invalid dataset: {dataset}")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:/-]{0,127}", source_id):
        raise StorageSyncError(f"Invalid source_id: {source_id}")
    if any(
        not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,63}", tag)
        for tag in tags
    ):
        raise StorageSyncError(f"Invalid tag in {tags!r}")
    identity = canonical_json(
        {
            "event_type": event_type,
            "dataset": dataset,
            "source_id": source_id,
            "event_time": event_time_normalized,
            "available_at": available_at_normalized,
            "payload": payload,
        }
    )
    return {
        "event_id": f"hlbt_{hashlib.sha256(identity.encode('utf-8')).hexdigest()}",
        "event_type": event_type,
        "dataset": dataset,
        "source_id": source_id,
        "event_time": event_time_normalized,
        "available_at": available_at_normalized,
        "payload": payload,
        "tags": sorted(set(tags)),
    }


def make_ledger_event(
    event_type: str,
    dataset: str,
    source_id: str,
    event_time: Any,
    available_at: Any,
    payload: dict[str, Any],
    tags: list[str],
) -> dict[str, Any]:
    return make_data_event(
        event_type=event_type,
        dataset=dataset,
        source_id=source_id,
        event_time=event_time,
        available_at=available_at,
        payload=payload,
        tags=tags,
    )


def assess_time_series(
    rows: list[dict[str, Any]],
    time_field: str,
    expected_minutes: int | None,
    now: datetime,
    allow_duplicate_times: bool = False,
) -> dict[str, Any]:
    parsed: list[datetime] = []
    invalid_timestamp_count = 0
    original_order: list[datetime] = []
    for row in rows:
        timestamp = parse_time(row.get(time_field)) if isinstance(row, dict) else None
        if timestamp is None:
            invalid_timestamp_count += 1
            continue
        parsed.append(timestamp)
        original_order.append(timestamp)
    ordered = sorted(parsed)
    duplicate_count = len(ordered) - len(set(ordered))
    gaps = [
        (right - left).total_seconds() / 60
        for left, right in zip(ordered, ordered[1:])
        if right > left
    ]
    max_gap = max(gaps) if gaps else None
    latest = ordered[-1] if ordered else None
    result: dict[str, Any] = {
        "row_count": len(rows),
        "valid_timestamp_count": len(parsed),
        "invalid_timestamp_count": invalid_timestamp_count,
        "duplicate_timestamp_count": duplicate_count,
        "out_of_order": original_order != sorted(original_order),
        "first_at": ordered[0].isoformat() if ordered else None,
        "last_at": latest.isoformat() if latest else None,
        "stale_minutes": round((now - latest).total_seconds() / 60, 1)
        if latest
        else None,
        "max_gap_minutes": round(max_gap, 1) if max_gap is not None else None,
        "expected_interval_minutes": expected_minutes,
    }
    warnings = []
    if invalid_timestamp_count:
        warnings.append("invalid_timestamps")
    if duplicate_count and not allow_duplicate_times:
        warnings.append("duplicate_timestamps")
    if expected_minutes and max_gap and max_gap > expected_minutes * 3:
        warnings.append("large_gap")
    result["warnings"] = warnings
    return result


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StorageSyncError(f"Could not read {path.relative_to(ROOT)}: {exc}") from exc


def load_list(path: Path) -> list[dict[str, Any]]:
    value = load_json(path, [])
    if not isinstance(value, list):
        raise StorageSyncError(f"Expected list in {path.relative_to(ROOT)}")
    return [item for item in value if isinstance(item, dict)]


def load_dict(path: Path) -> dict[str, Any]:
    value = load_json(path, {})
    if not isinstance(value, dict):
        raise StorageSyncError(f"Expected object in {path.relative_to(ROOT)}")
    return value


def dict_rows(payload: dict[str, Any], key: str) -> list[dict[str, Any]]:
    rows = payload.get(key)
    if not isinstance(rows, list):
        return []
    return [item for item in rows if isinstance(item, dict)]


def parse_time(value: Any) -> datetime | None:
    if isinstance(value, datetime):
        return ensure_utc(value)
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = f"{text[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        return None
    return ensure_utc(parsed)


def normalize_timestamp(value: Any) -> str:
    parsed = parse_time(value)
    if parsed is None:
        raise StorageSyncError(f"Invalid timestamp: {value!r}")
    return parsed.isoformat()


def ensure_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def in_window(value: Any, since: datetime, now: datetime) -> bool:
    parsed = parse_time(value)
    return parsed is not None and since <= parsed <= now + timedelta(minutes=2)


def canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def deterministic_gzip(value: bytes) -> bytes:
    body = bytearray(gzip.compress(value, compresslevel=6, mtime=0))
    # Python 3.11 delegates mtime=0 to zlib, whose gzip OS byte can vary by
    # platform. Normalize it so an immutable object key never maps to a
    # different compressed body on Windows versus GitHub's Linux runner.
    if len(body) >= 10:
        body[9] = 255
    return bytes(body)


def compact_time(value: str) -> str:
    return parse_time(value).strftime("%Y%m%dT%H%M%SZ")


def polymarket_source_id(row: dict[str, Any]) -> str:
    market = row.get("market_slug") or row.get("event_slug") or "unknown_market"
    outcome = row.get("token_id") or row.get("outcome_name") or "unknown_outcome"
    profile = row.get("profile") or "context"
    return stable_source_id(
        "polymarket",
        f"{profile}|{market}|{outcome}",
    )


def stable_source_id(prefix: str, value: str) -> str:
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return f"{prefix}:{digest[:40]}"


def raw_family(filename: str) -> str:
    normalized = filename.lower()
    families = (
        ("polymarket_alert_", "polymarket_flow"),
        ("dune_large_flows_", "dune_flow"),
        ("polymarket_", "polymarket"),
        ("hip4_", "hip4"),
        ("gdelt_", "gdelt"),
        ("rss_", "rss"),
        ("macro_", "macro"),
        ("fred_", "macro"),
        ("yahoo_", "macro"),
    )
    for prefix, family in families:
        if normalized.startswith(prefix):
            return family
    return "collector"


def is_daily_snapshot(value: Any) -> bool:
    parsed = parse_time(value)
    return parsed is not None and parsed.hour == 0 and parsed.minute < 15


def max_observed_at(objects: Iterable[PreparedObject], fallback: datetime) -> datetime:
    values = [parse_time(item.observed_end) for item in objects]
    valid = [item for item in values if item is not None]
    return max(valid) if valid else fallback


def default_run_id(profile: str, now: datetime) -> str:
    workflow_run = os.getenv("GITHUB_RUN_ID")
    attempt = os.getenv("GITHUB_RUN_ATTEMPT")
    if workflow_run:
        return f"github:{workflow_run}:{attempt or '1'}:{profile}"
    return f"local:{profile}:{now.strftime('%Y%m%dT%H%M%SZ')}"
