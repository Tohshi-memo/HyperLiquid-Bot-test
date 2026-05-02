# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T21:15:32.073896+00:00`
- Correlation status: `ready`
- Asset price records: `108`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `7`; crypto_alt avg `-0.0729` n `223`; crypto_major avg `-0.0951` n `7`; equity avg `0.0087` n `42`; fx avg `0.0072` n `4`; index avg `0.0065` n `9`; metal avg `-0.0001` n `7`; unknown avg `0.014` n `313`
- 1h: commodity avg `0.0595` n `7`; crypto_alt avg `-0.0693` n `223`; crypto_major avg `0.011` n `7`; equity avg `0.1905` n `42`; fx avg `0.0183` n `4`; index avg `0.0176` n `9`; metal avg `0.0023` n `7`; unknown avg `0.1242` n `313`
- 4h: commodity avg `-0.1083` n `7`; crypto_alt avg `0.1733` n `223`; crypto_major avg `-0.021` n `7`; equity avg `0.5622` n `42`; fx avg `0.0236` n `4`; index avg `0.0586` n `9`; metal avg `-0.0523` n `7`; unknown avg `0.1381` n `313`
- 24h: commodity avg `-0.0036` n `7`; crypto_alt avg `1.5472` n `223`; crypto_major avg `0.2015` n `7`; equity avg `1.1491` n `42`; fx avg `-0.0018` n `4`; index avg `0.0787` n `9`; metal avg `-0.1003` n `7`; unknown avg `0.3143` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5349`, n `100`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5342`, n `100`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5071`, n `104`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4895`, n `104`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4612`, n `100`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4239`, n `100`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4209`, n `100`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4198`, n `100`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4184`, n `100`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.418`, n `104`, moderate_sample_signal
