# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T01:22:28.089360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.041` n `12`; crypto_alt avg `0.2227` n `229`; crypto_major avg `0.2285` n `8`; equity avg `0.0969` n `91`; fx avg `0.0084` n `6`; index avg `0.0222` n `25`; metal avg `0.0071` n `20`; unknown avg `0.2031` n `765`
- 1h: commodity avg `0.0563` n `12`; crypto_alt avg `0.3368` n `229`; crypto_major avg `0.3356` n `8`; equity avg `0.3147` n `91`; fx avg `-0.047` n `6`; index avg `0.0688` n `25`; metal avg `0.0961` n `20`; unknown avg `0.2294` n `765`
- 4h: commodity avg `0.0222` n `12`; crypto_alt avg `-0.0045` n `229`; crypto_major avg `-0.0164` n `8`; equity avg `0.0073` n `91`; fx avg `-0.0066` n `6`; index avg `-0.0642` n `25`; metal avg `0.0862` n `20`; unknown avg `-0.404` n `765`
- 24h: commodity avg `-1.0971` n `12`; crypto_alt avg `0.4921` n `229`; crypto_major avg `0.1353` n `8`; equity avg `0.9038` n `91`; fx avg `0.0492` n `6`; index avg `0.1888` n `25`; metal avg `0.7561` n `20`; unknown avg `-0.3118` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
