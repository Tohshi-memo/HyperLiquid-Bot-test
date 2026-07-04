# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T21:22:26.847989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `0.1877` n `229`; crypto_major avg `0.2265` n `8`; equity avg `0.0185` n `88`; fx avg `0.0` n `6`; index avg `0.0014` n `25`; metal avg `0.0021` n `20`; unknown avg `1.2854` n `765`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `0.3973` n `229`; crypto_major avg `0.3777` n `8`; equity avg `0.068` n `88`; fx avg `0.0092` n `6`; index avg `-0.014` n `25`; metal avg `0.0325` n `20`; unknown avg `1.4646` n `765`
- 4h: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.1628` n `229`; crypto_major avg `0.0112` n `8`; equity avg `0.0853` n `88`; fx avg `-0.03` n `6`; index avg `0.0293` n `25`; metal avg `0.0496` n `20`; unknown avg `-0.7742` n `765`
- 24h: commodity avg `0.0163` n `12`; crypto_alt avg `0.4902` n `229`; crypto_major avg `0.717` n `8`; equity avg `0.2741` n `88`; fx avg `-0.0292` n `6`; index avg `-0.0297` n `25`; metal avg `0.0772` n `20`; unknown avg `-0.0371` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
