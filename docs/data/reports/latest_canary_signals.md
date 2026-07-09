# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T11:22:37.697806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0504` n `12`; crypto_alt avg `-0.0682` n `229`; crypto_major avg `-0.1657` n `8`; equity avg `0.0597` n `91`; fx avg `0.0002` n `6`; index avg `0.0216` n `25`; metal avg `-0.0147` n `20`; unknown avg `-0.0277` n `764`
- 1h: commodity avg `0.0867` n `12`; crypto_alt avg `-0.2034` n `229`; crypto_major avg `-0.4497` n `8`; equity avg `-0.2482` n `91`; fx avg `-0.0013` n `6`; index avg `-0.0119` n `25`; metal avg `-0.0482` n `20`; unknown avg `0.0171` n `764`
- 4h: commodity avg `0.0764` n `12`; crypto_alt avg `-0.1701` n `229`; crypto_major avg `-0.5642` n `8`; equity avg `-0.1141` n `91`; fx avg `0.0055` n `6`; index avg `-0.0278` n `25`; metal avg `-0.0525` n `20`; unknown avg `-0.1116` n `764`
- 24h: commodity avg `-0.3125` n `12`; crypto_alt avg `1.4629` n `229`; crypto_major avg `0.3964` n `8`; equity avg `3.2189` n `91`; fx avg `0.1277` n `6`; index avg `0.4956` n `25`; metal avg `0.6336` n `20`; unknown avg `0.7538` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
