# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T20:28:19.667618+00:00`
- Correlation status: `ready`
- Asset price records: `200`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `7`; crypto_alt avg `0.2037` n `223`; crypto_major avg `0.0644` n `7`; equity avg `-0.0132` n `42`; fx avg `0.0263` n `4`; index avg `0.0069` n `9`; metal avg `-0.0636` n `7`; unknown avg `0.0048` n `314`
- 1h: commodity avg `-0.0158` n `7`; crypto_alt avg `0.2738` n `223`; crypto_major avg `0.212` n `7`; equity avg `0.005` n `42`; fx avg `0.041` n `4`; index avg `0.0184` n `9`; metal avg `-0.0203` n `7`; unknown avg `-0.0222` n `314`
- 4h: commodity avg `0.4229` n `7`; crypto_alt avg `0.6248` n `223`; crypto_major avg `0.3575` n `7`; equity avg `0.1303` n `42`; fx avg `0.0022` n `4`; index avg `0.0218` n `9`; metal avg `0.097` n `7`; unknown avg `0.1634` n `313`
- 24h: commodity avg `-0.011` n `7`; crypto_alt avg `0.0169` n `223`; crypto_major avg `0.3008` n `7`; equity avg `0.2917` n `42`; fx avg `0.0804` n `4`; index avg `0.0671` n `9`; metal avg `0.4423` n `7`; unknown avg `0.0725` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3988`, n `196`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.381`, n `196`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3799`, n `192`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3727`, n `192`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3699`, n `196`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.357`, n `196`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3348`, n `196`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3166`, n `196`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3056`, n `196`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2515`, n `192`, moderate_sample_signal
