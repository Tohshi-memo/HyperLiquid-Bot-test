# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T22:52:28.739363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.1185` n `229`; crypto_major avg `-0.0689` n `8`; equity avg `0.0354` n `88`; fx avg `0.0007` n `6`; index avg `0.0013` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0667` n `765`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `-0.3689` n `229`; crypto_major avg `-0.1625` n `8`; equity avg `0.03` n `88`; fx avg `0.014` n `6`; index avg `0.0165` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.2149` n `765`
- 4h: commodity avg `0.0218` n `12`; crypto_alt avg `-0.6915` n `229`; crypto_major avg `-0.4841` n `8`; equity avg `0.1363` n `88`; fx avg `-0.0169` n `6`; index avg `0.0426` n `25`; metal avg `0.0554` n `20`; unknown avg `-0.649` n `765`
- 24h: commodity avg `0.0368` n `12`; crypto_alt avg `0.0585` n `229`; crypto_major avg `0.5691` n `8`; equity avg `0.3248` n `88`; fx avg `0.005` n `6`; index avg `0.0079` n `25`; metal avg `0.0877` n `20`; unknown avg `0.027` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
