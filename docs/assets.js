const DATA = {
  assetFeatures: "./data/processed/asset_features_latest.json",
};

let assetRows = [];
let assetPage = 1;
const DESKTOP_ASSET_PAGE_SIZE = 50;
const MOBILE_ASSET_PAGE_SIZE = 24;

function assetPageSize() {
  return window.matchMedia("(max-width: 720px)").matches
    ? MOBILE_ASSET_PAGE_SIZE
    : DESKTOP_ASSET_PAGE_SIZE;
}

async function loadJson(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
}

function fmtNumber(value, digits = 2) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
  return Number(value).toLocaleString("en-US", {
    maximumFractionDigits: digits,
    minimumFractionDigits: Math.abs(Number(value)) < 10 ? Math.min(digits, 4) : 0,
  });
}

function fmtPct(value) {
  if (value === null || value === undefined || Number.isNaN(Number(value))) return "--";
  const number = Number(value);
  const sign = number > 0 ? "+" : "";
  return `${sign}${number.toFixed(2)}%`;
}

function formatDate(value) {
  if (!value) return "--";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleString("en-US", { month: "short", day: "2-digit", hour: "2-digit", minute: "2-digit" });
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function classForPct(value) {
  const number = Number(value);
  if (Number.isNaN(number)) return "";
  if (number > 0) return "positive";
  if (number < 0) return "negative";
  return "";
}

function valueOf(row, key) {
  if (key === "volume") return Number(row.day_ntl_vlm || 0);
  if (key === "return4h") return Number(row.returns?.["4h"] || 0);
  if (key === "return24h") return Number(row.returns?.["24h"] || 0);
  if (key === "relationship") return Number(row.best_relationship?.score || 0);
  if (key === "funding") return Math.abs(Number(row.funding || 0));
  return Number(row.activity_score || 0);
}

function collectRows(data) {
  const map = new Map();
  const addRows = (rows) => {
    if (!Array.isArray(rows)) return;
    for (const row of rows) {
      if (row && row.symbol && !map.has(row.symbol)) map.set(row.symbol, row);
    }
  };
  addRows(data?.top_assets);
  const byClass = data?.by_class || {};
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

function renderClassOptions(rows) {
  const select = document.getElementById("assetClassFilter");
  if (!select) return;
  const classes = [...new Set(rows.map((row) => row.asset_class || "unknown"))].sort();
  select.innerHTML = `<option value="all">All classes</option>` + classes
    .map((assetClass) => `<option value="${escapeHtml(assetClass)}">${escapeHtml(assetClass)}</option>`)
    .join("");
}

function renderSummary(rows) {
  const node = document.getElementById("assetSummary");
  if (!node) return;
  const byClass = new Map();
  for (const row of rows) {
    const key = row.asset_class || "unknown";
    byClass.set(key, (byClass.get(key) || 0) + 1);
  }
  const cards = [...byClass.entries()].sort((a, b) => b[1] - a[1]).map(([assetClass, count]) => `
    <div class="asset-summary-card">
      <span>${escapeHtml(assetClass)}</span>
      <strong>${fmtNumber(count, 0)}</strong>
    </div>
  `);
  node.innerHTML = cards.join("");
}

function renderRows() {
  const tbody = document.getElementById("assetTableBody");
  const badge = document.getElementById("assetCountBadge");
  if (!tbody) return;
  const query = document.getElementById("assetSearch")?.value.trim().toLowerCase() || "";
  const assetClass = document.getElementById("assetClassFilter")?.value || "all";
  const sortKey = document.getElementById("assetSort")?.value || "activity";
  const hideUnknownAux = document.getElementById("hideUnknownAux")?.checked ?? true;

  const rows = assetRows
    .filter((row) => !hideUnknownAux || !isMetadataOnlySymbol(row))
    .filter((row) => assetClass === "all" || row.asset_class === assetClass)
    .filter((row) => {
      const text = `${row.symbol} ${row.display_name || ""} ${row.asset_class || ""}`.toLowerCase();
      return !query || text.includes(query);
    })
    .sort((a, b) => valueOf(b, sortKey) - valueOf(a, sortKey));

  const pageSize = assetPageSize();
  const pageCount = Math.max(1, Math.ceil(rows.length / pageSize));
  assetPage = Math.min(Math.max(assetPage, 1), pageCount);
  const start = (assetPage - 1) * pageSize;
  const visibleRows = rows.slice(start, start + pageSize);

  if (badge) {
    badge.textContent = `${fmtNumber(rows.length, 0)} matching`;
    badge.className = "badge badge--good";
  }

  tbody.innerHTML = visibleRows.map((row) => {
    const rel = row.best_relationship || {};
    const relText = rel.pattern_id
      ? `${rel.condition || "pattern"} / ${rel.horizon || ""} / score ${fmtNumber(rel.score, 2)}`
      : "none";
    return `
      <tr>
        <td><strong>${escapeHtml(row.symbol)}</strong><small>${escapeHtml(row.display_name || "")}</small></td>
        <td>${escapeHtml(row.asset_class || "unknown")}</td>
        <td>${fmtNumber(row.price, 6)}</td>
        <td class="${classForPct(row.returns?.["15m"])}">${fmtPct(row.returns?.["15m"])}</td>
        <td class="${classForPct(row.returns?.["1h"])}">${fmtPct(row.returns?.["1h"])}</td>
        <td class="${classForPct(row.returns?.["4h"])}">${fmtPct(row.returns?.["4h"])}</td>
        <td class="${classForPct(row.returns?.["24h"])}">${fmtPct(row.returns?.["24h"])}</td>
        <td>${fmtNumber(row.day_ntl_vlm, 0)}</td>
        <td>${fmtNumber(row.open_interest, 0)}</td>
        <td>${fmtPct(Number(row.funding || 0) * 100)}</td>
        <td class="asset-relationship">${escapeHtml(relText)}</td>
      </tr>
    `;
  }).join("") || `<tr><td colspan="11">No matching assets.</td></tr>`;

  renderMobileCards(visibleRows);
  renderPagination(rows.length, pageCount);
}

function renderMobileCards(rows) {
  const node = document.getElementById("assetMobileList");
  if (!node) return;
  node.innerHTML = rows.map((row) => {
    const rel = row.best_relationship || {};
    const relationship = rel.pattern_id
      ? `${rel.condition || "relationship"} / ${rel.horizon || ""} / score ${fmtNumber(rel.score, 2)}`
      : "No relationship candidate";
    return `
      <article class="asset-mobile-card">
        <div class="asset-mobile-card__head">
          <strong>${escapeHtml(row.symbol)}</strong>
          <span>${escapeHtml(row.asset_class || "unknown")}</span>
        </div>
        <div class="asset-mobile-card__meta">
          <span>Price ${fmtNumber(row.price, 6)}</span>
          <span>Funding ${fmtPct(Number(row.funding || 0) * 100)}</span>
        </div>
        <div class="asset-mobile-card__returns">
          <span>1h<strong class="${classForPct(row.returns?.["1h"])}">${fmtPct(row.returns?.["1h"])}</strong></span>
          <span>4h<strong class="${classForPct(row.returns?.["4h"])}">${fmtPct(row.returns?.["4h"])}</strong></span>
          <span>24h<strong class="${classForPct(row.returns?.["24h"])}">${fmtPct(row.returns?.["24h"])}</strong></span>
        </div>
        <div class="asset-mobile-card__meta">
          <span>Volume ${fmtNumber(row.day_ntl_vlm, 0)}</span>
          <span>OI ${fmtNumber(row.open_interest, 0)}</span>
        </div>
        <div class="asset-mobile-card__relationship">${escapeHtml(relationship)}</div>
      </article>
    `;
  }).join("") || `<article class="asset-mobile-card">No matching assets.</article>`;
}

function renderPagination(total, pageCount) {
  const node = document.getElementById("assetPagination");
  if (!node) return;
  if (total <= assetPageSize()) {
    node.innerHTML = "";
    return;
  }
  node.innerHTML = `
    <button type="button" data-page="previous" ${assetPage <= 1 ? "disabled" : ""}>Previous</button>
    <span>Page ${assetPage} of ${pageCount}</span>
    <button type="button" data-page="next" ${assetPage >= pageCount ? "disabled" : ""}>Next</button>
  `;
  node.querySelector('[data-page="previous"]')?.addEventListener("click", () => {
    assetPage -= 1;
    renderRows();
  });
  node.querySelector('[data-page="next"]')?.addEventListener("click", () => {
    assetPage += 1;
    renderRows();
  });
}

function isMetadataOnlySymbol(row) {
  const symbol = String(row?.symbol || "");
  const assetClass = String(row?.asset_class || "unknown");
  const volume = Number(row?.day_ntl_vlm || 0);
  const openInterest = Number(row?.open_interest || 0);
  return assetClass === "unknown" && /^[@#]/.test(symbol) && volume <= 0 && openInterest <= 0;
}

async function init() {
  try {
    const data = await loadJson(DATA.assetFeatures);
    assetRows = collectRows(data);
    document.getElementById("assetUpdatedAt").textContent = formatDate(data?.observed_at || data?.generated_at);
    renderClassOptions(assetRows);
    renderSummary(assetRows);
    renderRows();
  } catch (error) {
    const badge = document.getElementById("assetCountBadge");
    if (badge) {
      badge.textContent = "data error";
      badge.className = "badge badge--risk";
    }
    document.getElementById("assetUpdatedAt").textContent = error.message;
  }
}

for (const id of ["assetSearch", "assetClassFilter", "assetSort", "hideUnknownAux"]) {
  document.getElementById(id)?.addEventListener("input", () => {
    assetPage = 1;
    renderRows();
  });
  document.getElementById(id)?.addEventListener("change", () => {
    assetPage = 1;
    renderRows();
  });
}

function setupBackToTop() {
  const button = document.querySelector(".back-to-top");
  if (!button) return;
  const update = () => button.classList.toggle("is-visible", window.scrollY > 520);
  update();
  window.addEventListener("scroll", update, { passive: true });
}

setupBackToTop();
window.addEventListener("resize", () => {
  assetPage = 1;
  renderRows();
});
init();
