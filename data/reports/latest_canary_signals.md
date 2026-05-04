# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T23:00:28.565111+00:00`
- Correlation status: `ready`
- Asset price records: `306`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `7`; crypto_alt avg `-0.0867` n `223`; crypto_major avg `-0.0059` n `7`; equity avg `-0.2373` n `47`; fx avg `0.004` n `4`; index avg `-0.0161` n `6`; metal avg `-0.0832` n `7`; unknown avg `-0.036` n `312`
- 1h: commodity avg `-0.0799` n `7`; crypto_alt avg `-0.5164` n `223`; crypto_major avg `-0.3868` n `7`; equity avg `-0.3582` n `47`; fx avg `0.0032` n `4`; index avg `-0.0874` n `6`; metal avg `-0.1164` n `7`; unknown avg `-0.1057` n `312`
- 4h: commodity avg `-0.2133` n `7`; crypto_alt avg `-0.302` n `223`; crypto_major avg `-0.1528` n `7`; equity avg `-0.4794` n `47`; fx avg `0.0265` n `4`; index avg `-0.1108` n `6`; metal avg `-0.0954` n `7`; unknown avg `-0.2875` n `312`
- 24h: commodity avg `1.5774` n `7`; crypto_alt avg `1.5553` n `223`; crypto_major avg `0.4595` n `7`; equity avg `-0.4966` n `47`; fx avg `-0.0177` n `4`; index avg `-0.2067` n `6`; metal avg `-2.4449` n `7`; unknown avg `-1.2529` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2359`, n `302`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.23`, n `302`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1717`, n `298`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1703`, n `298`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `302`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `302`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `302`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `302`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1204`, n `302`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.12`, n `298`, weak_sample_signal
