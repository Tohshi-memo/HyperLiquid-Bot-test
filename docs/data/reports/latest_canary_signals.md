# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T10:22:19.019795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `12`; crypto_alt avg `0.1996` n `228`; crypto_major avg `0.2582` n `8`; equity avg `-0.0569` n `74`; fx avg `-0.0009` n `6`; index avg `-0.0312` n `23`; metal avg `-0.0104` n `18`; unknown avg `-0.0185` n `516`
- 1h: commodity avg `0.0507` n `12`; crypto_alt avg `-0.9075` n `228`; crypto_major avg `-0.9397` n `8`; equity avg `-0.5446` n `74`; fx avg `-0.0061` n `6`; index avg `-0.363` n `23`; metal avg `-0.1564` n `18`; unknown avg `-3.3835` n `516`
- 4h: commodity avg `-0.2552` n `12`; crypto_alt avg `0.4414` n `228`; crypto_major avg `0.825` n `8`; equity avg `-0.1693` n `74`; fx avg `-0.0302` n `6`; index avg `-0.3575` n `23`; metal avg `0.0281` n `18`; unknown avg `-4.6854` n `516`
- 24h: commodity avg `0.1093` n `12`; crypto_alt avg `3.5806` n `228`; crypto_major avg `3.3336` n `8`; equity avg `2.1344` n `74`; fx avg `0.017` n `6`; index avg `0.6902` n `23`; metal avg `0.6431` n `18`; unknown avg `0.2908` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
