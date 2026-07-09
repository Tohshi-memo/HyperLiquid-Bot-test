# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T23:07:28.169457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.0463` n `229`; crypto_major avg `-0.031` n `8`; equity avg `-0.0452` n `91`; fx avg `0.0036` n `6`; index avg `-0.012` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0776` n `765`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.086` n `229`; crypto_major avg `-0.0183` n `8`; equity avg `0.0174` n `91`; fx avg `0.0018` n `6`; index avg `0.0042` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0867` n `765`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `-0.0611` n `229`; crypto_major avg `0.0316` n `8`; equity avg `-0.1555` n `91`; fx avg `0.0043` n `6`; index avg `0.009` n `25`; metal avg `0.0183` n `20`; unknown avg `-0.4331` n `765`
- 24h: commodity avg `-1.1407` n `12`; crypto_alt avg `0.9651` n `229`; crypto_major avg `0.5052` n `8`; equity avg `1.5787` n `91`; fx avg `0.0504` n `6`; index avg `0.36` n `25`; metal avg `0.6505` n `20`; unknown avg `-0.1773` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
