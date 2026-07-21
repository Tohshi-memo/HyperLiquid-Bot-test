# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T11:22:32.226510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `-0.021` n `230`; crypto_major avg `0.0286` n `8`; equity avg `-0.029` n `98`; fx avg `0.0049` n `6`; index avg `-0.0103` n `25`; metal avg `0.0154` n `20`; unknown avg `0.0115` n `771`
- 1h: commodity avg `0.1035` n `12`; crypto_alt avg `-0.2094` n `230`; crypto_major avg `-0.2828` n `8`; equity avg `-0.293` n `98`; fx avg `-0.0033` n `6`; index avg `-0.0298` n `25`; metal avg `-0.0904` n `20`; unknown avg `0.0663` n `771`
- 4h: commodity avg `0.1661` n `12`; crypto_alt avg `-0.1478` n `230`; crypto_major avg `-0.0027` n `8`; equity avg `0.1437` n `98`; fx avg `0.0016` n `6`; index avg `0.0405` n `25`; metal avg `-0.0642` n `20`; unknown avg `0.0054` n `771`
- 24h: commodity avg `0.4738` n `12`; crypto_alt avg `1.9665` n `230`; crypto_major avg `2.3056` n `8`; equity avg `1.1162` n `98`; fx avg `-0.0841` n `6`; index avg `0.172` n `25`; metal avg `0.5464` n `20`; unknown avg `0.1913` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0681`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
