# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T03:52:30.521678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `0.0239` n `229`; crypto_major avg `0.0948` n `8`; equity avg `0.0114` n `91`; fx avg `-0.007` n `6`; index avg `0.0015` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.1918` n `765`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `-0.0292` n `229`; crypto_major avg `0.0024` n `8`; equity avg `-0.0979` n `91`; fx avg `0.0151` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.9413` n `765`
- 4h: commodity avg `0.0722` n `12`; crypto_alt avg `0.9107` n `229`; crypto_major avg `1.2437` n `8`; equity avg `0.0129` n `91`; fx avg `0.0046` n `6`; index avg `-0.0176` n `25`; metal avg `0.192` n `20`; unknown avg `0.7858` n `763`
- 24h: commodity avg `-0.995` n `12`; crypto_alt avg `1.8094` n `229`; crypto_major avg `1.8838` n `8`; equity avg `1.7895` n `91`; fx avg `0.0324` n `6`; index avg `0.4293` n `25`; metal avg `0.9654` n `20`; unknown avg `0.195` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
