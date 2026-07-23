# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T14:22:27.069386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0374` n `12`; crypto_alt avg `0.2596` n `230`; crypto_major avg `0.2297` n `8`; equity avg `-0.0324` n `100`; fx avg `-0.0092` n `6`; index avg `-0.0256` n `25`; metal avg `0.0064` n `20`; unknown avg `0.008` n `772`
- 1h: commodity avg `0.0654` n `12`; crypto_alt avg `0.2895` n `230`; crypto_major avg `0.0116` n `8`; equity avg `1.1366` n `100`; fx avg `-0.0111` n `6`; index avg `0.0838` n `25`; metal avg `0.0192` n `20`; unknown avg `0.0613` n `772`
- 4h: commodity avg `0.1467` n `12`; crypto_alt avg `-0.2746` n `230`; crypto_major avg `-0.7889` n `8`; equity avg `-0.5307` n `99`; fx avg `-0.0091` n `6`; index avg `-0.2376` n `25`; metal avg `-0.336` n `20`; unknown avg `0.0844` n `772`
- 24h: commodity avg `0.8587` n `12`; crypto_alt avg `-0.7044` n `230`; crypto_major avg `-0.8513` n `8`; equity avg `-0.6715` n `99`; fx avg `-0.0856` n `6`; index avg `-0.238` n `25`; metal avg `-0.9036` n `20`; unknown avg `-0.0597` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0661`, n `666`, weak_sample_signal
