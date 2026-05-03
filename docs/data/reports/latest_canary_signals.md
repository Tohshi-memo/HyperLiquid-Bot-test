# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T01:00:25.583428+00:00`
- Correlation status: `ready`
- Asset price records: `123`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `7`; crypto_alt avg `-0.0833` n `223`; crypto_major avg `-0.0778` n `7`; equity avg `0.0192` n `42`; fx avg `0.0008` n `4`; index avg `0.0028` n `9`; metal avg `-0.0043` n `7`; unknown avg `-0.0081` n `313`
- 1h: commodity avg `0.0037` n `7`; crypto_alt avg `-0.2521` n `223`; crypto_major avg `-0.2384` n `7`; equity avg `0.0018` n `42`; fx avg `-0.0043` n `4`; index avg `0.0251` n `9`; metal avg `-0.0316` n `7`; unknown avg `-0.2674` n `313`
- 4h: commodity avg `0.054` n `7`; crypto_alt avg `-0.2888` n `223`; crypto_major avg `-0.3154` n `7`; equity avg `-0.0229` n `42`; fx avg `0.0207` n `4`; index avg `-0.0017` n `9`; metal avg `0.0015` n `7`; unknown avg `-0.199` n `313`
- 24h: commodity avg `-0.1955` n `7`; crypto_alt avg `1.6268` n `223`; crypto_major avg `0.1888` n `7`; equity avg `0.784` n `42`; fx avg `-0.0137` n `4`; index avg `0.0897` n `9`; metal avg `0.0261` n `7`; unknown avg `0.3054` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4741`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4577`, n `119`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4199`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4175`, n `115`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4055`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4036`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4007`, n `115`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3858`, n `119`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3854`, n `115`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.3774`, n `115`, moderate_sample_signal
