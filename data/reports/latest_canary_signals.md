# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T16:52:23.456245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.0413` n `228`; crypto_major avg `0.0923` n `8`; equity avg `0.0687` n `74`; fx avg `-0.0031` n `6`; index avg `0.011` n `23`; metal avg `0.0244` n `18`; unknown avg `0.0307` n `516`
- 1h: commodity avg `0.0726` n `12`; crypto_alt avg `0.2487` n `228`; crypto_major avg `0.3784` n `8`; equity avg `0.2745` n `74`; fx avg `0.0259` n `6`; index avg `0.052` n `23`; metal avg `0.0884` n `18`; unknown avg `0.0822` n `516`
- 4h: commodity avg `0.2788` n `12`; crypto_alt avg `1.0277` n `228`; crypto_major avg `1.0769` n `8`; equity avg `0.6829` n `74`; fx avg `-0.0081` n `6`; index avg `0.245` n `23`; metal avg `0.1169` n `18`; unknown avg `0.3702` n `516`
- 24h: commodity avg `0.2837` n `12`; crypto_alt avg `2.6477` n `228`; crypto_major avg `3.0428` n `8`; equity avg `1.9631` n `74`; fx avg `-0.0605` n `6`; index avg `0.4553` n `23`; metal avg `0.6458` n `18`; unknown avg `-3.9629` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
