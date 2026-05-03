# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T09:30:23.022651+00:00`
- Correlation status: `ready`
- Asset price records: `157`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `7`; crypto_alt avg `0.0083` n `223`; crypto_major avg `0.0269` n `7`; equity avg `0.0563` n `42`; fx avg `0.0021` n `4`; index avg `0.0254` n `9`; metal avg `-0.0021` n `7`; unknown avg `-0.0788` n `313`
- 1h: commodity avg `0.0001` n `7`; crypto_alt avg `-0.0917` n `223`; crypto_major avg `0.1936` n `7`; equity avg `-0.0428` n `42`; fx avg `-0.001` n `4`; index avg `-0.0265` n `9`; metal avg `0.0226` n `7`; unknown avg `0.0434` n `313`
- 4h: commodity avg `-0.0669` n `7`; crypto_alt avg `0.3908` n `223`; crypto_major avg `0.2992` n `7`; equity avg `-0.1453` n `42`; fx avg `0.0191` n `4`; index avg `0.0354` n `9`; metal avg `0.1093` n `7`; unknown avg `0.0283` n `311`
- 24h: commodity avg `-0.2244` n `7`; crypto_alt avg `1.1067` n `223`; crypto_major avg `-0.0185` n `7`; equity avg `0.269` n `42`; fx avg `0.1067` n `4`; index avg `0.0284` n `9`; metal avg `0.1101` n `7`; unknown avg `0.1297` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4198`, n `153`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.405`, n `153`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `153`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3893`, n `149`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3855`, n `153`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3841`, n `149`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.376`, n `149`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3685`, n `149`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3335`, n `153`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3284`, n `153`, moderate_sample_signal
