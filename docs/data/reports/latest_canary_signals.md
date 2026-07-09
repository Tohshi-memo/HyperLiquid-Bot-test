# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T15:22:42.860183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `0.121` n `229`; crypto_major avg `-0.0123` n `8`; equity avg `0.1073` n `91`; fx avg `-0.0185` n `6`; index avg `0.0168` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0605` n `765`
- 1h: commodity avg `-0.2622` n `12`; crypto_alt avg `0.2414` n `229`; crypto_major avg `0.4945` n `8`; equity avg `0.8952` n `91`; fx avg `-0.0321` n `6`; index avg `0.1369` n `25`; metal avg `0.1892` n `20`; unknown avg `0.1379` n `765`
- 4h: commodity avg `-0.8221` n `12`; crypto_alt avg `0.3829` n `229`; crypto_major avg `0.5858` n `8`; equity avg `1.2635` n `91`; fx avg `-0.0494` n `6`; index avg `0.2816` n `25`; metal avg `0.4945` n `20`; unknown avg `0.3022` n `764`
- 24h: commodity avg `-1.2489` n `12`; crypto_alt avg `1.9935` n `229`; crypto_major avg `1.7027` n `8`; equity avg `3.6043` n `91`; fx avg `0.0407` n `6`; index avg `0.631` n `25`; metal avg `1.3827` n `20`; unknown avg `1.1093` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
