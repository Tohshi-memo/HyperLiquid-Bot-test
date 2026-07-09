# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T20:07:30.317095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.0727` n `229`; crypto_major avg `-0.0271` n `8`; equity avg `0.0974` n `91`; fx avg `-0.0091` n `6`; index avg `0.0153` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0672` n `765`
- 1h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.1112` n `229`; crypto_major avg `0.0078` n `8`; equity avg `-0.2074` n `91`; fx avg `-0.0165` n `6`; index avg `0.0065` n `25`; metal avg `-0.0211` n `20`; unknown avg `-0.0426` n `765`
- 4h: commodity avg `-0.1233` n `12`; crypto_alt avg `0.2069` n `229`; crypto_major avg `0.2039` n `8`; equity avg `-0.3746` n `91`; fx avg `-0.04` n `6`; index avg `0.0412` n `25`; metal avg `-0.2993` n `20`; unknown avg `-0.1202` n `765`
- 24h: commodity avg `-1.1506` n `12`; crypto_alt avg `1.0425` n `229`; crypto_major avg `0.5129` n `8`; equity avg `1.6344` n `91`; fx avg `0.0348` n `6`; index avg `0.3442` n `25`; metal avg `0.5882` n `20`; unknown avg `-0.0351` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
