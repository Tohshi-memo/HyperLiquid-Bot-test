# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T04:07:28.218441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.055` n `230`; crypto_major avg `-0.07` n `8`; equity avg `-0.2495` n `98`; fx avg `-0.0087` n `6`; index avg `-0.0346` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0538` n `773`
- 1h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.1671` n `230`; crypto_major avg `-0.0934` n `8`; equity avg `0.0612` n `98`; fx avg `-0.0146` n `6`; index avg `0.025` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.0019` n `773`
- 4h: commodity avg `0.1248` n `12`; crypto_alt avg `-0.6091` n `230`; crypto_major avg `-0.6918` n `8`; equity avg `-0.4044` n `98`; fx avg `-0.0912` n `6`; index avg `-0.0512` n `25`; metal avg `0.0919` n `20`; unknown avg `0.3281` n `773`
- 24h: commodity avg `0.785` n `12`; crypto_alt avg `-0.8473` n `230`; crypto_major avg `-0.9042` n `8`; equity avg `-0.7366` n `98`; fx avg `-0.1652` n `6`; index avg `-0.1253` n `25`; metal avg `-0.1085` n `20`; unknown avg `1.7796` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0912`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
