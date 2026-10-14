# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T13:37:34.378909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0443` n `13`; crypto_alt avg `0.9896` n `235`; crypto_major avg `0.7672` n `8`; equity avg `-0.1775` n `151`; fx avg `0.0021` n `6`; index avg `0.0364` n `26`; metal avg `0.1276` n `20`; unknown avg `11.8377` n `1136`
- 1h: commodity avg `0.0032` n `13`; crypto_alt avg `-0.2225` n `235`; crypto_major avg `-0.0343` n `8`; equity avg `-0.667` n `151`; fx avg `-0.029` n `6`; index avg `-0.0185` n `26`; metal avg `-0.1459` n `20`; unknown avg `24.1241` n `1134`
- 4h: commodity avg `-0.1181` n `13`; crypto_alt avg `-0.6859` n `235`; crypto_major avg `-0.4123` n `8`; equity avg `-1.6075` n `151`; fx avg `-0.077` n `6`; index avg `-0.2169` n `26`; metal avg `-0.3052` n `20`; unknown avg `2.8346` n `1127`
- 24h: commodity avg `0.62` n `13`; crypto_alt avg `-1.5615` n `235`; crypto_major avg `-0.7892` n `8`; equity avg `-1.3711` n `151`; fx avg `-0.1155` n `6`; index avg `-0.1894` n `26`; metal avg `-0.6984` n `20`; unknown avg `1258.9045` n `983`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1425`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.119`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0679`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
