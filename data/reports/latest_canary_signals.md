# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T05:37:21.403090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4104` n `12`; crypto_alt avg `-0.3189` n `228`; crypto_major avg `-0.349` n `8`; equity avg `-0.3382` n `74`; fx avg `-0.0248` n `6`; index avg `-0.1813` n `23`; metal avg `-0.9519` n `18`; unknown avg `-0.2912` n `517`
- 1h: commodity avg `0.2401` n `12`; crypto_alt avg `-0.2207` n `228`; crypto_major avg `-0.3505` n `8`; equity avg `-0.6468` n `74`; fx avg `-0.108` n `6`; index avg `-0.3121` n `23`; metal avg `-1.039` n `18`; unknown avg `-0.4855` n `517`
- 4h: commodity avg `0.4479` n `12`; crypto_alt avg `-0.6771` n `228`; crypto_major avg `-0.7108` n `8`; equity avg `-0.1587` n `74`; fx avg `-0.0878` n `6`; index avg `-0.0708` n `23`; metal avg `-0.9491` n `18`; unknown avg `-0.4974` n `517`
- 24h: commodity avg `0.9622` n `12`; crypto_alt avg `-0.4299` n `228`; crypto_major avg `1.2966` n `8`; equity avg `0.2897` n `74`; fx avg `-0.2105` n `6`; index avg `-0.1372` n `23`; metal avg `-1.4206` n `18`; unknown avg `-5.8155` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
