# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T19:22:26.187025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.0079` n `230`; crypto_major avg `0.0379` n `8`; equity avg `0.1057` n `102`; fx avg `0.0092` n `6`; index avg `0.026` n `25`; metal avg `0.0467` n `20`; unknown avg `-0.0485` n `779`
- 1h: commodity avg `-0.0899` n `12`; crypto_alt avg `-0.0436` n `230`; crypto_major avg `0.0751` n `8`; equity avg `0.4325` n `102`; fx avg `0.0087` n `6`; index avg `0.0564` n `25`; metal avg `0.1041` n `20`; unknown avg `-0.1003` n `779`
- 4h: commodity avg `-0.1674` n `12`; crypto_alt avg `-0.1531` n `230`; crypto_major avg `0.3224` n `8`; equity avg `0.8584` n `102`; fx avg `-0.0443` n `6`; index avg `0.17` n `25`; metal avg `0.333` n `20`; unknown avg `-0.0582` n `779`
- 24h: commodity avg `-0.152` n `12`; crypto_alt avg `0.2669` n `230`; crypto_major avg `1.352` n `8`; equity avg `4.3707` n `102`; fx avg `-0.4062` n `6`; index avg `0.4355` n `25`; metal avg `0.4345` n `20`; unknown avg `-0.0199` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
