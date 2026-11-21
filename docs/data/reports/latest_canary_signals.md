# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T22:07:29.789960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `-0.2523` n `239`; crypto_major avg `-0.3366` n `8`; equity avg `-0.0957` n `166`; fx avg `-0.0073` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0242` n `20`; unknown avg `214.4565` n `1248`
- 1h: commodity avg `-0.0121` n `13`; crypto_alt avg `-0.3859` n `239`; crypto_major avg `-0.4268` n `8`; equity avg `-0.0393` n `166`; fx avg `0.0072` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0442` n `20`; unknown avg `-0.4166` n `1250`
- 4h: commodity avg `0.0482` n `13`; crypto_alt avg `-0.4552` n `239`; crypto_major avg `-0.1884` n `8`; equity avg `0.1323` n `166`; fx avg `0.0164` n `6`; index avg `0.1289` n `27`; metal avg `-0.0313` n `20`; unknown avg `-0.7311` n `1204`
- 24h: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.0541` n `239`; crypto_major avg `1.4841` n `8`; equity avg `1.0912` n `166`; fx avg `-0.0826` n `6`; index avg `0.2025` n `27`; metal avg `0.1232` n `20`; unknown avg `-0.6087` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
