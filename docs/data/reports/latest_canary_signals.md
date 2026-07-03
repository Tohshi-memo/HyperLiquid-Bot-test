# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T08:52:31.302570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0921` n `12`; crypto_alt avg `-0.0291` n `229`; crypto_major avg `-0.1671` n `8`; equity avg `0.0053` n `88`; fx avg `0.0003` n `6`; index avg `0.0072` n `25`; metal avg `-0.0533` n `20`; unknown avg `-0.0074` n `765`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.0732` n `229`; crypto_major avg `-0.2019` n `8`; equity avg `0.0204` n `88`; fx avg `0.0447` n `6`; index avg `0.0157` n `25`; metal avg `-0.0291` n `20`; unknown avg `-0.0295` n `765`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `0.5579` n `229`; crypto_major avg `0.5634` n `8`; equity avg `0.0481` n `88`; fx avg `-0.1302` n `6`; index avg `0.0649` n `25`; metal avg `0.0613` n `20`; unknown avg `-0.0824` n `743`
- 24h: commodity avg `0.4185` n `12`; crypto_alt avg `2.0907` n `228`; crypto_major avg `3.1747` n `8`; equity avg `0.112` n `88`; fx avg `-0.1253` n `6`; index avg `0.1897` n `25`; metal avg `1.1661` n `20`; unknown avg `5.3437` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
