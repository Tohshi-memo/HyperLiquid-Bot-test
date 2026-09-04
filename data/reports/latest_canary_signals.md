# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T02:37:24.091402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.039` n `12`; crypto_alt avg `0.166` n `232`; crypto_major avg `0.0246` n `8`; equity avg `0.013` n `133`; fx avg `-0.0193` n `6`; index avg `-0.0088` n `26`; metal avg `-0.0188` n `20`; unknown avg `7.6268` n `793`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.1918` n `232`; crypto_major avg `0.1203` n `8`; equity avg `0.0351` n `133`; fx avg `-0.0218` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0503` n `20`; unknown avg `7.519` n `791`
- 4h: commodity avg `0.0171` n `12`; crypto_alt avg `-0.1008` n `232`; crypto_major avg `-0.0654` n `8`; equity avg `0.3408` n `133`; fx avg `0.0082` n `6`; index avg `0.0243` n `26`; metal avg `-0.0886` n `20`; unknown avg `1.9595` n `784`
- 24h: commodity avg `-0.2` n `12`; crypto_alt avg `2.7604` n `232`; crypto_major avg `3.845` n `8`; equity avg `1.4552` n `133`; fx avg `-0.1369` n `6`; index avg `0.1942` n `26`; metal avg `0.55` n `20`; unknown avg `1.069` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
