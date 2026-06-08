# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T05:07:23.205150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0751` n `12`; crypto_alt avg `-0.3245` n `228`; crypto_major avg `-0.479` n `8`; equity avg `-0.1867` n `74`; fx avg `0.0059` n `6`; index avg `-0.1149` n `23`; metal avg `-0.1305` n `18`; unknown avg `-0.2428` n `517`
- 1h: commodity avg `0.23` n `12`; crypto_alt avg `-0.6888` n `228`; crypto_major avg `-0.6744` n `8`; equity avg `-0.3916` n `74`; fx avg `0.018` n `6`; index avg `-0.1939` n `23`; metal avg `-0.2623` n `18`; unknown avg `-0.1402` n `517`
- 4h: commodity avg `0.7799` n `12`; crypto_alt avg `-1.3479` n `228`; crypto_major avg `-1.1643` n `8`; equity avg `-0.3713` n `74`; fx avg `0.0177` n `6`; index avg `-0.1685` n `23`; metal avg `-0.3896` n `18`; unknown avg `-0.2703` n `517`
- 24h: commodity avg `0.6738` n `12`; crypto_alt avg `0.2598` n `228`; crypto_major avg `1.8264` n `8`; equity avg `0.8807` n `74`; fx avg `-0.0826` n `6`; index avg `0.014` n `23`; metal avg `-0.4378` n `18`; unknown avg `-5.6431` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
