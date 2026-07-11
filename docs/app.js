const DATA = {
  index: "./data/processed/ai_context_index.json",
  canary: "./data/processed/canary_signals.json",
  pack: "./data/processed/ai_analysis_pack.json",
  context: "./data/processed/market_context.json",
  polymarketOutcomeHistory: "./data/processed/polymarket_outcome_latest.json",
  flow: "./data/processed/flow_alert.json",
  macro: "./data/processed/macro_indicators_latest.json",
  assetFeatures: "./data/processed/asset_features_latest.json",
  assetReport: "./data/reports/latest_asset_universe.md",
  hip4: "./data/processed/hip4_outcome_latest.json",
  relationship: "./data/processed/relationship_scan_latest.json",
  sectorReactions: "./data/processed/sector_reactions_latest.json",
};

const CLASS_ORDER = [
  "crypto_major",
  "crypto_alt",
  "equity",
  "index",
  "metal",
  "commodity",
  "fx",
  "unknown",
];

let polymarketPeopleHistory = [];
let polymarketPeopleControlsReady = false;
let polymarketPeopleExpanded = false;
let hip4Data = null;
let hip4Expanded = false;

async function loadJson(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
}

async function loadText(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.text();
}

function text(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value ?? "--";
}

function setBadge(id, value, tone) {
  const node = document.getElementById(id);
  if (!node) return;
  node.textContent = value;
  node.className = `badge badge--${tone}`;
}

function fmtNumber(value, digits = 2) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
  return Number(value).toLocaleString("en-US", {
    maximumFractionDigits: digits,
    minimumFractionDigits: Math.abs(Number(value)) < 10 ? Math.min(digits, 2) : 0,
  });
}

function fmtPct(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
  const number = Number(value);
  const sign = number > 0 ? "+" : "";
  return `${sign}${number.toFixed(2)}%`;
}

function fmtRate(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
  return `${(Number(value) * 100).toFixed(1)}%`;
}

function toneForScore(value, inverse = false) {
  const number = Number(value);
  if (Number.isNaN(number)) return "neutral";
  if (inverse) {
    if (number >= 70) return "risk";
    if (number >= 50) return "watch";
    return "good";
  }
  if (number >= 70) return "good";
  if (number >= 40) return "watch";
  return "neutral";
}

function readiness(index, pack) {
  const labels = pack?.dataset_summary?.label_counts || {};
  const records = index?.dataset_health?.asset_price_active_records || 0;
  if ((labels["24h"] || 0) > 0 && (labels["72h"] || 0) > 0 && records >= 96) return ["ready", "good"];
  if ((labels["1h"] || 0) >= 48 || (labels["4h"] || 0) >= 16) return ["partial", "watch"];
  return ["hold", "risk"];
}

function renderMetrics(index, context, flow, pack) {
  const scores = context?.scores || {};
  const flowScores = flow?.scores || {};
  const flowData = flow?.large_flows || {};
  const poly = flow?.polymarket || {};
  const [readinessLabel, readinessTone] = readiness(index, pack);

  setBadge("readinessBadge", readinessLabel, readinessTone);
  text("updatedAt", formatDate(latestTimestamp([
    context?.generated_at,
    flow?.generated_at,
    pack?.generated_at,
    pack?.updated_at,
    index?.updated_at,
  ])));
  setBadge("flowLevel", flowScores.flow_alert_level || "baseline", flowTone(flowScores.flow_alert_score));
  setBadge("correlationStatus", index?.canary_summary?.status || "unknown", index?.canary_summary?.status === "ready" ? "good" : "watch");

  text("marketContextScore", fmtNumber(scores.market_context_score));
  document.getElementById("marketContextScore")?.classList.add(`score-${toneForScore(scores.market_context_score)}`);
  text("newsRiskScore", fmtNumber(scores.news_risk_score));
  text("macroRiskScore", fmtNumber(scores.macro_risk_score));
  text("riskOnScore", fmtNumber(scores.risk_on_score));
  text("flowAlertScore", fmtNumber(flowScores.flow_alert_score));
  text("polyZScore", fmtNumber(poly.volume_24h_zscore_7d));
  text("largeUsdc", fmtNumber(flowData.large_usdc_inflow, 0));

  const health = index?.dataset_health || {};
  const labels = pack?.dataset_summary?.label_counts || health.day_swing_label_counts || {};
  text("assetPriceRecords", fmtNumber(health.asset_price_active_records, 0));
  text("flowRecords", fmtNumber(health.flow_alert_history_records, 0));
  text("label1h", fmtNumber(labels["1h"], 0));
  text("label4h", fmtNumber(labels["4h"], 0));
  text("label24h", fmtNumber(labels["24h"], 0));
  text("label72h", fmtNumber(labels["72h"], 0));
}

function latestTimestamp(values) {
  const dates = values
    .filter(Boolean)
    .map((value) => ({ value, time: new Date(value).getTime() }))
    .filter((item) => !Number.isNaN(item.time));
  dates.sort((a, b) => b.time - a.time);
  return dates[0]?.value || values.find(Boolean) || null;
}

function flowTone(score) {
  const value = Number(score || 0);
  if (value >= 60) return "risk";
  if (value >= 35) return "watch";
  return "good";
}

function formatDate(value) {
  if (!value) return "--";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString("en-US", { month: "short", day: "2-digit", hour: "2-digit", minute: "2-digit" });
}

function renderCanary(canary) {
  const list = document.getElementById("canaryList");
  if (!list) return;
  const signals = Array.isArray(canary?.signals) ? canary.signals : [];
  list.innerHTML = signals
    .map((item) => {
      const tone = Math.abs(Number(item.score || 0)) >= 35 ? "watch" : "neutral";
      return `
        <article class="signal">
          <strong>${escapeHtml(item.name || "signal")} <span class="badge badge--${tone}">${fmtNumber(item.score)}</span></strong>
          <p>${escapeHtml(item.message || "")}</p>
        </article>
      `;
    })
    .join("") || `<article class="signal"><strong>No signal</strong><p>Waiting for data.</p></article>`;
}

function renderSymbols(pack) {
  const tbody = document.getElementById("symbolsTable");
  if (!tbody) return;
  const latest = pack?.latest_compact?.symbols || {};
  const stats1h = pack?.horizon_stats?.["1h"]?.by_symbol || {};
  const stats4h = pack?.horizon_stats?.["4h"]?.by_symbol || {};
  tbody.innerHTML = Object.keys(latest)
    .map((symbol) => {
      const row = latest[symbol] || {};
      const oneHour = row.features?.["1h"] || {};
      const s1 = stats1h[symbol] || {};
      const s4 = stats4h[symbol] || {};
      return `
        <tr>
          <td><strong>${escapeHtml(symbol)}</strong></td>
          <td>${fmtNumber(row.price, 4)}</td>
          <td class="${classForPct(s1.avg_return_pct)}">${fmtPct(s1.avg_return_pct)}</td>
          <td>${fmtNumber(s1.long_win_rate_pct)}%</td>
          <td class="${classForPct(s4.avg_return_pct)}">${fmtPct(s4.avg_return_pct)}</td>
          <td>${fmtNumber(s4.long_win_rate_pct)}%</td>
          <td>${fmtNumber(oneHour.rsi_14)}</td>
          <td class="${classForPct(oneHour.return_12_pct)}">${fmtPct(oneHour.return_12_pct)}</td>
        </tr>
      `;
    })
    .join("");
}

function renderAssetClasses(index, canary) {
  const tbody = document.getElementById("assetClassTable");
  if (!tbody) return;
  const counts = index?.dataset_health?.asset_class_counts || {};
  const returns = canary?.class_returns || {};
  tbody.innerHTML = CLASS_ORDER
    .filter((assetClass) => counts[assetClass] !== undefined)
    .map((assetClass) => {
      const ret15 = returns["15m"]?.[assetClass]?.avg_return_pct;
      const ret1 = returns["1h"]?.[assetClass]?.avg_return_pct;
      const ret4 = returns["4h"]?.[assetClass]?.avg_return_pct;
      return `
        <tr>
          <td><strong>${escapeHtml(assetClass)}</strong></td>
          <td>${fmtNumber(counts[assetClass], 0)}</td>
          <td class="${classForPct(ret15)}">${fmtPct(ret15)}</td>
          <td class="${classForPct(ret1)}">${fmtPct(ret1)}</td>
          <td class="${classForPct(ret4)}">${fmtPct(ret4)}</td>
        </tr>
      `;
    })
    .join("");
}

function renderMovers(markdown) {
  renderList("topVolume", sectionItems(markdown, "Top By Volume"));
  renderList("topGainers", sectionItems(markdown, "Top 24h Gainers"));
  renderList("topLosers", sectionItems(markdown, "Top 24h Losers"));
}

function sectionItems(markdown, heading) {
  const lines = markdown.split(/\r?\n/);
  const start = lines.findIndex((line) => line.trim() === `## ${heading}`);
  if (start < 0) return [];
  const items = [];
  for (const line of lines.slice(start + 1)) {
    if (line.startsWith("## ")) break;
    if (line.startsWith("- ")) items.push(line.slice(2).replaceAll("`", ""));
    if (items.length >= 5) break;
  }
  return items;
}

function renderList(id, items) {
  const node = document.getElementById(id);
  if (!node) return;
  node.innerHTML = items.map((item) => `<li>${escapeHtml(item)}</li>`).join("") || "<li>No data</li>";
}

function classForPct(value) {
  const number = Number(value);
  if (Number.isNaN(number)) return "";
  if (number > 0) return "positive";
  if (number < 0) return "negative";
  return "";
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

async function renderDashboard() {
  try {
    const [index, canary, pack, context, polymarketOutcomeHistory, flow, macro, assetFeatures, assetReport, relationship, sectorReactions] = await Promise.all([
      loadJson(DATA.index),
      loadJson(DATA.canary),
      loadJson(DATA.pack),
      loadJson(DATA.context),
      loadJson(DATA.polymarketOutcomeHistory).catch(() => []),
      loadJson(DATA.flow),
      loadJson(DATA.macro).catch(() => null),
      loadJson(DATA.assetFeatures).catch(() => null),
      loadText(DATA.assetReport),
      loadJson(DATA.relationship).catch(() => null),
      loadJson(DATA.sectorReactions).catch(() => null),
    ]);

    renderMetrics(index, context, flow, pack);
    renderCanary(canary);
    renderIntelligence(context, flow);
    renderPolymarketPeople(polymarketOutcomeHistory);
    renderNewsCategories(context);
    renderMacroIndicators(macro);
    renderSectorReactions(sectorReactions);
    renderGdelt(context);
    renderFlowDetail(flow);
    renderRelationshipScan(relationship);
    renderIndividualSignals(assetFeatures);
    renderSymbols(pack);
    renderAssetClasses(index, canary);
    renderMovers(assetReport);
  } catch (error) {
    setBadge("readinessBadge", "data error", "risk");
    text("updatedAt", error.message);
  }

  loadJson(DATA.hip4).then(renderHip4).catch(() => {
    setBadge("hip4Badge", "no data", "neutral");
    const node = document.getElementById("hip4List");
    if (node) node.innerHTML = emptyCard("HIP-4 data not yet available.");
  });
}

function renderIndividualSignals(assetFeatures) {
  const node = document.getElementById("individualSignalsList");
  if (!node) return;
  const rows = collectAssetFeatureRows(assetFeatures);
  const selected = rows
    .filter(isReadableDashboardAsset)
    .filter((row) => row.best_relationship || ["equity", "commodity", "metal", "index", "fx", "crypto_major"].includes(row.asset_class))
    .sort((a, b) => {
      const relEdge = Number(b.best_relationship?.score || 0) - Number(a.best_relationship?.score || 0);
      if (relEdge !== 0) return relEdge;
      return Number(b.activity_score || 0) - Number(a.activity_score || 0);
    })
    .slice(0, 6);
  node.innerHTML = selected.map((row) => {
    const rel = row.best_relationship || {};
    return `
      <article class="item-card">
        <strong>${escapeHtml(row.symbol)} <span class="muted">${escapeHtml(row.asset_class || "")}</span></strong>
        <div class="meta-line">
          <span>price ${fmtNumber(row.price, 4)}</span>
          <span>4h ${fmtPct(row.returns?.["4h"])}</span>
          <span>24h ${fmtPct(row.returns?.["24h"])}</span>
        </div>
        <div class="meta-line">
          <span>vol ${fmtNumber(row.day_ntl_vlm, 0)}</span>
          <span>${escapeHtml(rel.condition || "no pattern")}</span>
          <span>score ${fmtNumber(rel.score, 2)}</span>
        </div>
      </article>
    `;
  }).join("") || emptyCard("Individual asset signals will appear after the next context run.");
}

function collectAssetFeatureRows(assetFeatures) {
  const map = new Map();
  const addRows = (rows) => {
    if (!Array.isArray(rows)) return;
    for (const row of rows) {
      if (row && row.symbol && !map.has(row.symbol)) map.set(row.symbol, row);
    }
  };
  addRows(assetFeatures?.top_assets);
  const byClass = assetFeatures?.by_class || {};
  for (const summary of Object.values(byClass)) {
    addRows(summary?.top_activity);
    addRows(summary?.top_volume);
    addRows(summary?.top_4h_return);
    addRows(summary?.bottom_4h_return);
    addRows(summary?.top_24h_return);
    addRows(summary?.bottom_24h_return);
  }
  return [...map.values()];
}

function isReadableDashboardAsset(row) {
  const symbol = String(row?.symbol || "");
  const assetClass = String(row?.asset_class || "unknown");
  const volume = Number(row?.day_ntl_vlm || 0);
  const openInterest = Number(row?.open_interest || 0);
  if (assetClass !== "unknown") return true;
  return !/^[@#]/.test(symbol) || volume > 0 || openInterest > 0;
}

renderDashboard();
setInterval(renderDashboard, 5 * 60 * 1000);

function setupBackToTop() {
  const button = document.querySelector(".back-to-top");
  if (!button) return;
  const update = () => button.classList.toggle("is-visible", window.scrollY > 520);
  update();
  window.addEventListener("scroll", update, { passive: true });
}

setupBackToTop();

function renderIntelligence(context, flow) {
  renderPolymarket(context, flow);
  renderHealthPolymarket(context, flow);
  renderHeadlines(context);
}

function renderPolymarket(context, flow) {
  const node = document.getElementById("polymarketList");
  if (!node) return;
  const flowMarkets = Array.isArray(flow?.polymarket?.top_markets) ? flow.polymarket.top_markets : [];
  const contextMarkets = Array.isArray(context?.polymarket?.top_markets) ? context.polymarket.top_markets : [];
  const markets = mergeMarkets(contextMarkets, flowMarkets);
  node.innerHTML = markets.slice(0, 6).map((market) => {
    const volume24h = market.volume_24h !== undefined ? market.volume_24h : market.volume;
    const endDate = market.end_date || market.endDate;
    const odds = renderOutcomeOdds(market);
    return `
      <article class="item-card">
        <strong>${escapeHtml(market.question || market.title || "Untitled market")}</strong>
        ${odds}
        <div class="meta-line">
          <span>24h vol ${fmtNumber(volume24h, 0)}</span>
          <span>liquidity ${fmtNumber(market.liquidity, 0)}</span>
        </div>
        <div class="meta-line">
          <span>end ${formatDate(endDate)}</span>
          <span>${escapeHtml(market.impact_category || market.query || market.slug || "")}</span>
        </div>
        ${renderPolymarketAction(market)}
      </article>
    `;
  }).join("") || emptyCard("No active Polymarket markets.");
}

function renderHealthPolymarket(context, flow) {
  const node = document.getElementById("healthPolymarketList");
  if (!node) return;
  const contextMarkets = Array.isArray(context?.polymarket?.health_markets) ? context.polymarket.health_markets : [];
  const flowMarkets = Array.isArray(flow?.polymarket?.health_markets) ? flow.polymarket.health_markets : [];
  const fallbackMarkets = mergeMarkets(
    Array.isArray(context?.polymarket?.top_markets) ? context.polymarket.top_markets : [],
    Array.isArray(flow?.polymarket?.top_markets) ? flow.polymarket.top_markets : [],
  ).filter(isHealthMarket);
  const markets = mergeMarkets([...contextMarkets, ...flowMarkets], fallbackMarkets).filter(isHealthMarket);
  node.innerHTML = markets.slice(0, 8).map((market) => {
    const volume24h = market.volume_24h !== undefined ? market.volume_24h : market.volume;
    const endDate = market.end_date || market.endDate;
    return `
      <article class="item-card">
        <strong>${escapeHtml(market.question || market.title || "Untitled market")}</strong>
        ${renderOutcomeOdds(market)}
        <div class="meta-line">
          <span>24h vol ${fmtNumber(volume24h, 0)}</span>
          <span>liquidity ${fmtNumber(market.liquidity, 0)}</span>
        </div>
        <div class="meta-line">
          <span>end ${formatDate(endDate)}</span>
          <span>${escapeHtml(market.impact_category || market.query || market.slug || "")}</span>
        </div>
        ${renderPolymarketAction(market)}
      </article>
    `;
  }).join("") || emptyCard("No pandemic or public-health Polymarket markets collected yet.");
}

function renderPolymarketPeople(history) {
  polymarketPeopleHistory = Array.isArray(history) ? history : [];
  setupPolymarketPeopleControls(polymarketPeopleHistory);
  renderPolymarketPeopleList();
}

function setupPolymarketPeopleControls(rows) {
  const eventSelect = document.getElementById("polymarketPeopleEvent");
  const searchInput = document.getElementById("polymarketPeopleSearch");
  const sortSelect = document.getElementById("polymarketPeopleSort");
  const toggle = document.getElementById("polymarketPeopleToggle");
  const events = [...new Set(rows.map((row) => row?.event_slug).filter(Boolean))].sort();
  if (eventSelect) {
    const selected = eventSelect.value;
    eventSelect.innerHTML = `<option value="">All events</option>` + events
      .map((slug) => `<option value="${escapeHtml(slug)}">${escapeHtml(slug)}</option>`)
      .join("");
    eventSelect.value = events.includes(selected) ? selected : "";
    if (!polymarketPeopleControlsReady) {
      eventSelect.addEventListener("change", renderPolymarketPeopleList);
    }
  }
  if (!polymarketPeopleControlsReady) {
    searchInput?.addEventListener("input", renderPolymarketPeopleList);
    sortSelect?.addEventListener("change", renderPolymarketPeopleList);
    toggle?.addEventListener("click", () => {
      polymarketPeopleExpanded = !polymarketPeopleExpanded;
      renderPolymarketPeopleList();
    });
  }
  polymarketPeopleControlsReady = true;
}

function renderPolymarketPeopleList() {
  const node = document.getElementById("polymarketPeopleList");
  if (!node) return;
  const query = String(document.getElementById("polymarketPeopleSearch")?.value || "").trim().toLowerCase();
  const event = String(document.getElementById("polymarketPeopleEvent")?.value || "");
  const sort = String(document.getElementById("polymarketPeopleSort")?.value || "volume");
  const latest = latestPolymarketPeopleRows(polymarketPeopleHistory)
    .filter((row) => !event || row.event_slug === event)
    .filter((row) => {
      if (!query) return true;
      return [
        row.person_name,
        row.subject_name,
        row.outcome_name,
        row.event_slug,
        row.question,
      ].join(" ").toLowerCase().includes(query);
    });
  sortPolymarketPeopleRows(latest, sort);
  setBadge("polymarketPeopleCount", `${fmtNumber(latest.length, 0)} people`, latest.length ? "good" : "neutral");
  const visibleLimit = polymarketPeopleExpanded ? latest.length : 10;
  const visibleRows = latest.slice(0, visibleLimit);
  const summary = document.getElementById("polymarketPeopleSummary");
  const toggle = document.getElementById("polymarketPeopleToggle");
  if (summary) summary.textContent = `Showing ${fmtNumber(visibleRows.length, 0)} of ${fmtNumber(latest.length, 0)} matching people`;
  if (toggle) {
    toggle.hidden = latest.length <= 10;
    toggle.textContent = polymarketPeopleExpanded ? "Show less" : `Show all ${fmtNumber(latest.length, 0)}`;
  }
  node.innerHTML = visibleRows.map((row) => {
    const name = row.person_name || row.subject_name || row.outcome_name || "Unknown";
    const href = row.event_slug
      ? `https://polymarket.com/event/${encodeURIComponent(String(row.event_slug))}`
      : row.market_slug
        ? `https://polymarket.com/market/${encodeURIComponent(String(row.market_slug))}`
        : null;
    const title = href
      ? `<a href="${escapeHtml(href)}" target="_blank" rel="noopener noreferrer">${escapeHtml(name)}</a>`
      : escapeHtml(name);
    return `
      <article class="item-card">
        <strong>${title} <span class="badge badge--neutral">${formatProbability(row.probability)}</span></strong>
        <div class="meta-line">
          <span>${escapeHtml(row.outcome_name || "Outcome")}</span>
          <span>${escapeHtml(row.impact_category || "")}</span>
          <span>${formatDate(row.observed_at)}</span>
        </div>
        <div class="meta-line">
          <span>24h vol ${fmtNumber(row.volume_24h, 0)}</span>
          <span>liquidity ${fmtNumber(row.liquidity, 0)}</span>
        </div>
        <small>${escapeHtml(row.question || "")}</small>
      </article>
    `;
  }).join("") || emptyCard("Person-level Polymarket history will appear after the next context run.");
}

function latestPolymarketPeopleRows(rows) {
  const map = new Map();
  for (const row of rows) {
    if (!row || !(row.person_name || row.subject_name || row.outcome_name)) continue;
    if (String(row.outcome_name || "").trim().toLowerCase() === "no") continue;
    if (row.probability === null || row.probability === undefined) continue;
    const key = [
      row.event_slug || "",
      row.market_slug || "",
      row.token_id || row.outcome_name || "",
    ].join(":");
    const current = map.get(key);
    if (!current || String(row.observed_at || "") > String(current.observed_at || "")) {
      map.set(key, row);
    }
  }
  return [...map.values()];
}

function sortPolymarketPeopleRows(rows, sort) {
  rows.sort((a, b) => {
    if (sort === "name") {
      return String(a.person_name || a.subject_name || a.outcome_name || "")
        .localeCompare(String(b.person_name || b.subject_name || b.outcome_name || ""));
    }
    if (sort === "probability") {
      return Number(b.probability || 0) - Number(a.probability || 0);
    }
    const volumeDelta = Number(b.volume_24h || 0) - Number(a.volume_24h || 0);
    if (volumeDelta !== 0) return volumeDelta;
    return Number(b.probability || 0) - Number(a.probability || 0);
  });
}

function renderPolymarketAction(market) {
  const href = polymarketUrl(market);
  if (!href) return "";
  return `
    <div class="market-action">
      <a href="${escapeHtml(href)}" target="_blank" rel="noopener noreferrer">Open market</a>
    </div>
  `;
}

function polymarketUrl(market) {
  const rawUrl = market?.url || market?.market_url;
  if (typeof rawUrl === "string" && rawUrl.startsWith("https://polymarket.com/")) return rawUrl;
  const eventSlug = market?.event_slug || market?.eventSlug;
  if (eventSlug) return `https://polymarket.com/event/${encodeURIComponent(String(eventSlug))}`;
  const slug = market?.slug;
  if (!slug) return null;
  return `https://polymarket.com/event/${encodeURIComponent(String(slug))}`;
}

function renderOutcomeOdds(market) {
  const yes = market.yes_probability;
  const no = market.no_probability;
  if (yes !== null && yes !== undefined || no !== null && no !== undefined) {
    return `
      <div class="meta-line">
        <span>Yes ${formatProbability(yes)}</span>
        <span>No ${formatProbability(no)}</span>
      </div>
    `;
  }
  const outcomes = Array.isArray(market.outcomes) ? market.outcomes : [];
  const priced = outcomes.filter((outcome) => outcome?.probability !== null && outcome?.probability !== undefined);
  if (!priced.length) return "";
  return `
    <div class="meta-line">
      ${priced.slice(0, 3).map((outcome) => `<span>${escapeHtml(outcome.name || "Outcome")} ${formatProbability(outcome.probability)}</span>`).join("")}
    </div>
  `;
}

function formatProbability(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
  return `${(Number(value) * 100).toFixed(1)}%`;
}

function isHealthMarket(market) {
  const text = [
    market?.question,
    market?.title,
    market?.slug,
    market?.impact_category,
    market?.query,
  ].join(" ").toLowerCase();
  return /\b(pandemic|covid|covid-19|coronavirus|virus|disease|outbreak|bird flu|avian flu|h5n1|h5n5|hantavirus|public health|world health organization|who declare|who declares|who emergency|who pandemic|who outbreak|vaccine|mpox|ebola)\b/.test(text);
}

function mergeMarkets(primary, secondary) {
  const map = new Map();
  for (const market of [...primary, ...secondary]) {
    const key = market.slug || market.question || market.title;
    if (!key || map.has(key)) continue;
    map.set(key, market);
  }
  return [...map.values()];
}

function renderHeadlines(context) {
  const node = document.getElementById("headlinesList");
  if (!node) return;
  const headlines = Array.isArray(context?.news?.top_headlines) ? context.news.top_headlines : [];
  node.innerHTML = headlines.slice(0, 8).map((item) => {
    const title = escapeHtml(item.title || "Untitled headline");
    const href = item.url ? escapeHtml(item.url) : "";
    const titleHtml = href
      ? `<a href="${href}" target="_blank" rel="noopener noreferrer">${title}</a>`
      : title;
    return `
      <article class="item-card">
        <strong>${titleHtml}</strong>
        <div class="meta-line">
          <span>${escapeHtml([item.category, item.source || "unknown source"].filter(Boolean).join(" / "))}</span>
          <span>${formatDate(item.published_at)}</span>
        </div>
      </article>
    `;
  }).join("") || emptyCard("No recent headlines.");
}

function renderNewsCategories(context) {
  const node = document.getElementById("newsCategoryList");
  if (!node) return;
  const categories = context?.news?.categories || {};
  const rows = Object.entries(categories);
  node.innerHTML = rows.map(([category, summary]) => `
    <div class="detail-row">
      <span>${escapeHtml(category)}</span>
      <strong>${fmtNumber(summary?.article_count, 0)} articles</strong>
      <small>${fmtNumber(summary?.risk_keyword_hits, 0)} risk words / ${fmtRate(summary?.risk_headline_rate)} risk headlines</small>
    </div>
  `).join("") || emptyCard("No category summary.");
}

function renderMacroIndicators(macro) {
  const node = document.getElementById("macroIndicatorList");
  if (!node) return;
  const rows = Array.isArray(macro?.indicators) ? macro.indicators : [];
  const priority = [
    "us_10y_yield",
    "us_2y_yield",
    "us_10y_2y_spread",
    "fed_funds_effective",
    "us_unemployment_rate",
    "us_nonfarm_payrolls",
    "us_cpi_u",
    "us_core_cpi_u",
    "vix",
    "dollar_index_broad",
  ];
  const byKey = new Map(rows.map((row) => [row.key, row]));
  const selected = [
    ...priority.map((key) => byKey.get(key)).filter(Boolean),
    ...rows.filter((row) => !priority.includes(row.key)).slice(0, 8),
  ].slice(0, 10);
  const indicatorHtml = selected.map((row) => `
    <div class="detail-row">
      <span>${escapeHtml(row.name || row.key)}</span>
      <strong>${fmtNumber(row.value, 4)} ${escapeHtml(row.unit || "")}</strong>
      <small>${escapeHtml([row.source, row.observed_at, row.category].filter(Boolean).join(" / "))}</small>
    </div>
  `).join("") || emptyCard("Macro indicators will appear after the next context run.");
  const releaseRows = Array.isArray(macro?.release_calendar) ? macro.release_calendar : [];
  const releaseHtml = releaseRows.slice(0, 6).map((row) => `
    <div class="detail-row">
      <span>${escapeHtml(row.name || row.key)}</span>
      <strong>${formatDate(row.scheduled_for || row.scheduled_utc)}</strong>
      <small>${escapeHtml([row.reference_period, row.source, row.calendar_status].filter(Boolean).join(" / "))}</small>
    </div>
  `).join("");
  node.innerHTML = indicatorHtml + (releaseHtml ? `
    <div class="section-subtitle">Upcoming macro releases</div>
    ${releaseHtml}
  ` : "");
}

function renderSectorReactions(sectorReactions) {
  const node = document.getElementById("sectorReactionList");
  if (!node) return;
  const snapshot = Array.isArray(sectorReactions?.sector_snapshot) ? sectorReactions.sector_snapshot : [];
  const patterns = Array.isArray(sectorReactions?.top_patterns) ? sectorReactions.top_patterns : [];
  if (!snapshot.length && !patterns.length) {
    node.innerHTML = emptyCard("Sector reaction data will appear after the next context run.");
    return;
  }
  const snapshotHtml = snapshot.slice(0, 6).map((row) => `
    <article class="item-card">
      <strong>${escapeHtml(row.proxy)} <span class="muted">${escapeHtml(row.sector || "")}</span></strong>
      <div class="meta-line">
        <span>5d ${fmtPct(row.return_5d_pct)}</span>
        <span>20d ${fmtPct(row.return_20d_pct)}</span>
        <span>60d ${fmtPct(row.return_60d_pct)}</span>
      </div>
      <div class="meta-line">
        <span>price ${fmtNumber(row.price, 2)}</span>
        <span>${formatDate(row.date)}</span>
      </div>
    </article>
  `).join("");
  const patternHtml = patterns.slice(0, 6).map((row) => `
    <article class="item-card">
      <strong>${escapeHtml(shortSectorPattern(row.pattern_id || ""))}</strong>
      <div class="meta-line">
        <span>${escapeHtml(row.proxy || "")}</span>
        <span>${escapeHtml(row.horizon || "")}</span>
        <span>n ${fmtNumber(row.sample_count, 0)}</span>
      </div>
      <div class="meta-line">
        <span>avg ${fmtPct(row.avg_return_pct)}</span>
        <span>up ${fmtNumber(row.up_rate_pct, 1)}%</span>
        <span>score ${fmtNumber(row.score, 2)}</span>
      </div>
    </article>
  `).join("");
  node.innerHTML = `
    <article class="chart-card">
      <div class="chart-head">
        <strong>Current Sector Moves</strong>
        <span>${fmtNumber(sectorReactions?.price_record_count, 0)} daily records</span>
      </div>
      <div class="relationship-cards">${snapshotHtml || emptyCard("No sector snapshot.")}</div>
    </article>
    <article class="chart-card">
      <div class="chart-head">
        <strong>Delayed-Reaction Patterns</strong>
        <span>1d to 252d horizons</span>
      </div>
      <div class="relationship-cards">${patternHtml || emptyCard("No sector patterns yet.")}</div>
    </article>
  `;
}

function shortSectorPattern(value) {
  return String(value || "pattern")
    .replace("news_risk_high", "news risk")
    .replace("macro_risk_high", "macro risk")
    .replace("risk_on_high", "risk-on")
    .replace("market_context_high", "context")
    .replace("polymarket_volume_spike", "poly spike")
    .replace("flow_alert_high", "flow")
    .replace("energy_5d_up", "energy +5d")
    .replace("semis_5d_up", "semis +5d")
    .replace("rates_sensitive_rebound", "rates-sensitive rebound")
    .replace("defensive_rotation", "defensive rotation")
    .replace("broad_risk_on_20d", "broad risk-on")
    .replace("small_caps_5d_up", "small caps +5d")
    .replace("->", " -> ");
}

function renderGdelt(context) {
  const node = document.getElementById("gdeltList");
  if (!node) return;
  const rows = Array.isArray(context?.gdelt?.queries) ? context.gdelt.queries : [];
  const errors = Array.isArray(context?.errors) ? context.errors.filter((item) => String(item).startsWith("GDELT")) : [];
  const activity = rows.map((row) => `
    <div class="detail-row">
      <span>${escapeHtml(row.query || "query")}</span>
      <strong>${fmtNumber(row.latest_volume)} latest</strong>
      <small>${fmtNumber(row.avg_volume)} avg / ${fmtNumber(row.points, 0)} points</small>
    </div>
  `).join("");
  const errorRows = errors.map((error) => {
    const summary = summarizeGdeltError(error);
    return `
      <div class="detail-row detail-row--warning">
        <span>${escapeHtml(summary.query)}</span>
        <strong>warning</strong>
        <small>${escapeHtml(summary.message)}</small>
      </div>
    `;
  }).join("");
  node.innerHTML = activity + errorRows || emptyCard("No GDELT activity.");
}

function summarizeGdeltError(error) {
  const textValue = String(error || "");
  const cleaned = textValue.replace(/^GDELT\s+/i, "");
  const [queryPart, ...rest] = cleaned.split(":");
  const detail = rest.join(":").trim();
  let message = "GDELT temporarily returned an error. The dashboard keeps the latest available public data.";

  if (detail.includes("429") || /too many requests/i.test(detail)) {
    message = "GDELT rate-limited this request. This is temporary and does not stop the other collectors.";
  } else if (/expecting value|json|empty/i.test(detail)) {
    message = "GDELT returned an empty or non-JSON response. Other news and market data remain available.";
  } else if (detail) {
    message = "GDELT request failed temporarily. Other public data is still being collected.";
  }

  return {
    query: queryPart ? `GDELT: ${queryPart.trim()}` : "GDELT",
    message,
  };
}

function renderFlowDetail(flow) {
  const node = document.getElementById("flowDetailList");
  if (!node) return;
  const large = flow?.large_flows || {};
  const poly = flow?.polymarket || {};
  const rows = [
    ["Dune status", large.enabled ? "enabled" : "not enabled", large.source_state || large.source_reason || "no source state"],
    ["Large tx count", fmtNumber(large.large_usdc_tx_count, 0), "transactions"],
    ["Large USDC inflow", fmtNumber(large.large_usdc_inflow, 0), "USDC"],
    ["Max transfer", fmtNumber(large.max_large_usdc_transfer, 0), "USDC"],
    ["Unique wallets", fmtNumber(large.unique_large_wallets, 0), "wallets"],
    ["Inflow z-score", fmtNumber(large.inflow_zscore_7d), "7d baseline"],
    ["Polymarket 24h volume", fmtNumber(poly.volume_24h, 0), "public markets"],
    ["Polymarket z-score", fmtNumber(poly.volume_24h_zscore_7d), "7d baseline"],
  ];
  const errorRows = Array.isArray(flow?.errors) ? flow.errors : [];
  node.innerHTML = rows.map(([label, value, note]) => `
    <div class="detail-row">
      <span>${escapeHtml(label)}</span>
      <strong>${escapeHtml(value)}</strong>
      <small>${escapeHtml(note)}</small>
    </div>
  `).join("") + errorRows.map((error) => `
    <div class="detail-row detail-row--warning">
      <span>${escapeHtml(error)}</span>
      <strong>warning</strong>
      <small>Flow source returned an issue.</small>
    </div>
  `).join("");
}

function renderRelationshipScan(scan) {
  const node = document.getElementById("relationshipList");
  if (!node) return;
  const rows = Array.isArray(scan?.top_patterns) ? scan.top_patterns : [];
  const ready = rows.filter((row) =>
    row.sample_status === "ready" && Number(row.sample_count || 0) >= Number(scan?.min_samples || 0)
  );
  const positive = ready.filter((row) => Number(row.score || 0) > 0).slice(0, 8);
  const watch = ready.slice(0, 6);

  if (!ready.length) {
    node.innerHTML = emptyCard("Relationship scan will appear after enough samples are ready.");
    return;
  }

  const chart = positive.length >= 2 ? renderRelationshipBarChart(positive) : "";
  const heatmap = positive.length >= 3 ? renderRelationshipHeatmap(ready) : "";
  const cards = watch.map((row) => `
    <article class="item-card">
      <strong>${escapeHtml(row.pattern_id || "pattern")}</strong>
      <div class="meta-line">
        <span>score ${fmtNumber(row.score, 2)}</span>
        <span>n ${fmtNumber(row.sample_count, 0)}</span>
        <span>${escapeHtml(row.sample_status || "")}</span>
      </div>
      <div class="meta-line">
        <span>deltaP ${fmtNumber(row.delta_probability_pct, 2)}%</span>
        <span>edge ${fmtPct(row.edge_return_pct)}</span>
        <span>DD ${fmtPct(row.max_drawdown_pct)}</span>
      </div>
    </article>
  `).join("");

  node.innerHTML = chart + heatmap + `<div class="relationship-cards">${cards}</div>`;
}

function renderRelationshipBarChart(rows) {
  const maxScore = Math.max(...rows.map((row) => Math.max(0, Number(row.score || 0))), 1);
  return `
    <article class="chart-card">
      <div class="chart-head">
        <strong>Top Ready Pattern Scores</strong>
        <span>positive score only</span>
      </div>
      <div class="bar-chart">
        ${rows.map((row) => {
          const score = Math.max(0, Number(row.score || 0));
          const width = Math.max(6, Math.round((score / maxScore) * 100));
          return `
            <div class="bar-row">
              <span>${escapeHtml(shortPattern(row.pattern_id))}</span>
              <div class="bar-track"><i style="width:${width}%"></i></div>
              <strong>${fmtNumber(row.score, 2)}</strong>
            </div>
          `;
        }).join("")}
      </div>
    </article>
  `;
}

function renderRelationshipHeatmap(rows) {
  const horizons = ["1h", "4h", "24h"];
  const targets = [...new Set(rows.map((row) => row.target).filter(Boolean))].slice(0, 8);
  if (!targets.length) return "";
  const best = new Map();
  for (const row of rows) {
    const key = `${row.target}:${row.horizon}`;
    const current = best.get(key);
    if (!current || Number(row.score || -999) > Number(current.score || -999)) best.set(key, row);
  }
  return `
    <article class="chart-card">
      <div class="chart-head">
        <strong>Best Score by Class / Horizon</strong>
        <span>ready samples</span>
      </div>
      <div class="heatmap" style="grid-template-columns: 96px repeat(${horizons.length}, minmax(58px, 1fr));">
        <b></b>
        ${horizons.map((horizon) => `<b>${horizon}</b>`).join("")}
        ${targets.map((target) => `
          <b>${escapeHtml(target)}</b>
          ${horizons.map((horizon) => {
            const row = best.get(`${target}:${horizon}`);
            const score = Number(row?.score || 0);
            const tone = score > 2 ? "good" : score > 0 ? "watch" : "neutral";
            return `<span class="heat heat--${tone}" title="${escapeHtml(row?.pattern_id || "")}">${row ? fmtNumber(score, 2) : "--"}</span>`;
          }).join("")}
        `).join("")}
      </div>
    </article>
  `;
}

function shortPattern(value) {
  return String(value || "pattern")
    .replace("market_context_high", "context")
    .replace("polymarket_volume_spike", "poly spike")
    .replace("news_risk_high", "news risk")
    .replace("macro_risk_high", "macro risk")
    .replace("risk_on_high", "risk-on")
    .replace("flow_alert_high", "flow")
    .replace("->", " -> ");
}

function emptyCard(message) {
  return `<article class="item-card"><strong>${escapeHtml(message)}</strong></article>`;
}

function formatExpiry(expiry) {
  if (!expiry) return "--";
  const match = String(expiry).match(/^(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})$/);
  if (!match) return expiry;
  const [, year, month, day, hour, minute] = match;
  return `${year}-${month}-${day} ${hour}:${minute} UTC`;
}

function buildHip4Question(row) {
  const cls = row.outcome_class || "";
  const underlying = escapeHtml(row.underlying || "?");
  const expiry = escapeHtml(formatExpiry(row.expiry));
  if (cls === "priceBinary") {
    const price = row.target_price != null ? `$${fmtNumber(row.target_price, 0)}` : "?";
    return `Will ${underlying} be above ${price} by ${expiry}?`;
  }
  const rawDescription = row.raw_outcome?.description;
  const outcomeId = row.outcome_id !== null && row.outcome_id !== undefined ? `Outcome #${row.outcome_id}` : "Outcome";
  const baseName = row.outcome_name && !/^Recurring(?: Named Outcome| Fallback)?$/.test(row.outcome_name)
    ? row.outcome_name
    : outcomeId;
  const label = cls || (
    typeof rawDescription === "string" && rawDescription.startsWith("index:") ? "named outcome" : "metadata incomplete"
  );
  if (!row.underlying && !row.expiry && row.target_price == null) {
    return `${escapeHtml(baseName)} (${escapeHtml(label)})`;
  }
  return `${underlying} (${escapeHtml(label)}) - expires ${expiry}`;
}

function renderHip4(hip4) {
  const node = document.getElementById("hip4List");
  if (!node) return;

  hip4Data = hip4;

  const rows = Array.isArray(hip4?.rows) ? hip4.rows : [];
  const errors = Array.isArray(hip4?.request_errors) ? hip4.request_errors : [];
  const warnings = Array.isArray(hip4?.request_warnings) ? hip4.request_warnings : [];

  if (rows.length === 0) {
    setBadge("hip4Badge", "0 markets", "neutral");
    document.getElementById("hip4Summary").textContent = "No markets available";
    document.getElementById("hip4Toggle").hidden = true;
    node.innerHTML = emptyCard("No HIP-4 prediction markets found.");
    return;
  }

  const byOutcome = new Map();
  for (const row of rows) {
    const id = hip4MarketKey(row);
    if (!byOutcome.has(id)) byOutcome.set(id, []);
    byOutcome.get(id).push(row);
  }

  const badgeCount = hip4?.outcome_count || byOutcome.size;
  setBadge("hip4Badge", `${badgeCount} market${Number(badgeCount) !== 1 ? "s" : ""}`, "good");

  const groups = [...byOutcome.values()].sort((a, b) => hip4GroupScore(b) - hip4GroupScore(a));
  const visibleLimit = hip4Expanded ? groups.length : 8;
  const visibleGroups = groups.slice(0, visibleLimit);
  const summary = document.getElementById("hip4Summary");
  const toggle = document.getElementById("hip4Toggle");
  if (summary) summary.textContent = `Showing ${fmtNumber(visibleGroups.length, 0)} of ${fmtNumber(groups.length, 0)} markets`;
  if (toggle) {
    toggle.hidden = groups.length <= 8;
    toggle.textContent = hip4Expanded ? "Show less" : `Show all ${fmtNumber(groups.length, 0)}`;
    if (!toggle.dataset.bound) {
      toggle.dataset.bound = "true";
      toggle.addEventListener("click", () => {
        hip4Expanded = !hip4Expanded;
        renderHip4(hip4Data);
      });
    }
  }
  const unknownCount = groups.filter((sides) => !sides[0]?.underlying && !sides[0]?.expiry && sides[0]?.target_price == null).length;

  const statusHtml = unknownCount
    ? `<article class="item-card item-card--warning"><strong>${fmtNumber(unknownCount, 0)} HIP-4 markets have incomplete metadata</strong><div class="meta-line"><span>Prices are shown from allMids when available. Names fill in automatically when HyperLiquid exposes more outcome metadata.</span></div></article>`
    : "";

  const cards = visibleGroups.map((sides) => {
    const first = sides[0];
    const question = buildHip4Question(first);
    const sideHtml = sides.map((side) => {
      const prob = side.implied_probability != null
        ? `${(Number(side.implied_probability) * 100).toFixed(1)}%`
        : "n/a";
      const probClass = side.implied_probability != null
        ? (Number(side.implied_probability) >= 0.5 ? "positive" : "negative")
        : "";
      const symbol = side.symbol ? ` ${escapeHtml(side.symbol)}` : "";
      return `<span>${escapeHtml(side.side_name)}${symbol}: <strong class="${probClass}">${prob}</strong></span>`;
    }).join(" &nbsp;|&nbsp; ");
    const vol = fmtNumber(first.volume_24h, 0);
    const oi = fmtNumber(first.open_interest, 0);
    const status = first.status ? escapeHtml(first.status) : "active";
    const symbols = sides.map((side) => side.symbol).filter(Boolean).join(" / ");
    const source = sides.map((side) => side.price_source).filter(Boolean)[0] || "metadata";
    const target = first.target_price != null ? `$${fmtNumber(first.target_price, 0)}` : "n/a";
    const expiry = formatExpiry(first.expiry);
    const rawDescription = first.raw_outcome?.description;
    const detailNote = rawDescription && (!first.underlying || !first.expiry || first.target_price == null)
      ? `<div class="meta-line"><span>source detail ${escapeHtml(rawDescription)}</span></div>`
      : "";
    return `
      <article class="item-card">
        <strong>${question}</strong>
        <div class="meta-line">${sideHtml}</div>
        <div class="meta-line">
          <span>expiry ${escapeHtml(expiry)}</span>
          <span>target ${escapeHtml(target)}</span>
        </div>
        <div class="meta-line">
          <span>vol 24h ${vol}</span>
          <span>OI ${oi}</span>
          <span>${status}</span>
        </div>
        <div class="meta-line">
          <span>${escapeHtml(symbols || "symbols pending")}</span>
          <span>price ${escapeHtml(source)}</span>
        </div>
        ${detailNote}
      </article>
    `;
  });

  const errorHtml = errors.length
    ? `<article class="item-card item-card--warning"><strong>Price data unavailable</strong><div class="meta-line"><span>${escapeHtml(errors[0])}</span></div></article>`
    : "";
  const warningHtml = warnings.length
    ? `<article class="item-card item-card--warning"><strong>Context endpoint unavailable</strong><div class="meta-line"><span>Prices are still filled from allMids when available.</span></div></article>`
    : "";

  node.innerHTML = statusHtml + cards.join("") + errorHtml + warningHtml;
}

function hip4GroupScore(sides) {
  const first = sides[0] || {};
  let score = 0;
  if (first.underlying) score += 5;
  if (first.expiry) score += 3;
  if (first.target_price != null) score += 3;
  if (first.outcome_class && first.outcome_class !== "unknown" && first.outcome_class !== "fallback") score += 2;
  score += Math.min(Number(first.volume_24h || 0) / 1000, 3);
  const probabilities = sides
    .map((side) => Number(side.implied_probability))
    .filter((value) => !Number.isNaN(value));
  if (probabilities.some((value) => Math.abs(value - 0.5) > 0.01)) score += 1;
  return score;
}

function hip4MarketKey(row) {
  return [
    row.outcome_id ?? row.outcome_name ?? "unknown",
    row.underlying ?? "unknown",
    row.expiry ?? "no-expiry",
    row.target_price ?? "no-target",
    row.outcome_class ?? "unknown",
  ].join(":");
}
