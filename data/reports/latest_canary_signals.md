# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T08:00:31.155557+00:00`
- Correlation status: `ready`
- Asset price records: `151`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `7`; crypto_alt avg `-0.1881` n `223`; crypto_major avg `-0.0905` n `7`; equity avg `0.0242` n `42`; fx avg `0.0` n `4`; index avg `-0.0419` n `9`; metal avg `0.0006` n `7`; unknown avg `0.0134` n `313`
- 1h: commodity avg `0.0143` n `7`; crypto_alt avg `0.067` n `223`; crypto_major avg `0.0772` n `7`; equity avg `0.0424` n `42`; fx avg `0.0111` n `4`; index avg `-0.0096` n `9`; metal avg `0.0319` n `7`; unknown avg `0.0661` n `313`
- 4h: commodity avg `-0.0711` n `7`; crypto_alt avg `0.4663` n `223`; crypto_major avg `0.1981` n `7`; equity avg `-0.187` n `42`; fx avg `0.0135` n `4`; index avg `-0.0009` n `9`; metal avg `0.0588` n `7`; unknown avg `0.3757` n `311`
- 24h: commodity avg `-0.1965` n `7`; crypto_alt avg `1.2543` n `223`; crypto_major avg `-0.0504` n `7`; equity avg `0.2444` n `42`; fx avg `0.1624` n `4`; index avg `0.0515` n `9`; metal avg `0.0748` n `7`; unknown avg `0.4002` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4249`, n `147`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4101`, n `147`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `147`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3902`, n `143`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3862`, n `147`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3852`, n `143`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3758`, n `143`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3684`, n `143`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.359`, n `147`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3553`, n `147`, moderate_sample_signal
