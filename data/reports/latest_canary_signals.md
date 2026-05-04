# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T21:15:17.755710+00:00`
- Correlation status: `ready`
- Asset price records: `299`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0243` n `7`; crypto_alt avg `0.3184` n `223`; crypto_major avg `0.2455` n `7`; equity avg `-0.0176` n `47`; fx avg `-0.0056` n `4`; index avg `-0.0341` n `6`; metal avg `0.0407` n `7`; unknown avg `-0.0315` n `312`
- 1h: commodity avg `0.0896` n `7`; crypto_alt avg `-0.014` n `223`; crypto_major avg `0.011` n `7`; equity avg `0.0356` n `47`; fx avg `-0.0011` n `4`; index avg `0.0019` n `6`; metal avg `0.1157` n `7`; unknown avg `-0.051` n `312`
- 4h: commodity avg `-0.2329` n `7`; crypto_alt avg `-0.0119` n `223`; crypto_major avg `-0.3412` n `7`; equity avg `-0.2584` n `47`; fx avg `0.0035` n `4`; index avg `0.0136` n `6`; metal avg `-0.0743` n `7`; unknown avg `-0.3033` n `312`
- 24h: commodity avg `2.1741` n `7`; crypto_alt avg `1.6169` n `223`; crypto_major avg `0.9121` n `7`; equity avg `-0.471` n `47`; fx avg `-0.0316` n `4`; index avg `-0.1282` n `6`; metal avg `-2.4664` n `7`; unknown avg `-1.1008` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2363`, n `295`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2305`, n `295`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1857`, n `291`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1841`, n `291`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `295`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `295`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.144`, n `295`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `295`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `291`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1205`, n `295`, weak_sample_signal
