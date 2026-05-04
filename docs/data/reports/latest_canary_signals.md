# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T22:45:24.484807+00:00`
- Correlation status: `ready`
- Asset price records: `305`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `7`; crypto_alt avg `-0.2127` n `223`; crypto_major avg `-0.1859` n `7`; equity avg `-0.1157` n `47`; fx avg `-0.0008` n `4`; index avg `-0.0181` n `6`; metal avg `-0.0491` n `7`; unknown avg `-0.0404` n `312`
- 1h: commodity avg `-0.0294` n `7`; crypto_alt avg `-0.2188` n `223`; crypto_major avg `-0.2017` n `7`; equity avg `0.0079` n `47`; fx avg `0.0037` n `4`; index avg `-0.0391` n `6`; metal avg `-0.0882` n `7`; unknown avg `0.158` n `312`
- 4h: commodity avg `-0.2795` n `7`; crypto_alt avg `-0.1796` n `223`; crypto_major avg `-0.088` n `7`; equity avg `-0.137` n `47`; fx avg `0.0029` n `4`; index avg `-0.0925` n `6`; metal avg `0.0754` n `7`; unknown avg `-0.3047` n `312`
- 24h: commodity avg `1.7073` n `7`; crypto_alt avg `1.4284` n `223`; crypto_major avg `0.3246` n `7`; equity avg `-0.4093` n `47`; fx avg `-0.0257` n `4`; index avg `-0.2147` n `6`; metal avg `-2.5103` n `7`; unknown avg `-1.3452` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2358`, n `301`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2299`, n `301`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1644`, n `297`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1633`, n `297`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `301`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `301`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1411`, n `301`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `301`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.12`, n `301`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `297`, weak_sample_signal
