# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T19:37:29.367413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.057` n `12`; crypto_alt avg `0.0879` n `229`; crypto_major avg `0.1676` n `8`; equity avg `-0.121` n `91`; fx avg `-0.0063` n `6`; index avg `-0.0077` n `25`; metal avg `-0.0256` n `20`; unknown avg `0.0156` n `765`
- 1h: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.1249` n `229`; crypto_major avg `-0.1662` n `8`; equity avg `-0.2155` n `91`; fx avg `-0.0164` n `6`; index avg `-0.0218` n `25`; metal avg `-0.1714` n `20`; unknown avg `-0.0002` n `765`
- 4h: commodity avg `-0.1871` n `12`; crypto_alt avg `0.368` n `229`; crypto_major avg `0.313` n `8`; equity avg `-0.1551` n `91`; fx avg `-0.0322` n `6`; index avg `0.0499` n `25`; metal avg `-0.3249` n `20`; unknown avg `-0.0434` n `765`
- 24h: commodity avg `-1.018` n `12`; crypto_alt avg `1.2869` n `229`; crypto_major avg `0.6656` n `8`; equity avg `1.8976` n `91`; fx avg `0.0411` n `6`; index avg `0.3455` n `25`; metal avg `0.5004` n `20`; unknown avg `0.0243` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
