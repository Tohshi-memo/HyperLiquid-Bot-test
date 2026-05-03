# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T12:00:28.563529+00:00`
- Correlation status: `ready`
- Asset price records: `167`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `7`; crypto_alt avg `0.0005` n `223`; crypto_major avg `0.0503` n `7`; equity avg `0.0111` n `42`; fx avg `-0.0011` n `4`; index avg `0.0` n `9`; metal avg `0.0274` n `7`; unknown avg `0.1085` n `313`
- 1h: commodity avg `-0.0114` n `7`; crypto_alt avg `0.2787` n `223`; crypto_major avg `0.4075` n `7`; equity avg `0.022` n `42`; fx avg `-0.0024` n `4`; index avg `0.0419` n `9`; metal avg `0.0284` n `7`; unknown avg `0.538` n `313`
- 4h: commodity avg `-0.0629` n `7`; crypto_alt avg `0.3283` n `223`; crypto_major avg `0.4272` n `7`; equity avg `0.0829` n `42`; fx avg `0.0117` n `4`; index avg `0.0391` n `9`; metal avg `0.1128` n `7`; unknown avg `0.1885` n `313`
- 24h: commodity avg `-0.2339` n `7`; crypto_alt avg `1.3255` n `223`; crypto_major avg `0.4046` n `7`; equity avg `0.3368` n `42`; fx avg `0.1358` n `4`; index avg `0.0674` n `9`; metal avg `0.1546` n `7`; unknown avg `0.6859` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4043`, n `163`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `163`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.39`, n `163`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `163`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.381`, n `159`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3756`, n `159`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3624`, n `159`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3545`, n `159`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3324`, n `163`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3222`, n `163`, moderate_sample_signal
