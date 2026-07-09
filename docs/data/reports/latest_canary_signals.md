# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T17:52:30.107345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.2396` n `229`; crypto_major avg `0.2091` n `8`; equity avg `0.0812` n `91`; fx avg `0.0014` n `6`; index avg `0.0039` n `25`; metal avg `0.038` n `20`; unknown avg `0.1921` n `765`
- 1h: commodity avg `-0.1385` n `12`; crypto_alt avg `0.5465` n `229`; crypto_major avg `0.5066` n `8`; equity avg `0.2548` n `91`; fx avg `0.0003` n `6`; index avg `0.0657` n `25`; metal avg `0.0056` n `20`; unknown avg `0.1416` n `765`
- 4h: commodity avg `-0.621` n `12`; crypto_alt avg `-0.0305` n `229`; crypto_major avg `-0.1126` n `8`; equity avg `0.1231` n `91`; fx avg `-0.0027` n `6`; index avg `0.0581` n `25`; metal avg `0.0589` n `20`; unknown avg `-0.0898` n `765`
- 24h: commodity avg `-1.0614` n `12`; crypto_alt avg `1.1653` n `229`; crypto_major avg `0.5833` n `8`; equity avg `2.7208` n `91`; fx avg `0.0434` n `6`; index avg `0.428` n `25`; metal avg `1.0082` n `20`; unknown avg `0.9472` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
