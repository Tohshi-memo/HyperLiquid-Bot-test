# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T08:13:27.348466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.3702` n `230`; crypto_major avg `0.2554` n `8`; equity avg `0.0614` n `121`; fx avg `-0.0485` n `6`; index avg `0.0103` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.0867` n `794`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `0.8752` n `230`; crypto_major avg `0.4783` n `8`; equity avg `0.1367` n `121`; fx avg `-0.0404` n `6`; index avg `0.0155` n `25`; metal avg `0.0079` n `20`; unknown avg `0.2069` n `794`
- 4h: commodity avg `0.016` n `12`; crypto_alt avg `1.1634` n `230`; crypto_major avg `-0.1373` n `8`; equity avg `-0.0268` n `121`; fx avg `-0.0276` n `6`; index avg `-0.0194` n `25`; metal avg `0.0041` n `20`; unknown avg `0.4872` n `778`
- 24h: commodity avg `0.0098` n `12`; crypto_alt avg `-3.5733` n `230`; crypto_major avg `-1.9838` n `8`; equity avg `0.0799` n `121`; fx avg `0.075` n `6`; index avg `0.0062` n `25`; metal avg `0.0585` n `20`; unknown avg `2.341` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
