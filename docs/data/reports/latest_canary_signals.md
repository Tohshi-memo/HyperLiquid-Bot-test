# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T23:30:25.318106+00:00`
- Correlation status: `ready`
- Asset price records: `117`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `7`; crypto_alt avg `0.126` n `223`; crypto_major avg `0.1434` n `7`; equity avg `0.0043` n `42`; fx avg `0.0037` n `4`; index avg `0.0013` n `9`; metal avg `0.0018` n `7`; unknown avg `-0.1385` n `313`
- 1h: commodity avg `0.0675` n `7`; crypto_alt avg `0.0881` n `223`; crypto_major avg `0.1468` n `7`; equity avg `0.0332` n `42`; fx avg `-0.0037` n `4`; index avg `-0.0064` n `9`; metal avg `0.0084` n `7`; unknown avg `-0.1708` n `313`
- 4h: commodity avg `0.0523` n `7`; crypto_alt avg `0.1215` n `223`; crypto_major avg `0.1051` n `7`; equity avg `0.2218` n `42`; fx avg `0.0361` n `4`; index avg `-0.023` n `9`; metal avg `0.014` n `7`; unknown avg `-0.0087` n `313`
- 24h: commodity avg `-0.1812` n `7`; crypto_alt avg `2.4449` n `223`; crypto_major avg `0.9495` n `7`; equity avg `0.7221` n `42`; fx avg `0.0012` n `4`; index avg `0.0098` n `9`; metal avg `0.0484` n `7`; unknown avg `0.3181` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4843`, n `113`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4675`, n `113`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4544`, n `109`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4163`, n `109`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4142`, n `109`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4101`, n `109`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4054`, n `109`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `113`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.3924`, n `109`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `113`, moderate_sample_signal
