# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T22:22:27.401543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `-0.1218` n `230`; crypto_major avg `-0.0328` n `8`; equity avg `-0.0558` n `100`; fx avg `-0.0023` n `6`; index avg `-0.0157` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.0701` n `772`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.1609` n `230`; crypto_major avg `-0.0427` n `8`; equity avg `-0.2398` n `100`; fx avg `-0.0044` n `6`; index avg `-0.0597` n `25`; metal avg `-0.0395` n `20`; unknown avg `-0.2075` n `772`
- 4h: commodity avg `-0.1383` n `12`; crypto_alt avg `-0.016` n `230`; crypto_major avg `0.0947` n `8`; equity avg `0.0182` n `100`; fx avg `-0.0021` n `6`; index avg `0.0365` n `25`; metal avg `0.053` n `20`; unknown avg `0.1754` n `772`
- 24h: commodity avg `0.6346` n `12`; crypto_alt avg `-1.7341` n `230`; crypto_major avg `-2.1044` n `8`; equity avg `-1.29` n `99`; fx avg `-0.0593` n `6`; index avg `-0.2779` n `25`; metal avg `-0.6926` n `20`; unknown avg `-0.2901` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
