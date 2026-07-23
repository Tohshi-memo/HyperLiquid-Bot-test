# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T11:52:25.034945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `0.0117` n `230`; crypto_major avg `-0.0054` n `8`; equity avg `0.0756` n `99`; fx avg `0.022` n `6`; index avg `-0.0106` n `25`; metal avg `0.0226` n `20`; unknown avg `0.0347` n `772`
- 1h: commodity avg `0.0505` n `12`; crypto_alt avg `-0.0091` n `230`; crypto_major avg `-0.0248` n `8`; equity avg `-0.5501` n `99`; fx avg `0.0041` n `6`; index avg `-0.1367` n `25`; metal avg `-0.1009` n `20`; unknown avg `0.008` n `772`
- 4h: commodity avg `0.0915` n `12`; crypto_alt avg `0.2148` n `230`; crypto_major avg `0.4161` n `8`; equity avg `0.0985` n `99`; fx avg `-0.0304` n `6`; index avg `-0.016` n `25`; metal avg `-0.0858` n `20`; unknown avg `0.0687` n `772`
- 24h: commodity avg `0.677` n `12`; crypto_alt avg `-0.2848` n `230`; crypto_major avg `-0.0723` n `8`; equity avg `0.4882` n `99`; fx avg `-0.0813` n `6`; index avg `0.1063` n `25`; metal avg `-0.4404` n `20`; unknown avg `10.2961` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
