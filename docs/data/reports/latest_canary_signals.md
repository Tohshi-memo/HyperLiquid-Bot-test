# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T09:22:31.528352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1077` n `12`; crypto_alt avg `0.1282` n `231`; crypto_major avg `0.1012` n `8`; equity avg `-0.1094` n `122`; fx avg `-0.0034` n `6`; index avg `-0.0146` n `25`; metal avg `-0.0224` n `20`; unknown avg `0.0522` n `793`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.6763` n `231`; crypto_major avg `0.6251` n `8`; equity avg `0.0557` n `122`; fx avg `-0.0314` n `6`; index avg `0.0114` n `25`; metal avg `-0.0299` n `20`; unknown avg `0.7199` n `793`
- 4h: commodity avg `0.1257` n `12`; crypto_alt avg `-0.1152` n `231`; crypto_major avg `-0.212` n `8`; equity avg `-0.1496` n `122`; fx avg `0.0312` n `6`; index avg `-0.0378` n `25`; metal avg `-0.0137` n `20`; unknown avg `0.3215` n `777`
- 24h: commodity avg `-0.1849` n `12`; crypto_alt avg `2.1138` n `231`; crypto_major avg `0.6226` n `8`; equity avg `-1.274` n `122`; fx avg `-0.1468` n `6`; index avg `-0.113` n `25`; metal avg `0.1071` n `20`; unknown avg `5.4274` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
