# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T19:37:14.754389+00:00`
- Correlation status: `ready`
- Asset price records: `578`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1825` n `12`; crypto_alt avg `0.2338` n `228`; crypto_major avg `0.1065` n `8`; equity avg `0.0607` n `65`; fx avg `-0.0012` n `5`; index avg `0.0923` n `23`; metal avg `0.1852` n `18`; unknown avg `-0.0713` n `365`
- 1h: commodity avg `0.1854` n `12`; crypto_alt avg `-0.2578` n `228`; crypto_major avg `-0.2674` n `8`; equity avg `-0.14` n `65`; fx avg `-0.0002` n `5`; index avg `0.0604` n `23`; metal avg `-0.1308` n `18`; unknown avg `-0.4832` n `365`
- 4h: commodity avg `1.4151` n `12`; crypto_alt avg `1.0139` n `228`; crypto_major avg `-0.0774` n `8`; equity avg `-1.4625` n `65`; fx avg `0.0055` n `5`; index avg `-0.8032` n `23`; metal avg `-1.1904` n `18`; unknown avg `-0.4553` n `365`
- 24h: commodity avg `0.5676` n `12`; crypto_alt avg `1.759` n `228`; crypto_major avg `-1.6912` n `8`; equity avg `-1.3578` n `65`; fx avg `0.1872` n `5`; index avg `-0.8046` n `23`; metal avg `0.1747` n `18`; unknown avg `-0.335` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `574`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `574`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `574`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `574`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `570`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `570`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0937`, n `570`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0891`, n `570`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0866`, n `570`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0863`, n `570`, weak_sample_signal
