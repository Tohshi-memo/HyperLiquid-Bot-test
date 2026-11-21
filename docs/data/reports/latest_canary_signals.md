# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T23:52:27.213502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `13`; crypto_alt avg `0.1016` n `239`; crypto_major avg `0.0067` n `8`; equity avg `0.0406` n `166`; fx avg `-0.0091` n `6`; index avg `-0.0136` n `27`; metal avg `0.0086` n `20`; unknown avg `0.342` n `1262`
- 1h: commodity avg `-0.0049` n `13`; crypto_alt avg `0.2671` n `239`; crypto_major avg `0.2302` n `8`; equity avg `0.0563` n `166`; fx avg `-0.0069` n `6`; index avg `0.0271` n `27`; metal avg `0.0201` n `20`; unknown avg `161.5157` n `1250`
- 4h: commodity avg `-0.0048` n `13`; crypto_alt avg `0.1203` n `239`; crypto_major avg `-0.2302` n `8`; equity avg `0.1537` n `166`; fx avg `0.0054` n `6`; index avg `0.0378` n `27`; metal avg `-0.0853` n `20`; unknown avg `208.0902` n `1198`
- 24h: commodity avg `0.0371` n `13`; crypto_alt avg `0.2639` n `239`; crypto_major avg `1.8477` n `8`; equity avg `0.693` n `166`; fx avg `-0.0373` n `6`; index avg `0.1749` n `27`; metal avg `0.1109` n `20`; unknown avg `417.1022` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
