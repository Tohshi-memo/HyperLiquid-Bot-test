# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T22:15:35.516821+00:00`
- Correlation status: `ready`
- Asset price records: `397`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `7`; crypto_alt avg `-0.0078` n `223`; crypto_major avg `-0.0534` n `7`; equity avg `-0.0424` n `47`; fx avg `-0.0027` n `4`; index avg `-0.0104` n `6`; metal avg `-0.0249` n `7`; unknown avg `0.0231` n `313`
- 1h: commodity avg `-0.0814` n `7`; crypto_alt avg `-0.2816` n `223`; crypto_major avg `0.0298` n `7`; equity avg `0.1013` n `47`; fx avg `0.1083` n `4`; index avg `-0.0094` n `6`; metal avg `-0.1482` n `7`; unknown avg `1.0195` n `313`
- 4h: commodity avg `-0.0255` n `7`; crypto_alt avg `0.9632` n `223`; crypto_major avg `0.4244` n `7`; equity avg `0.3697` n `47`; fx avg `0.1153` n `4`; index avg `0.1178` n `6`; metal avg `-0.3302` n `7`; unknown avg `0.0862` n `313`
- 24h: commodity avg `-1.1249` n `7`; crypto_alt avg `2.1658` n `223`; crypto_major avg `2.4627` n `7`; equity avg `2.2317` n `47`; fx avg `0.0671` n `4`; index avg `1.6688` n `6`; metal avg `0.5717` n `7`; unknown avg `2.3385` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2066`, n `393`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1998`, n `393`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `393`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `393`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `393`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `389`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.107`, n `393`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `389`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `393`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `393`, weak_sample_signal
