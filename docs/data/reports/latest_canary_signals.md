# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T01:37:42.494810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `13`; crypto_alt avg `-0.2388` n `239`; crypto_major avg `-0.3388` n `8`; equity avg `-0.043` n `166`; fx avg `0.004` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0301` n `20`; unknown avg `158.2832` n `1262`
- 1h: commodity avg `-0.0121` n `13`; crypto_alt avg `-0.3602` n `239`; crypto_major avg `-0.41` n `8`; equity avg `-0.0631` n `166`; fx avg `0.0101` n `6`; index avg `-0.007` n `27`; metal avg `-0.0192` n `20`; unknown avg `2.3663` n `1258`
- 4h: commodity avg `-0.0426` n `13`; crypto_alt avg `0.1552` n `239`; crypto_major avg `0.0756` n `8`; equity avg `0.6447` n `166`; fx avg `-0.0212` n `6`; index avg `0.0856` n `27`; metal avg `0.0893` n `20`; unknown avg `164.0933` n `1228`
- 24h: commodity avg `0.2973` n `13`; crypto_alt avg `-5.0028` n `239`; crypto_major avg `-5.9021` n `8`; equity avg `-5.1403` n `166`; fx avg `0.005` n `6`; index avg `-0.5617` n `27`; metal avg `-0.3181` n `20`; unknown avg `12.75` n `1117`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
