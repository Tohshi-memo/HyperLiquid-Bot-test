# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T05:52:24.181947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1932` n `12`; crypto_alt avg `0.0605` n `228`; crypto_major avg `0.2182` n `8`; equity avg `-0.1748` n `74`; fx avg `0.0216` n `6`; index avg `0.0706` n `23`; metal avg `0.4202` n `18`; unknown avg `-0.0814` n `517`
- 1h: commodity avg `0.1238` n `12`; crypto_alt avg `-0.3633` n `228`; crypto_major avg `-0.4161` n `8`; equity avg `-0.8027` n `74`; fx avg `-0.0984` n `6`; index avg `-0.2054` n `23`; metal avg `-0.6469` n `18`; unknown avg `-0.7058` n `517`
- 4h: commodity avg `0.4654` n `12`; crypto_alt avg `-0.9235` n `228`; crypto_major avg `-0.7189` n `8`; equity avg `-0.6576` n `74`; fx avg `-0.0797` n `6`; index avg `-0.106` n `23`; metal avg `-0.7677` n `18`; unknown avg `-0.4341` n `517`
- 24h: commodity avg `0.7804` n `12`; crypto_alt avg `-0.3263` n `228`; crypto_major avg `1.5197` n `8`; equity avg `0.1264` n `74`; fx avg `-0.1822` n `6`; index avg `-0.0774` n `23`; metal avg `-1.0225` n `18`; unknown avg `-5.8228` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
