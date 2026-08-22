# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T15:07:21.261056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `0.1147` n `230`; crypto_major avg `-0.0063` n `8`; equity avg `-0.0146` n `121`; fx avg `0.0012` n `6`; index avg `-0.0024` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0324` n `794`
- 1h: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.1153` n `230`; crypto_major avg `-0.4307` n `8`; equity avg `-0.0457` n `121`; fx avg `0.0085` n `6`; index avg `0.0002` n `25`; metal avg `-0.0077` n `20`; unknown avg `0.0049` n `794`
- 4h: commodity avg `-0.0725` n `12`; crypto_alt avg `-0.2977` n `230`; crypto_major avg `-0.3224` n `8`; equity avg `0.0223` n `121`; fx avg `-0.0225` n `6`; index avg `-0.0007` n `25`; metal avg `0.0328` n `20`; unknown avg `0.1106` n `794`
- 24h: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.4783` n `230`; crypto_major avg `1.5445` n `8`; equity avg `-0.3539` n `121`; fx avg `0.0604` n `6`; index avg `-0.0463` n `25`; metal avg `-0.034` n `20`; unknown avg `1.2044` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
