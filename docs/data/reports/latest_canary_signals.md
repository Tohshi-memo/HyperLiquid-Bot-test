# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T13:00:30.303931+00:00`
- Correlation status: `ready`
- Asset price records: `171`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `7`; crypto_alt avg `-0.1479` n `223`; crypto_major avg `-0.0771` n `7`; equity avg `0.019` n `42`; fx avg `0.0` n `4`; index avg `-0.0232` n `9`; metal avg `0.0083` n `7`; unknown avg `-0.0814` n `313`
- 1h: commodity avg `-0.0347` n `7`; crypto_alt avg `0.0798` n `223`; crypto_major avg `0.0603` n `7`; equity avg `0.0542` n `42`; fx avg `0.0032` n `4`; index avg `0.0178` n `9`; metal avg `0.0232` n `7`; unknown avg `-0.3506` n `313`
- 4h: commodity avg `-0.1116` n `7`; crypto_alt avg `0.2195` n `223`; crypto_major avg `0.3958` n `7`; equity avg `0.278` n `42`; fx avg `0.0085` n `4`; index avg `0.0626` n `9`; metal avg `0.09` n `7`; unknown avg `-0.1513` n `313`
- 24h: commodity avg `-0.2674` n `7`; crypto_alt avg `1.257` n `223`; crypto_major avg `0.3939` n `7`; equity avg `0.4035` n `42`; fx avg `0.1457` n `4`; index avg `0.0553` n `9`; metal avg `0.1575` n `7`; unknown avg `0.1681` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `167`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3856`, n `167`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `167`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3776`, n `163`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3717`, n `167`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3717`, n `163`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3617`, n `163`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3536`, n `163`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3268`, n `167`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3173`, n `167`, moderate_sample_signal
