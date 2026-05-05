# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T01:00:28.696749+00:00`
- Correlation status: `ready`
- Asset price records: `314`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `7`; crypto_alt avg `0.0987` n `223`; crypto_major avg `0.0813` n `7`; equity avg `0.0232` n `47`; fx avg `0.0` n `4`; index avg `0.0324` n `6`; metal avg `0.0747` n `7`; unknown avg `0.0082` n `312`
- 1h: commodity avg `-0.0312` n `7`; crypto_alt avg `0.2491` n `223`; crypto_major avg `0.3904` n `7`; equity avg `0.3615` n `47`; fx avg `-0.0059` n `4`; index avg `0.0311` n `6`; metal avg `0.2123` n `7`; unknown avg `-0.0097` n `312`
- 4h: commodity avg `-0.0869` n `7`; crypto_alt avg `0.435` n `223`; crypto_major avg `0.3616` n `7`; equity avg `0.1234` n `47`; fx avg `-0.0094` n `4`; index avg `-0.1872` n `6`; metal avg `0.1744` n `7`; unknown avg `-0.1219` n `312`
- 24h: commodity avg `1.4486` n `7`; crypto_alt avg `1.8818` n `223`; crypto_major avg `1.2162` n `7`; equity avg `-0.3756` n `47`; fx avg `-0.0292` n `4`; index avg `-0.0706` n `6`; metal avg `-1.9996` n `7`; unknown avg `-1.2331` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2341`, n `310`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2281`, n `310`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1678`, n `306`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1654`, n `306`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1504`, n `310`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `310`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1409`, n `310`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `310`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `306`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1194`, n `310`, weak_sample_signal
