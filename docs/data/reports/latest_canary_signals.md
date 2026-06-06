# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T15:52:25.424287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.118` n `228`; crypto_major avg `0.0554` n `8`; equity avg `0.0739` n `74`; fx avg `0.0261` n `6`; index avg `-0.001` n `23`; metal avg `0.0046` n `18`; unknown avg `-1.3274` n `515`
- 1h: commodity avg `-0.1001` n `12`; crypto_alt avg `-0.641` n `228`; crypto_major avg `-0.5524` n `8`; equity avg `-0.1743` n `74`; fx avg `0.0141` n `6`; index avg `-0.0049` n `23`; metal avg `0.0065` n `18`; unknown avg `-3.5841` n `515`
- 4h: commodity avg `0.1026` n `12`; crypto_alt avg `-0.076` n `228`; crypto_major avg `-0.2613` n `8`; equity avg `0.3584` n `74`; fx avg `0.0188` n `6`; index avg `0.507` n `23`; metal avg `-0.203` n `18`; unknown avg `-0.53` n `413`
- 24h: commodity avg `0.0451` n `12`; crypto_alt avg `-0.8683` n `228`; crypto_major avg `-0.7149` n `8`; equity avg `-3.0629` n `74`; fx avg `-0.0606` n `6`; index avg `-1.8682` n `23`; metal avg `-1.3616` n `18`; unknown avg `0.8599` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
