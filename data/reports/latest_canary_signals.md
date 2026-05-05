# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T04:00:35.176593+00:00`
- Correlation status: `ready`
- Asset price records: `326`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `7`; crypto_alt avg `-0.0346` n `223`; crypto_major avg `-0.0723` n `7`; equity avg `-0.0218` n `47`; fx avg `-0.0` n `4`; index avg `0.0071` n `6`; metal avg `-0.0588` n `7`; unknown avg `0.0259` n `312`
- 1h: commodity avg `0.1377` n `7`; crypto_alt avg `0.1197` n `223`; crypto_major avg `0.4423` n `7`; equity avg `-0.0287` n `47`; fx avg `0.0005` n `4`; index avg `0.0774` n `6`; metal avg `-0.2004` n `7`; unknown avg `-0.0849` n `312`
- 4h: commodity avg `-0.1702` n `7`; crypto_alt avg `0.8468` n `223`; crypto_major avg `1.1838` n `7`; equity avg `0.6207` n `47`; fx avg `-0.011` n `4`; index avg `0.1832` n `6`; metal avg `0.3702` n `7`; unknown avg `0.2508` n `312`
- 24h: commodity avg `1.2092` n `7`; crypto_alt avg `0.4929` n `223`; crypto_major avg `-0.2287` n `7`; equity avg `-1.0291` n `47`; fx avg `-0.0057` n `4`; index avg `-0.2108` n `6`; metal avg `-1.9318` n `7`; unknown avg `-1.4961` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2268`, n `322`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2204`, n `322`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1523`, n `322`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1411`, n `318`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `322`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1384`, n `318`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `322`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `322`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `322`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1213`, n `318`, weak_sample_signal
