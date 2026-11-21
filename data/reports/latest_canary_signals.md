# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T22:22:23.402804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `0.2015` n `239`; crypto_major avg `0.17` n `8`; equity avg `0.1052` n `166`; fx avg `0.0044` n `6`; index avg `0.0096` n `27`; metal avg `-0.0121` n `20`; unknown avg `0.05` n `1260`
- 1h: commodity avg `-0.0264` n `13`; crypto_alt avg `-0.1564` n `239`; crypto_major avg `-0.2917` n `8`; equity avg `0.0163` n `166`; fx avg `0.018` n `6`; index avg `0.0029` n `27`; metal avg `-0.057` n `20`; unknown avg `373.3005` n `1252`
- 4h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.1103` n `239`; crypto_major avg `0.1215` n `8`; equity avg `0.2676` n `166`; fx avg `0.0125` n `6`; index avg `0.1327` n `27`; metal avg `-0.0409` n `20`; unknown avg `42.2613` n `1206`
- 24h: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.1165` n `239`; crypto_major avg `1.4057` n `8`; equity avg `1.042` n `166`; fx avg `-0.0589` n `6`; index avg `0.1986` n `27`; metal avg `0.1194` n `20`; unknown avg `232.1375` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
