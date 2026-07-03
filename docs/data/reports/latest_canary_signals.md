# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T07:52:25.409911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `0.067` n `229`; crypto_major avg `0.1623` n `8`; equity avg `-0.0224` n `88`; fx avg `-0.0059` n `6`; index avg `-0.0046` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.0139` n `765`
- 1h: commodity avg `-0.0905` n `12`; crypto_alt avg `0.1303` n `229`; crypto_major avg `0.2262` n `8`; equity avg `0.0232` n `88`; fx avg `-0.0339` n `6`; index avg `0.03` n `25`; metal avg `0.104` n `20`; unknown avg `0.3546` n `765`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `0.431` n `229`; crypto_major avg `0.7107` n `8`; equity avg `0.535` n `88`; fx avg `-0.1917` n `6`; index avg `0.2026` n `25`; metal avg `0.1065` n `20`; unknown avg `-0.0595` n `743`
- 24h: commodity avg `0.3277` n `12`; crypto_alt avg `2.3745` n `228`; crypto_major avg `3.7489` n `8`; equity avg `0.5602` n `88`; fx avg `-0.1649` n `6`; index avg `0.2449` n `25`; metal avg `1.4054` n `20`; unknown avg `5.6787` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
