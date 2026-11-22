# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T02:52:24.164909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `13`; crypto_alt avg `-0.2296` n `239`; crypto_major avg `-0.1273` n `8`; equity avg `-0.0431` n `166`; fx avg `-0.0064` n `6`; index avg `-0.0202` n `27`; metal avg `-0.0167` n `20`; unknown avg `159.0724` n `1263`
- 1h: commodity avg `-0.0502` n `13`; crypto_alt avg `-0.9053` n `239`; crypto_major avg `-0.9488` n `8`; equity avg `-0.3647` n `166`; fx avg `0.003` n `6`; index avg `-0.0806` n `27`; metal avg `-0.0722` n `20`; unknown avg `1.5248` n `1261`
- 4h: commodity avg `-0.0523` n `13`; crypto_alt avg `-0.695` n `239`; crypto_major avg `-0.6457` n `8`; equity avg `-0.2264` n `166`; fx avg `-0.0133` n `6`; index avg `-0.0365` n `27`; metal avg `-0.0461` n `20`; unknown avg `163.3418` n `1250`
- 24h: commodity avg `-0.0253` n `13`; crypto_alt avg `-0.0952` n `239`; crypto_major avg `1.5868` n `8`; equity avg `0.4376` n `166`; fx avg `-0.0462` n `6`; index avg `0.1071` n `27`; metal avg `0.0496` n `20`; unknown avg `232.4673` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
