# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T05:30:22.374971+00:00`
- Correlation status: `ready`
- Asset price records: `426`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0694` n `7`; crypto_alt avg `0.3193` n `223`; crypto_major avg `0.1983` n `7`; equity avg `0.1556` n `47`; fx avg `0.0052` n `4`; index avg `0.0042` n `6`; metal avg `-0.0194` n `7`; unknown avg `0.1714` n `313`
- 1h: commodity avg `0.1857` n `7`; crypto_alt avg `0.1551` n `223`; crypto_major avg `0.1341` n `7`; equity avg `0.0843` n `47`; fx avg `-0.0303` n `4`; index avg `0.1027` n `6`; metal avg `-0.0549` n `7`; unknown avg `0.2725` n `313`
- 4h: commodity avg `0.0347` n `7`; crypto_alt avg `0.5235` n `223`; crypto_major avg `0.2384` n `7`; equity avg `0.8127` n `47`; fx avg `-0.1983` n `4`; index avg `0.1884` n `6`; metal avg `0.6851` n `7`; unknown avg `0.1293` n `313`
- 24h: commodity avg `-1.3387` n `7`; crypto_alt avg `2.4036` n `223`; crypto_major avg `1.6532` n `7`; equity avg `2.7276` n `47`; fx avg `-0.3697` n `4`; index avg `2.2477` n `6`; metal avg `2.1318` n `7`; unknown avg `1.0691` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1809`, n `422`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1747`, n `422`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `422`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `422`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1228`, n `422`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1102`, n `422`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `418`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0964`, n `418`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `422`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `422`, weak_sample_signal
