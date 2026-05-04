# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T01:15:24.250546+00:00`
- Correlation status: `ready`
- Asset price records: `220`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1226` n `7`; crypto_alt avg `-0.1465` n `223`; crypto_major avg `-0.1328` n `7`; equity avg `0.0462` n `42`; fx avg `0.0074` n `4`; index avg `0.0602` n `9`; metal avg `-0.2336` n `7`; unknown avg `0.1587` n `314`
- 1h: commodity avg `-0.1104` n `7`; crypto_alt avg `0.3633` n `223`; crypto_major avg `0.0613` n `7`; equity avg `0.268` n `42`; fx avg `0.0133` n `4`; index avg `0.0897` n `9`; metal avg `-0.3488` n `7`; unknown avg `0.0984` n `314`
- 4h: commodity avg `0.7133` n `7`; crypto_alt avg `-0.3018` n `223`; crypto_major avg `-0.3174` n `7`; equity avg `0.0349` n `42`; fx avg `0.0011` n `4`; index avg `0.1087` n `9`; metal avg `-0.5783` n `7`; unknown avg `0.2542` n `314`
- 24h: commodity avg `0.0112` n `7`; crypto_alt avg `0.0596` n `223`; crypto_major avg `0.2627` n `7`; equity avg `0.3361` n `42`; fx avg `-0.0122` n `4`; index avg `0.206` n `9`; metal avg `0.0099` n `7`; unknown avg `0.3398` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3824`, n `216`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3665`, n `216`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3187`, n `212`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3178`, n `212`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.289`, n `216`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2784`, n `216`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2296`, n `216`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2245`, n `212`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2196`, n `212`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2176`, n `216`, weak_sample_signal
