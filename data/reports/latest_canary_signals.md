# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T04:07:27.560596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0004` n `228`; crypto_major avg `-0.0253` n `8`; equity avg `-0.0389` n `74`; fx avg `0.0069` n `6`; index avg `-0.0342` n `23`; metal avg `0.008` n `18`; unknown avg `-0.0339` n `516`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `-0.1661` n `228`; crypto_major avg `-0.0449` n `8`; equity avg `0.0726` n `74`; fx avg `0.0081` n `6`; index avg `0.1391` n `23`; metal avg `0.0118` n `18`; unknown avg `0.375` n `516`
- 4h: commodity avg `-0.0192` n `12`; crypto_alt avg `1.4254` n `228`; crypto_major avg `1.5391` n `8`; equity avg `0.4154` n `74`; fx avg `0.0072` n `6`; index avg `0.3696` n `23`; metal avg `0.4169` n `18`; unknown avg `2.1314` n `516`
- 24h: commodity avg `0.1853` n `12`; crypto_alt avg `2.9907` n `228`; crypto_major avg `1.9471` n `8`; equity avg `1.4503` n `74`; fx avg `0.042` n `6`; index avg `0.7887` n `23`; metal avg `0.5818` n `18`; unknown avg `0.6247` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
