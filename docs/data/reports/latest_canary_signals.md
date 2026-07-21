# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T07:24:27.719461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0528` n `12`; crypto_alt avg `-0.128` n `230`; crypto_major avg `-0.0661` n `8`; equity avg `-0.0663` n `98`; fx avg `-0.0097` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.0065` n `771`
- 1h: commodity avg `0.1423` n `12`; crypto_alt avg `-0.025` n `230`; crypto_major avg `0.0726` n `8`; equity avg `0.0819` n `98`; fx avg `0.0249` n `6`; index avg `0.007` n `25`; metal avg `0.1066` n `20`; unknown avg `0.0419` n `771`
- 4h: commodity avg `0.1765` n `12`; crypto_alt avg `0.4509` n `230`; crypto_major avg `0.4858` n `8`; equity avg `0.8688` n `98`; fx avg `0.0236` n `6`; index avg `0.0898` n `25`; metal avg `0.431` n `20`; unknown avg `0.0659` n `755`
- 24h: commodity avg `-0.1042` n `12`; crypto_alt avg `2.8471` n `230`; crypto_major avg `2.8801` n `8`; equity avg `1.8357` n `98`; fx avg `-0.1064` n `6`; index avg `0.3401` n `25`; metal avg `0.8218` n `20`; unknown avg `0.2419` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0777`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
