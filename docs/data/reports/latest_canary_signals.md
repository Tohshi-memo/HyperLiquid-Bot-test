# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T19:37:21.751954+00:00`
- Correlation status: `ready`
- Asset price records: `482`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.64` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1346` n `12`; crypto_alt avg `-0.2818` n `228`; crypto_major avg `-0.201` n `8`; equity avg `0.0102` n `65`; fx avg `0.0033` n `4`; index avg `-0.0352` n `23`; metal avg `-0.0342` n `18`; unknown avg `-0.0569` n `356`
- 1h: commodity avg `0.0782` n `12`; crypto_alt avg `-0.2512` n `228`; crypto_major avg `-0.0106` n `8`; equity avg `0.0777` n `65`; fx avg `-0.0079` n `4`; index avg `0.0865` n `23`; metal avg `0.1933` n `18`; unknown avg `0.0198` n `356`
- 4h: commodity avg `0.1366` n `12`; crypto_alt avg `-0.0396` n `228`; crypto_major avg `-0.153` n `8`; equity avg `0.7677` n `65`; fx avg `-0.0279` n `4`; index avg `0.3705` n `23`; metal avg `0.0468` n `18`; unknown avg `-0.2837` n `356`
- 24h: commodity avg `-2.4465` n `7`; crypto_alt avg `2.0098` n `223`; crypto_major avg `0.2475` n `7`; equity avg `2.864` n `47`; fx avg `-0.5095` n `4`; index avg `1.8196` n `6`; metal avg `3.4093` n `7`; unknown avg `3.1819` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1562`, n `474`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1425`, n `474`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1379`, n `474`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1313`, n `478`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.127`, n `474`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `478`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `474`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `474`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0779`, n `478`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `478`, weak_sample_signal
