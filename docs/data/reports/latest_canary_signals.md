# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T01:15:44.000284+00:00`
- Correlation status: `ready`
- Asset price records: `409`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0306` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1474` n `7`; crypto_alt avg `0.3953` n `223`; crypto_major avg `0.2895` n `7`; equity avg `-0.0178` n `47`; fx avg `-0.005` n `4`; index avg `0.0457` n `6`; metal avg `-0.0094` n `7`; unknown avg `0.0328` n `313`
- 1h: commodity avg `0.068` n `7`; crypto_alt avg `0.3335` n `223`; crypto_major avg `0.0731` n `7`; equity avg `-0.1448` n `47`; fx avg `-0.0759` n `4`; index avg `0.5275` n `6`; metal avg `0.471` n `7`; unknown avg `-0.0146` n `313`
- 4h: commodity avg `-0.4549` n `7`; crypto_alt avg `-0.1431` n `223`; crypto_major avg `-0.3392` n `7`; equity avg `0.5016` n `47`; fx avg `-0.1702` n `4`; index avg `0.6914` n `6`; metal avg `1.0115` n `7`; unknown avg `0.0606` n `313`
- 24h: commodity avg `-1.4806` n `7`; crypto_alt avg `2.2164` n `223`; crypto_major avg `2.0885` n `7`; equity avg `2.5468` n `47`; fx avg `-0.2016` n `4`; index avg `2.3781` n `6`; metal avg `1.3766` n `7`; unknown avg `1.5398` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1902`, n `405`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1839`, n `405`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `405`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.126`, n `405`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `405`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1023`, n `401`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.102`, n `405`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `405`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1`, n `405`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0959`, n `401`, weak_sample_signal
