# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T22:37:32.018124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0568` n `230`; crypto_major avg `0.0565` n `8`; equity avg `0.0038` n `100`; fx avg `0.0011` n `6`; index avg `-0.0075` n `25`; metal avg `0.0206` n `20`; unknown avg `0.117` n `772`
- 1h: commodity avg `-0.0319` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `0.0618` n `8`; equity avg `-0.1286` n `100`; fx avg `0.004` n `6`; index avg `-0.0654` n `25`; metal avg `-0.0175` n `20`; unknown avg `0.0983` n `772`
- 4h: commodity avg `-0.0196` n `12`; crypto_alt avg `-0.1518` n `230`; crypto_major avg `0.0194` n `8`; equity avg `0.0174` n `100`; fx avg `-0.0028` n `6`; index avg `0.0251` n `25`; metal avg `0.0467` n `20`; unknown avg `0.2404` n `772`
- 24h: commodity avg `0.6204` n `12`; crypto_alt avg `-1.5326` n `230`; crypto_major avg `-1.9375` n `8`; equity avg `-1.208` n `99`; fx avg `-0.0603` n `6`; index avg `-0.2604` n `25`; metal avg `-0.6599` n `20`; unknown avg `-0.2771` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
