# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T00:37:26.686716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.1124` n `229`; crypto_major avg `-0.1316` n `8`; equity avg `0.0158` n `88`; fx avg `-0.0066` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0199` n `765`
- 1h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.357` n `229`; crypto_major avg `-0.4891` n `8`; equity avg `0.0118` n `88`; fx avg `-0.0016` n `6`; index avg `-0.017` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.1245` n `765`
- 4h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.673` n `229`; crypto_major avg `-0.6538` n `8`; equity avg `0.0354` n `88`; fx avg `0.0232` n `6`; index avg `0.0055` n `25`; metal avg `0.0291` n `20`; unknown avg `-0.1945` n `765`
- 24h: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.4754` n `229`; crypto_major avg `-0.3052` n `8`; equity avg `0.291` n `88`; fx avg `-0.022` n `6`; index avg `0.0491` n `25`; metal avg `0.0982` n `20`; unknown avg `-1.006` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
