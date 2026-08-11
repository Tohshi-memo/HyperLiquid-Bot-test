# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T07:58:53.636979+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `-0.1246` n `230`; crypto_major avg `0.0167` n `8`; equity avg `-0.0069` n `113`; fx avg `0.0041` n `6`; index avg `-0.003` n `25`; metal avg `-0.0596` n `20`; unknown avg `0.0518` n `785`
- 1h: commodity avg `0.0794` n `12`; crypto_alt avg `-0.2232` n `230`; crypto_major avg `0.1193` n `8`; equity avg `0.1412` n `113`; fx avg `-0.0156` n `6`; index avg `0.0146` n `25`; metal avg `-0.0339` n `20`; unknown avg `0.0524` n `785`
- 4h: commodity avg `0.3726` n `12`; crypto_alt avg `-0.6424` n `230`; crypto_major avg `-0.2378` n `8`; equity avg `-0.2913` n `113`; fx avg `0.0103` n `6`; index avg `-0.0547` n `25`; metal avg `-0.3654` n `20`; unknown avg `-0.0128` n `753`
- 24h: commodity avg `1.2748` n `12`; crypto_alt avg `-1.4387` n `230`; crypto_major avg `-1.1216` n `8`; equity avg `-1.4557` n `113`; fx avg `0.0358` n `6`; index avg `-0.0531` n `25`; metal avg `0.0094` n `20`; unknown avg `0.1628` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
