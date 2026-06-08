# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T09:37:27.612227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0499` n `12`; crypto_alt avg `-0.0844` n `228`; crypto_major avg `-0.0487` n `8`; equity avg `-0.0542` n `74`; fx avg `-0.0022` n `6`; index avg `-0.0608` n `23`; metal avg `0.0656` n `18`; unknown avg `0.0187` n `517`
- 1h: commodity avg `0.0588` n `12`; crypto_alt avg `0.2363` n `228`; crypto_major avg `0.2582` n `8`; equity avg `-0.0977` n `74`; fx avg `-0.0299` n `6`; index avg `-0.0479` n `23`; metal avg `0.1421` n `18`; unknown avg `0.0643` n `517`
- 4h: commodity avg `-0.445` n `12`; crypto_alt avg `1.2582` n `228`; crypto_major avg `1.053` n `8`; equity avg `0.8331` n `74`; fx avg `-0.1577` n `6`; index avg `0.3768` n `23`; metal avg `0.8197` n `18`; unknown avg `-0.0366` n `507`
- 24h: commodity avg `0.7894` n `12`; crypto_alt avg `0.0443` n `228`; crypto_major avg `1.1556` n `8`; equity avg `0.7992` n `74`; fx avg `-0.3298` n `6`; index avg `0.2723` n `23`; metal avg `-0.8248` n `18`; unknown avg `-4.5256` n `506`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
