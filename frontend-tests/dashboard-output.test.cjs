// Offline frontend-only regression tests. Run: node --test frontend-tests/*.test.cjs
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { test } = require('node:test');

const source = readFileSync(path.join(__dirname, '../docs/app.js'), 'utf8');
// Suppress only the three browser startup statements. No collector, API, timers,
// credentials, or network are used; render functions receive synthetic fixtures.
const startup = [
  'renderDashboard();',
  'setInterval(renderDashboard, 5 * 60 * 1000);',
  'setupBackToTop();',
];
let offlineSource = source;
for (const statement of startup) {
  assert.equal(offlineSource.split(`\n${statement}\n`).length, 2, `startup changed: ${statement}`);
  offlineSource = offlineSource.replace(`\n${statement}\n`, '\n');
}
function dashboard() {
  const nodes = new Map();
  const getNode = (id) => {
    if (!nodes.has(id)) nodes.set(id, { innerHTML: '', textContent: '', value: '', addEventListener() {} });
    return nodes.get(id);
  };
  const context = vm.createContext({
    URL,
    document: { getElementById: getNode },
    fetch() { throw new Error('Network must never be used in frontend tests'); },
    setInterval() { throw new Error('Timers must never be used in frontend tests'); },
  });
  vm.runInContext(offlineSource, context);
  return { app: context, html: (id) => getNode(id).innerHTML };
}
const payload = '<img src=x onerror="alert(1)">';
const escapedPayload = '&lt;img src=x onerror=&quot;alert(1)&quot;&gt;';

test('invalid and missing dates use a fixed placeholder; valid date formatting is unchanged', () => {
  const { app } = dashboard();
  for (const value of [undefined, null, '', 'not a date', payload, {}]) {
    assert.equal(app.formatDate(value), '--');
  }
  for (const value of ['2026-10-06T12:34:56Z', '2026-10-06', '2026-10-06T23:59:00+09:00']) {
    assert.equal(app.formatDate(value), new Date(value).toLocaleString('en-US', {
      month: 'short', day: '2-digit', hour: '2-digit', minute: '2-digit',
    }));
  }
});

test('market and health market date injection is rejected and titles are escaped once', () => {
  const { app, html } = dashboard();
  const market = { question: `pandemic ${payload} & news`, slug: 'health-fixture', end_date: payload };
  const context = { polymarket: { top_markets: [market], health_markets: [market] } };
  app.renderPolymarket(context, {});
  app.renderHealthPolymarket(context, {});
  for (const id of ['polymarketList', 'healthPolymarketList']) {
    assert.ok(html(id).includes('<span>end --</span>'));
    assert.ok(html(id).includes(`pandemic ${escapedPayload} &amp; news`));
    assert.ok(!html(id).includes('<img'));
    assert.ok(!html(id).includes('&amp;lt;'));
    assert.ok(html(id).includes('https://polymarket.com/event/health-fixture'));
  }
});

test('remaining date sinks reject external HTML: people, headlines, macro releases and sectors', () => {
  const { app, html } = dashboard();
  app.renderPolymarketPeople([{ person_name: 'Example', probability: 0.5, observed_at: payload }]);
  app.renderHeadlines({ news: { top_headlines: [{ title: 'Example', published_at: payload }] } });
  app.renderMacroIndicators({ release_calendar: [{ name: 'Example', scheduled_for: payload }] });
  app.renderSectorReactions({ sector_snapshot: [{ proxy: 'Example', date: payload }] });
  for (const id of ['polymarketPeopleList', 'headlinesList', 'macroIndicatorList', 'sectorReactionList']) {
    assert.ok(!html(id).includes('<img'), id);
    assert.match(html(id), /<(?:span|strong)>--<\/(?:span|strong)>/, id);
  }
});

test('RSS URL parser allows absolute HTTP(S) only', () => {
  const { app } = dashboard();
  for (const value of ['https://example.com/news?a=1&b=2', 'http://example.com/news', 'HTTPS://EXAMPLE.COM/news', ' https://example.com/news ']) {
    assert.equal(app.safeHeadlineUrl(value), new URL(value).href);
  }
  for (const value of [undefined, null, 123, {}, '', '/news', '../news', '//example.com/news', 'news', 'https://',
    'javascript:alert(1)', 'JaVaScRiPt:alert(1)', 'java\nscript:alert(1)', ' javascript:alert(1)',
    'data:text/html,<script>alert(1)</script>', 'vbscript:msgbox(1)', 'file:///tmp/news',
    'mailto:reader@example.com', 'ftp://example.com/news', 'javascript&#58;alert(1)']) {
    assert.equal(app.safeHeadlineUrl(value), null, String(value));
  }
});

test('unsafe RSS URLs retain escaped headline text without an anchor', () => {
  const { app, html } = dashboard();
  for (const url of ['javascript:alert(1)', 'data:text/html,test', '//example.com', '/news', undefined]) {
    app.renderHeadlines({ news: { top_headlines: [{ title: `${payload} & news`, url, published_at: payload }] } });
    const output = html('headlinesList');
    assert.ok(!output.includes('<a '));
    assert.ok(!output.includes('<img'));
    assert.ok(output.includes(`${escapedPayload} &amp; news`));
    assert.ok(!output.includes('&amp;lt;'));
  }
});

test('valid RSS links preserve destination and escape attributes exactly once', () => {
  const { app, html } = dashboard();
  const url = 'https://example.com/news?q="quoted"&second=one';
  app.renderHeadlines({ news: { top_headlines: [{ title: 'A & B', url, published_at: '2026-10-06T12:00:00Z' }] } });
  const output = html('headlinesList');
  assert.ok(output.includes(`href="${app.escapeHtml(new URL(url).href)}"`));
  assert.ok(output.includes('target="_blank" rel="noopener noreferrer">A &amp; B</a>'));
  assert.ok(!output.includes('&amp;amp;'));
  assert.ok(output.includes(app.formatDate('2026-10-06T12:00:00Z')));
});

test('date HTML sinks escape formatter output, while the formatter stays plain text', () => {
  const { app, html } = dashboard();
  // Defense in depth: all template sinks still escape if the formatter changes.
  app.formatDate = () => payload;
  app.renderPolymarket({ polymarket: { top_markets: [{ question: 'Example', end_date: 'valid' }] } }, {});
  app.renderHealthPolymarket({ polymarket: { health_markets: [{ question: 'pandemic', end_date: 'valid' }] } }, {});
  app.renderPolymarketPeople([{ person_name: 'Example', probability: 0.5, observed_at: 'valid' }]);
  app.renderHeadlines({ news: { top_headlines: [{ title: 'Example', published_at: 'valid' }] } });
  app.renderMacroIndicators({ release_calendar: [{ name: 'Example', scheduled_utc: 'valid' }] });
  app.renderSectorReactions({ sector_snapshot: [{ proxy: 'Example', date: 'valid' }] });
  for (const id of ['polymarketList', 'healthPolymarketList', 'polymarketPeopleList', 'headlinesList', 'macroIndicatorList', 'sectorReactionList']) {
    assert.ok(html(id).includes(escapedPayload), id);
    assert.ok(!html(id).includes('<img'), id);
    assert.ok(!html(id).includes('&amp;lt;'), id);
  }
});
