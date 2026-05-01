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
