# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T01:45:33.086500+00:00`
- Correlation status: `ready`
- Asset price records: `126`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `7`; crypto_alt avg `-0.2717` n `223`; crypto_major avg `-0.1052` n `7`; equity avg `-0.0097` n `42`; fx avg `-0.0032` n `4`; index avg `-0.0161` n `9`; metal avg `0.0045` n `7`; unknown avg `-0.0904` n `313`
- 1h: commodity avg `0.0138` n `7`; crypto_alt avg `-0.7688` n `223`; crypto_major avg `-0.423` n `7`; equity avg `-0.0093` n `42`; fx avg `-0.0024` n `4`; index avg `-0.0138` n `9`; metal avg `0.0008` n `7`; unknown avg `0.1352` n `313`
- 4h: commodity avg `0.0763` n `7`; crypto_alt avg `-1.3285` n `223`; crypto_major avg `-0.9366` n `7`; equity avg `-0.0439` n `42`; fx avg `0.0` n `4`; index avg `-0.0085` n `9`; metal avg `0.0006` n `7`; unknown avg `-0.2308` n `313`
- 24h: commodity avg `-0.1434` n `7`; crypto_alt avg `0.8065` n `223`; crypto_major avg `-0.2389` n `7`; equity avg `0.7302` n `42`; fx avg `-0.0147` n `4`; index avg `0.0506` n `9`; metal avg `0.0233` n `7`; unknown avg `0.0683` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.458`, n `122`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4423`, n `122`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4202`, n `118`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4181`, n `118`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4043`, n `118`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4039`, n `122`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3991`, n `118`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3876`, n `118`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.386`, n `122`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3732`, n `118`, moderate_sample_signal
