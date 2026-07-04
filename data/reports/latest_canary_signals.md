# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T01:37:27.181820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.2925` n `229`; crypto_major avg `-0.2075` n `8`; equity avg `-0.032` n `88`; fx avg `-0.001` n `6`; index avg `0.0023` n `25`; metal avg `0.0061` n `20`; unknown avg `0.193` n `765`
- 1h: commodity avg `-0.0481` n `12`; crypto_alt avg `-0.7393` n `229`; crypto_major avg `-0.5256` n `8`; equity avg `0.0089` n `88`; fx avg `-0.0204` n `6`; index avg `0.0045` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.1767` n `765`
- 4h: commodity avg `0.0104` n `12`; crypto_alt avg `-0.7143` n `229`; crypto_major avg `-0.2999` n `8`; equity avg `-0.0443` n `88`; fx avg `0.0075` n `6`; index avg `-0.0515` n `25`; metal avg `-0.0448` n `20`; unknown avg `0.3639` n `765`
- 24h: commodity avg `0.0912` n `12`; crypto_alt avg `1.6217` n `229`; crypto_major avg `2.1797` n `8`; equity avg `0.9482` n `88`; fx avg `-0.1158` n `6`; index avg `0.1867` n `25`; metal avg `-0.1654` n `20`; unknown avg `3.1778` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
