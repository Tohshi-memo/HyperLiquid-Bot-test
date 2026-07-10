# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T01:14:47.086805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.2005` n `229`; crypto_major avg `0.22` n `8`; equity avg `0.0645` n `91`; fx avg `-0.0285` n `6`; index avg `0.028` n `25`; metal avg `0.0603` n `20`; unknown avg `0.009` n `765`
- 1h: commodity avg `-0.008` n `12`; crypto_alt avg `0.0761` n `229`; crypto_major avg `0.1419` n `8`; equity avg `0.0045` n `91`; fx avg `-0.0119` n `6`; index avg `-0.0093` n `25`; metal avg `0.0928` n `20`; unknown avg `0.0797` n `765`
- 4h: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.2998` n `229`; crypto_major avg `-0.2856` n `8`; equity avg `-0.1141` n `91`; fx avg `-0.0105` n `6`; index avg `-0.0861` n `25`; metal avg `0.0746` n `20`; unknown avg `-0.4538` n `765`
- 24h: commodity avg `-1.0416` n `12`; crypto_alt avg `0.8178` n `229`; crypto_major avg `0.2322` n `8`; equity avg `0.9582` n `91`; fx avg `0.0519` n `6`; index avg `0.2007` n `25`; metal avg `0.7978` n `20`; unknown avg `-0.2693` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
