# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T21:17:54.210091+00:00`
- Correlation status: `ready`
- Asset price records: `299`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `7`; crypto_alt avg `0.3224` n `223`; crypto_major avg `0.2431` n `7`; equity avg `-0.0034` n `47`; fx avg `-0.0056` n `4`; index avg `-0.0449` n `6`; metal avg `0.0456` n `7`; unknown avg `-0.1396` n `312`
- 1h: commodity avg `0.088` n `7`; crypto_alt avg `-0.0097` n `223`; crypto_major avg `0.0087` n `7`; equity avg `0.0496` n `47`; fx avg `-0.0011` n `4`; index avg `-0.0088` n `6`; metal avg `0.1205` n `7`; unknown avg `-0.1593` n `312`
- 4h: commodity avg `-0.2344` n `7`; crypto_alt avg `-0.0085` n `223`; crypto_major avg `-0.3434` n `7`; equity avg `-0.245` n `47`; fx avg `0.0035` n `4`; index avg `0.0029` n `6`; metal avg `-0.0695` n `7`; unknown avg `-0.4119` n `312`
- 24h: commodity avg `2.1727` n `7`; crypto_alt avg `1.6314` n `223`; crypto_major avg `0.9098` n `7`; equity avg `-0.4587` n `47`; fx avg `-0.0316` n `4`; index avg `-0.1389` n `6`; metal avg `-2.4617` n `7`; unknown avg `-1.2097` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2363`, n `295`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2304`, n `295`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1854`, n `291`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1838`, n `291`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `295`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `295`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.144`, n `295`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `295`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `291`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1205`, n `295`, weak_sample_signal
