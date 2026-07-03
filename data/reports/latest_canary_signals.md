# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T08:07:33.308411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.0132` n `229`; crypto_major avg `-0.0721` n `8`; equity avg `0.0784` n `88`; fx avg `0.0403` n `6`; index avg `0.0171` n `25`; metal avg `0.0379` n `20`; unknown avg `-0.0651` n `765`
- 1h: commodity avg `-0.0605` n `12`; crypto_alt avg `0.0225` n `229`; crypto_major avg `0.0754` n `8`; equity avg `0.0741` n `88`; fx avg `0.0142` n `6`; index avg `0.0059` n `25`; metal avg `0.0881` n `20`; unknown avg `0.166` n `765`
- 4h: commodity avg `-0.0065` n `12`; crypto_alt avg `0.5378` n `229`; crypto_major avg `0.7103` n `8`; equity avg `0.4195` n `88`; fx avg `-0.1371` n `6`; index avg `0.1604` n `25`; metal avg `0.1523` n `20`; unknown avg `-0.1132` n `743`
- 24h: commodity avg `0.3857` n `12`; crypto_alt avg `2.2278` n `228`; crypto_major avg `3.5131` n `8`; equity avg `0.6256` n `88`; fx avg `-0.1262` n `6`; index avg `0.2869` n `25`; metal avg `1.4418` n `20`; unknown avg `5.2136` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
