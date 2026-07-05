# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T14:13:00.050258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.1215` n `229`; crypto_major avg `0.0529` n `8`; equity avg `-0.0401` n `88`; fx avg `-0.0` n `6`; index avg `-0.0359` n `25`; metal avg `-0.0208` n `20`; unknown avg `0.0177` n `765`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `-0.1538` n `229`; crypto_major avg `-0.0248` n `8`; equity avg `-0.0407` n `88`; fx avg `0.0012` n `6`; index avg `-0.0103` n `25`; metal avg `-0.015` n `20`; unknown avg `0.0235` n `765`
- 4h: commodity avg `-0.0078` n `12`; crypto_alt avg `0.6182` n `229`; crypto_major avg `0.8417` n `8`; equity avg `0.1038` n `88`; fx avg `-0.0398` n `6`; index avg `0.01` n `25`; metal avg `0.0155` n `20`; unknown avg `0.1299` n `765`
- 24h: commodity avg `0.007` n `12`; crypto_alt avg `-1.0726` n `229`; crypto_major avg `-0.4433` n `8`; equity avg `0.279` n `88`; fx avg `-0.018` n `6`; index avg `0.0456` n `25`; metal avg `0.0783` n `20`; unknown avg `-1.1291` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
