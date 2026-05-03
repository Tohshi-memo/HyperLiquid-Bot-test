# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T13:30:23.634404+00:00`
- Correlation status: `ready`
- Asset price records: `173`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `7`; crypto_alt avg `-0.1639` n `223`; crypto_major avg `-0.1361` n `7`; equity avg `0.0155` n `42`; fx avg `0.0111` n `4`; index avg `-0.0321` n `9`; metal avg `0.0036` n `7`; unknown avg `-0.1177` n `313`
- 1h: commodity avg `-0.0257` n `7`; crypto_alt avg `-0.2399` n `223`; crypto_major avg `-0.1373` n `7`; equity avg `-0.0257` n `42`; fx avg `0.0111` n `4`; index avg `-0.0082` n `9`; metal avg `0.0072` n `7`; unknown avg `-0.1192` n `313`
- 4h: commodity avg `-0.0969` n `7`; crypto_alt avg `0.1569` n `223`; crypto_major avg `0.2094` n `7`; equity avg `0.1625` n `42`; fx avg `0.0218` n `4`; index avg `0.0147` n `9`; metal avg `0.0729` n `7`; unknown avg `-0.1268` n `313`
- 24h: commodity avg `-0.2643` n `7`; crypto_alt avg `0.9944` n `223`; crypto_major avg `0.1731` n `7`; equity avg `0.3404` n `42`; fx avg `0.1717` n `4`; index avg `0.0218` n `9`; metal avg `0.1641` n `7`; unknown avg `0.1398` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `169`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3855`, n `169`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `169`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3769`, n `165`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3716`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3708`, n `165`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3597`, n `165`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3511`, n `165`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3246`, n `169`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.312`, n `169`, moderate_sample_signal
