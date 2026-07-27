# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T21:07:32.075128+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `0.11` n `8`; equity avg `0.033` n `102`; fx avg `-0.0137` n `6`; index avg `-0.0074` n `25`; metal avg `0.0041` n `20`; unknown avg `3.9385` n `774`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.1628` n `230`; crypto_major avg `0.075` n `8`; equity avg `0.041` n `102`; fx avg `-0.0079` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0248` n `20`; unknown avg `3.8577` n `774`
- 4h: commodity avg `-0.1482` n `12`; crypto_alt avg `0.1493` n `230`; crypto_major avg `-0.0249` n `8`; equity avg `0.9115` n `102`; fx avg `-0.0041` n `6`; index avg `0.1848` n `25`; metal avg `0.0369` n `20`; unknown avg `99.1346` n `774`
- 24h: commodity avg `-1.0967` n `12`; crypto_alt avg `-0.6943` n `230`; crypto_major avg `-0.1224` n `8`; equity avg `-0.9751` n `102`; fx avg `-0.0366` n `6`; index avg `-0.3296` n `25`; metal avg `0.1794` n `20`; unknown avg `97.6792` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
