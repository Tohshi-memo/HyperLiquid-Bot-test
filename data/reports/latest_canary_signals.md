# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T17:56:32.655639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.0357` n `229`; crypto_major avg `-0.1228` n `8`; equity avg `0.0138` n `88`; fx avg `-0.0002` n `6`; index avg `0.0001` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.006` n `765`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1057` n `229`; crypto_major avg `0.0677` n `8`; equity avg `0.0255` n `88`; fx avg `0.0043` n `6`; index avg `-0.0076` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0502` n `765`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.0405` n `229`; crypto_major avg `0.1518` n `8`; equity avg `0.0041` n `88`; fx avg `-0.028` n `6`; index avg `-0.0039` n `25`; metal avg `-0.026` n `20`; unknown avg `0.0465` n `695`
- 24h: commodity avg `-0.0259` n `12`; crypto_alt avg `-2.023` n `229`; crypto_major avg `-1.5356` n `8`; equity avg `0.227` n `88`; fx avg `-0.0813` n `6`; index avg `0.0886` n `25`; metal avg `0.0439` n `20`; unknown avg `-0.11` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
