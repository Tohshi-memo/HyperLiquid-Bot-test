# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T22:15:21.551826+00:00`
- Correlation status: `ready`
- Asset price records: `303`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0841` n `7`; crypto_alt avg `-0.0092` n `223`; crypto_major avg `0.0874` n `7`; equity avg `0.0526` n `47`; fx avg `0.0002` n `4`; index avg `-0.0283` n `6`; metal avg `0.0138` n `7`; unknown avg `-0.003` n `312`
- 1h: commodity avg `-0.0874` n `7`; crypto_alt avg `0.4956` n `223`; crypto_major avg `0.492` n `7`; equity avg `0.2382` n `47`; fx avg `0.001` n `4`; index avg `-0.119` n `6`; metal avg `-0.0294` n `7`; unknown avg `0.1687` n `312`
- 4h: commodity avg `-0.1287` n `7`; crypto_alt avg `0.2231` n `223`; crypto_major avg `0.1366` n `7`; equity avg `-0.0483` n `47`; fx avg `-0.0003` n `4`; index avg `-0.1492` n `6`; metal avg `-0.0166` n `7`; unknown avg `-0.3186` n `312`
- 24h: commodity avg `1.6151` n `7`; crypto_alt avg `1.9012` n `223`; crypto_major avg `0.9825` n `7`; equity avg `-0.2017` n `47`; fx avg `-0.0217` n `4`; index avg `-0.1794` n `6`; metal avg `-2.2732` n `7`; unknown avg `-1.2717` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2357`, n `299`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2298`, n `299`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1671`, n `295`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1659`, n `295`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `299`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `299`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1404`, n `299`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `299`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.12`, n `295`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1197`, n `299`, weak_sample_signal
