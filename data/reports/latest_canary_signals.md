# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T21:30:23.865212+00:00`
- Correlation status: `ready`
- Asset price records: `300`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `7`; crypto_alt avg `0.2447` n `223`; crypto_major avg `0.1573` n `7`; equity avg `0.0524` n `47`; fx avg `0.0` n `4`; index avg `-0.0047` n `6`; metal avg `-0.0025` n `7`; unknown avg `0.0717` n `312`
- 1h: commodity avg `0.1009` n `7`; crypto_alt avg `0.4153` n `223`; crypto_major avg `0.3269` n `7`; equity avg `0.1285` n `47`; fx avg `-0.0069` n `4`; index avg `-0.0197` n `6`; metal avg `0.0871` n `7`; unknown avg `-0.0773` n `312`
- 4h: commodity avg `-0.0574` n `7`; crypto_alt avg `0.0929` n `223`; crypto_major avg `-0.2307` n `7`; equity avg `-0.3693` n `47`; fx avg `0.0002` n `4`; index avg `-0.0705` n `6`; metal avg `-0.0908` n `7`; unknown avg `-0.3482` n `312`
- 24h: commodity avg `1.9861` n `7`; crypto_alt avg `2.0235` n `223`; crypto_major avg `1.1311` n `7`; equity avg `-0.4222` n `47`; fx avg `-0.0329` n `4`; index avg `-0.141` n `6`; metal avg `-2.4771` n `7`; unknown avg `-1.08` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.236`, n `296`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2301`, n `296`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1816`, n `292`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1803`, n `292`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `296`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.149`, n `296`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1435`, n `296`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `296`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `292`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `296`, weak_sample_signal
