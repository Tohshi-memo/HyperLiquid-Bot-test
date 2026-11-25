# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T11:52:27.583972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0816` n `13`; crypto_alt avg `0.0492` n `239`; crypto_major avg `0.267` n `8`; equity avg `0.2317` n `168`; fx avg `-0.0017` n `6`; index avg `0.0277` n `27`; metal avg `0.0143` n `20`; unknown avg `0.3184` n `1263`
- 1h: commodity avg `0.0719` n `13`; crypto_alt avg `-0.3562` n `239`; crypto_major avg `-0.0778` n `8`; equity avg `-0.0089` n `168`; fx avg `-0.0202` n `6`; index avg `-0.0376` n `27`; metal avg `-0.1201` n `20`; unknown avg `124.8312` n `1197`
- 4h: commodity avg `0.3118` n `13`; crypto_alt avg `-0.8085` n `239`; crypto_major avg `-0.1967` n `8`; equity avg `-0.6052` n `168`; fx avg `0.0212` n `6`; index avg `-0.1198` n `27`; metal avg `-0.1228` n `20`; unknown avg `126.8156` n `1177`
- 24h: commodity avg `0.2797` n `13`; crypto_alt avg `-2.4473` n `239`; crypto_major avg `-3.2722` n `8`; equity avg `-4.9595` n `167`; fx avg `-0.0339` n `6`; index avg `-0.4718` n `27`; metal avg `-1.1473` n `20`; unknown avg `429.1717` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
