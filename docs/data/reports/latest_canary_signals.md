# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T07:22:29.008025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `13`; crypto_alt avg `-0.0769` n `239`; crypto_major avg `-0.1567` n `8`; equity avg `-0.0444` n `165`; fx avg `-0.0162` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0541` n `20`; unknown avg `3.0058` n `1260`
- 1h: commodity avg `-0.0927` n `13`; crypto_alt avg `-0.1026` n `239`; crypto_major avg `-0.0632` n `8`; equity avg `-0.3117` n `165`; fx avg `-0.0245` n `6`; index avg `-0.0308` n `27`; metal avg `-0.1782` n `20`; unknown avg `-0.0822` n `1256`
- 4h: commodity avg `-0.0557` n `13`; crypto_alt avg `-0.2965` n `239`; crypto_major avg `-0.1853` n `8`; equity avg `-0.8033` n `165`; fx avg `-0.0121` n `6`; index avg `-0.0811` n `27`; metal avg `0.1188` n `20`; unknown avg `162.8932` n `1226`
- 24h: commodity avg `-0.171` n `13`; crypto_alt avg `-3.2122` n `239`; crypto_major avg `-2.6274` n `8`; equity avg `-7.2082` n `165`; fx avg `-0.0009` n `6`; index avg `-0.6693` n `27`; metal avg `-1.6912` n `20`; unknown avg `60.9071` n `1167`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
