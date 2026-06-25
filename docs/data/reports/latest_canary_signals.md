# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T04:52:28.916398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.4159` n `228`; crypto_major avg `0.5671` n `8`; equity avg `0.1818` n `86`; fx avg `-0.014` n `6`; index avg `0.0354` n `23`; metal avg `0.04` n `20`; unknown avg `2.0483` n `765`
- 1h: commodity avg `0.0434` n `12`; crypto_alt avg `0.2849` n `228`; crypto_major avg `0.4993` n `8`; equity avg `0.2196` n `86`; fx avg `-0.0055` n `6`; index avg `0.0421` n `23`; metal avg `0.0134` n `20`; unknown avg `1.6631` n `765`
- 4h: commodity avg `-0.1211` n `12`; crypto_alt avg `0.2619` n `228`; crypto_major avg `0.2635` n `8`; equity avg `0.2499` n `86`; fx avg `0.0116` n `6`; index avg `0.1521` n `23`; metal avg `0.0373` n `20`; unknown avg `1.7825` n `748`
- 24h: commodity avg `-0.4528` n `12`; crypto_alt avg `-1.5976` n `228`; crypto_major avg `-1.4269` n `8`; equity avg `0.1841` n `86`; fx avg `0.0593` n `6`; index avg `0.6254` n `23`; metal avg `-1.3248` n `20`; unknown avg `-0.4696` n `708`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
