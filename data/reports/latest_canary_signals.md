# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T20:30:28.389220+00:00`
- Correlation status: `ready`
- Asset price records: `296`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `7`; crypto_alt avg `-0.1777` n `223`; crypto_major avg `-0.1603` n `7`; equity avg `-0.0241` n `47`; fx avg `0.0058` n `4`; index avg `0.0062` n `6`; metal avg `0.0309` n `7`; unknown avg `-0.0107` n `312`
- 1h: commodity avg `-0.0924` n `7`; crypto_alt avg `-0.221` n `223`; crypto_major avg `-0.1087` n `7`; equity avg `-0.329` n `47`; fx avg `0.0116` n `4`; index avg `0.0891` n `6`; metal avg `-0.1365` n `7`; unknown avg `-0.127` n `312`
- 4h: commodity avg `-0.343` n `7`; crypto_alt avg `0.1509` n `223`; crypto_major avg `-0.142` n `7`; equity avg `-0.3715` n `47`; fx avg `0.0086` n `4`; index avg `-0.0254` n `6`; metal avg `0.073` n `7`; unknown avg `-0.2757` n `312`
- 24h: commodity avg `1.4348` n `7`; crypto_alt avg `1.3131` n `223`; crypto_major avg `0.6461` n `7`; equity avg `-0.4031` n `47`; fx avg `-0.0713` n `4`; index avg `-0.06` n `6`; metal avg `-2.3906` n `7`; unknown avg `-1.1279` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2366`, n `292`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2309`, n `292`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1842`, n `288`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1826`, n `288`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `292`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `292`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1438`, n `292`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `292`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `288`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1207`, n `292`, weak_sample_signal
