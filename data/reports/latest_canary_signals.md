# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T12:30:39.012418+00:00`
- Correlation status: `ready`
- Asset price records: `169`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `7`; crypto_alt avg `-0.0063` n `223`; crypto_major avg `-0.0473` n `7`; equity avg `0.0442` n `42`; fx avg `-0.0005` n `4`; index avg `-0.0018` n `9`; metal avg `0.0225` n `7`; unknown avg `0.1055` n `313`
- 1h: commodity avg `0.0147` n `7`; crypto_alt avg `0.3778` n `223`; crypto_major avg `0.4417` n `7`; equity avg `0.0619` n `42`; fx avg `-0.0045` n `4`; index avg `-0.0296` n `9`; metal avg `0.0221` n `7`; unknown avg `0.203` n `313`
- 4h: commodity avg `-0.0712` n `7`; crypto_alt avg `0.2986` n `223`; crypto_major avg `0.5408` n `7`; equity avg `0.1455` n `42`; fx avg `0.0096` n `4`; index avg `-0.0036` n `9`; metal avg `0.0883` n `7`; unknown avg `0.0391` n `313`
- 24h: commodity avg `-0.2431` n `7`; crypto_alt avg `1.2471` n `223`; crypto_major avg `0.3844` n `7`; equity avg `0.4192` n `42`; fx avg `0.1524` n `4`; index avg `0.0376` n `9`; metal avg `0.1681` n `7`; unknown avg `0.1697` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `165`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3875`, n `165`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `165`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3796`, n `161`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.374`, n `161`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3736`, n `165`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3625`, n `161`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3547`, n `161`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3268`, n `165`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.316`, n `165`, moderate_sample_signal
