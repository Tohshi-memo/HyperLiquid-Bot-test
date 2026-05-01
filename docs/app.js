const DATA = {
  index: "./data/processed/ai_context_index.json",
  canary: "./data/processed/canary_signals.json",
  pack: "./data/processed/ai_analysis_pack.json",
  context: "./data/processed/market_context.json",
  flow: "./data/processed/flow_alert.json",
  assetReport: "./data/reports/latest_asset_universe.md",
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
  text("updatedAt", formatDate(index?.updated_at || context?.generated_at));
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
    const [index, canary, pack, context, flow, assetReport] = await Promise.all([
      loadJson(DATA.index),
      loadJson(DATA.canary),
      loadJson(DATA.pack),
      loadJson(DATA.context),
      loadJson(DATA.flow),
      loadText(DATA.assetReport),
    ]);

    renderMetrics(index, context, flow, pack);
    renderCanary(canary);
    renderIntelligence(context, flow);
    renderNewsCategories(context);
    renderGdelt(context);
    renderFlowDetail(flow);
    renderSymbols(pack);
    renderAssetClasses(index, canary);
    renderMovers(assetReport);
  } catch (error) {
    setBadge("readinessBadge", "data error", "risk");
    text("updatedAt", error.message);
  }
}

renderDashboard();
setInterval(renderDashboard, 5 * 60 * 1000);

function renderIntelligence(context, flow) {
  renderPolymarket(context, flow);
  renderHeadlines(context);
}

function renderPolymarket(context, flow) {
  const node = document.getElementById("polymarketList");
  if (!node) return;
  const flowMarkets = Array.isArray(flow?.polymarket?.top_markets) ? flow.polymarket.top_markets : [];
  const contextMarkets = Array.isArray(context?.polymarket?.top_markets) ? context.polymarket.top_markets : [];
  const markets = flowMarkets.length ? flowMarkets : contextMarkets;
  node.innerHTML = markets.slice(0, 6).map((market) => {
    const volume24h = market.volume_24h !== undefined ? market.volume_24h : market.volume;
    const endDate = market.end_date || market.endDate;
    return `
      <article class="item-card">
        <strong>${escapeHtml(market.question || market.title || "Untitled market")}</strong>
        <div class="meta-line">
          <span>24h vol ${fmtNumber(volume24h, 0)}</span>
          <span>liquidity ${fmtNumber(market.liquidity, 0)}</span>
        </div>
        <div class="meta-line">
          <span>end ${formatDate(endDate)}</span>
          <span>${escapeHtml(market.slug || "")}</span>
        </div>
      </article>
    `;
  }).join("") || emptyCard("No active Polymarket markets.");
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

function emptyCard(message) {
  return `<article class="item-card"><strong>${escapeHtml(message)}</strong></article>`;
}
