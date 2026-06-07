# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T05:22:22.075513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `0.2264` n `228`; crypto_major avg `0.2466` n `8`; equity avg `0.1238` n `74`; fx avg `0.0029` n `6`; index avg `0.0063` n `23`; metal avg `0.0673` n `18`; unknown avg `-0.2744` n `516`
- 1h: commodity avg `-0.0452` n `12`; crypto_alt avg `0.5247` n `228`; crypto_major avg `0.9556` n `8`; equity avg `0.3466` n `74`; fx avg `0.0043` n `6`; index avg `0.0491` n `23`; metal avg `0.1272` n `18`; unknown avg `0.0584` n `516`
- 4h: commodity avg `-0.1097` n `12`; crypto_alt avg `0.0332` n `228`; crypto_major avg `0.7995` n `8`; equity avg `0.5172` n `74`; fx avg `0.0066` n `6`; index avg `0.3788` n `23`; metal avg `0.4278` n `18`; unknown avg `0.4969` n `516`
- 24h: commodity avg `0.4418` n `12`; crypto_alt avg `3.612` n `228`; crypto_major avg `2.5584` n `8`; equity avg `2.2512` n `74`; fx avg `0.0505` n `6`; index avg `1.2673` n `23`; metal avg `0.8794` n `18`; unknown avg `0.6575` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
