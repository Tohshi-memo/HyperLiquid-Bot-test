# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T02:07:29.202129+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `0.1688` n `234`; crypto_major avg `-0.0523` n `8`; equity avg `0.0237` n `140`; fx avg `-0.0075` n `6`; index avg `0.011` n `26`; metal avg `0.0248` n `20`; unknown avg `0.0243` n `917`
- 1h: commodity avg `0.019` n `12`; crypto_alt avg `0.7709` n `234`; crypto_major avg `0.3437` n `8`; equity avg `-0.0451` n `140`; fx avg `0.0323` n `6`; index avg `-0.0163` n `26`; metal avg `-0.0374` n `20`; unknown avg `-0.1735` n `917`
- 4h: commodity avg `-0.0094` n `12`; crypto_alt avg `1.8931` n `234`; crypto_major avg `1.1078` n `8`; equity avg `-0.1711` n `140`; fx avg `0.093` n `6`; index avg `-0.0937` n `26`; metal avg `0.1545` n `20`; unknown avg `-0.1812` n `845`
- 24h: commodity avg `-0.2815` n `12`; crypto_alt avg `4.4418` n `234`; crypto_major avg `2.5715` n `8`; equity avg `1.563` n `138`; fx avg `0.0499` n `6`; index avg `0.2126` n `26`; metal avg `0.5129` n `20`; unknown avg `1.8267` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
