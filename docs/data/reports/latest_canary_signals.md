# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T17:17:50.613589+00:00`
- Correlation status: `ready`
- Asset price records: `473`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `6.18` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.4017` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1609` n `12`; crypto_alt avg `-0.4505` n `228`; crypto_major avg `-0.2886` n `8`; equity avg `-0.0586` n `65`; fx avg `0.0031` n `4`; index avg `0.0211` n `23`; metal avg `-0.0773` n `18`; unknown avg `-0.1363` n `356`
- 1h: commodity avg `0.2942` n `12`; crypto_alt avg `-0.1074` n `228`; crypto_major avg `-0.1424` n `8`; equity avg `0.0545` n `65`; fx avg `-0.0158` n `4`; index avg `0.0887` n `23`; metal avg `-0.1911` n `18`; unknown avg `-0.4083` n `356`
- 4h: commodity avg `-0.2854` n `12`; crypto_alt avg `-0.37` n `228`; crypto_major avg `-0.9206` n `8`; equity avg `0.5137` n `65`; fx avg `-0.0271` n `4`; index avg `0.4811` n `23`; metal avg `0.3051` n `18`; unknown avg `0.4688` n `356`
- 24h: commodity avg `-2.3555` n `7`; crypto_alt avg `2.8474` n `223`; crypto_major avg `0.9187` n `7`; equity avg `2.3476` n `47`; fx avg `-0.4568` n `4`; index avg `1.9354` n `6`; metal avg `3.0211` n `7`; unknown avg `4.0557` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `469`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1407`, n `465`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `469`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1237`, n `465`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `469`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1102`, n `465`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `469`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0957`, n `465`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `469`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `465`, weak_sample_signal
