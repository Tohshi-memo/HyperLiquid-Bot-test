# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T20:37:30.152656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.0733` n `229`; crypto_major avg `0.1281` n `8`; equity avg `0.0424` n `91`; fx avg `0.0001` n `6`; index avg `0.0009` n `25`; metal avg `0.0207` n `20`; unknown avg `0.0727` n `765`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.0183` n `229`; crypto_major avg `0.1067` n `8`; equity avg `-0.0923` n `91`; fx avg `-0.0003` n `6`; index avg `0.0106` n `25`; metal avg `0.0263` n `20`; unknown avg `-0.1171` n `765`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `0.4409` n `229`; crypto_major avg `0.4462` n `8`; equity avg `-0.0881` n `91`; fx avg `-0.0317` n `6`; index avg `0.0639` n `25`; metal avg `-0.3269` n `20`; unknown avg `0.1084` n `765`
- 24h: commodity avg `-1.2617` n `12`; crypto_alt avg `1.434` n `229`; crypto_major avg `0.9297` n `8`; equity avg `1.8762` n `91`; fx avg `0.0471` n `6`; index avg `0.3954` n `25`; metal avg `0.7291` n `20`; unknown avg `-0.0014` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
