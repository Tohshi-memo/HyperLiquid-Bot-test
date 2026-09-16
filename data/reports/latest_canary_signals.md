# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T23:52:25.363845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `12`; crypto_alt avg `0.3124` n `234`; crypto_major avg `0.2366` n `8`; equity avg `0.1979` n `137`; fx avg `-0.0004` n `6`; index avg `0.0941` n `27`; metal avg `0.0581` n `20`; unknown avg `2.2081` n `917`
- 1h: commodity avg `-0.0439` n `12`; crypto_alt avg `1.3802` n `234`; crypto_major avg `0.984` n `8`; equity avg `0.469` n `137`; fx avg `-0.0095` n `6`; index avg `0.1186` n `27`; metal avg `0.0933` n `20`; unknown avg `0.8498` n `907`
- 4h: commodity avg `0.0203` n `12`; crypto_alt avg `1.6285` n `234`; crypto_major avg `0.3167` n `8`; equity avg `1.1074` n `137`; fx avg `0.0055` n `6`; index avg `0.2213` n `27`; metal avg `0.1301` n `20`; unknown avg `0.6715` n `779`
- 24h: commodity avg `-0.6639` n `12`; crypto_alt avg `1.2952` n `234`; crypto_major avg `1.1894` n `8`; equity avg `1.6712` n `137`; fx avg `0.0346` n `6`; index avg `0.1923` n `27`; metal avg `-0.1596` n `20`; unknown avg `-0.1291` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
