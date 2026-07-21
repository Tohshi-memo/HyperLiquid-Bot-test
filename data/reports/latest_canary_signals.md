# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T18:22:32.007840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.0105` n `230`; crypto_major avg `-0.0269` n `8`; equity avg `-0.1362` n `98`; fx avg `-0.0011` n `6`; index avg `-0.0108` n `25`; metal avg `0.0193` n `20`; unknown avg `-0.0785` n `771`
- 1h: commodity avg `-0.015` n `12`; crypto_alt avg `0.0949` n `230`; crypto_major avg `-0.0964` n `8`; equity avg `-0.071` n `98`; fx avg `0.0158` n `6`; index avg `0.0073` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0891` n `771`
- 4h: commodity avg `-0.0678` n `12`; crypto_alt avg `-0.1177` n `230`; crypto_major avg `-0.3533` n `8`; equity avg `1.0026` n `98`; fx avg `0.0025` n `6`; index avg `0.198` n `25`; metal avg `0.0805` n `20`; unknown avg `0.1211` n `771`
- 24h: commodity avg `0.3231` n `12`; crypto_alt avg `0.5804` n `230`; crypto_major avg `0.3982` n `8`; equity avg `2.9375` n `98`; fx avg `0.0226` n `6`; index avg `0.489` n `25`; metal avg `0.6593` n `20`; unknown avg `0.1251` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0901`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0542`, n `666`, weak_sample_signal
