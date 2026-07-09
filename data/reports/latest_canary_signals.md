# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T23:36:11.352609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `0.0411` n `229`; crypto_major avg `0.0301` n `8`; equity avg `0.0234` n `91`; fx avg `0.0095` n `6`; index avg `0.0043` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0264` n `765`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `-0.1185` n `229`; crypto_major avg `-0.2027` n `8`; equity avg `0.1369` n `91`; fx avg `0.011` n `6`; index avg `0.0114` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.1509` n `765`
- 4h: commodity avg `0.0089` n `12`; crypto_alt avg `-0.3237` n `229`; crypto_major avg `-0.2108` n `8`; equity avg `0.1132` n `91`; fx avg `0.018` n `6`; index avg `0.0217` n `25`; metal avg `0.0489` n `20`; unknown avg `-0.4944` n `765`
- 24h: commodity avg `-1.1041` n `12`; crypto_alt avg `0.8937` n `229`; crypto_major avg `0.4368` n `8`; equity avg `1.6817` n `91`; fx avg `0.0471` n `6`; index avg `0.3333` n `25`; metal avg `0.649` n `20`; unknown avg `-0.197` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
