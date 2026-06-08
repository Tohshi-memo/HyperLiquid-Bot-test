# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T03:07:25.873972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `-0.0923` n `228`; crypto_major avg `-0.0813` n `8`; equity avg `-0.0692` n `74`; fx avg `0.004` n `6`; index avg `0.1058` n `23`; metal avg `-0.1885` n `18`; unknown avg `-0.0211` n `517`
- 1h: commodity avg `0.1299` n `12`; crypto_alt avg `-0.129` n `228`; crypto_major avg `0.163` n `8`; equity avg `0.4524` n `74`; fx avg `0.0013` n `6`; index avg `0.4583` n `23`; metal avg `-0.2694` n `18`; unknown avg `-0.0699` n `517`
- 4h: commodity avg `0.1522` n `12`; crypto_alt avg `-0.0869` n `228`; crypto_major avg `0.7219` n `8`; equity avg `1.0635` n `74`; fx avg `-0.0346` n `6`; index avg `0.578` n `23`; metal avg `-0.192` n `18`; unknown avg `-0.3481` n `516`
- 24h: commodity avg `0.4842` n `12`; crypto_alt avg `1.0537` n `228`; crypto_major avg `3.5686` n `8`; equity avg `1.9013` n `74`; fx avg `-0.0917` n `6`; index avg `0.4911` n `23`; metal avg `-0.35` n `18`; unknown avg `-5.3101` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
