# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T12:52:24.004695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.3794` n `239`; crypto_major avg `0.3793` n `8`; equity avg `0.1733` n `166`; fx avg `0.0054` n `6`; index avg `0.0435` n `27`; metal avg `0.0252` n `20`; unknown avg `0.1899` n `1263`
- 1h: commodity avg `-0.0117` n `13`; crypto_alt avg `0.0057` n `239`; crypto_major avg `-0.2083` n `8`; equity avg `-0.1045` n `166`; fx avg `0.003` n `6`; index avg `0.0115` n `27`; metal avg `-0.0057` n `20`; unknown avg `0.5375` n `1253`
- 4h: commodity avg `0.0229` n `13`; crypto_alt avg `1.0732` n `239`; crypto_major avg `1.1724` n `8`; equity avg `0.5174` n `166`; fx avg `0.0003` n `6`; index avg `0.0595` n `27`; metal avg `0.0912` n `20`; unknown avg `515.7789` n `1151`
- 24h: commodity avg `0.0039` n `13`; crypto_alt avg `2.3996` n `239`; crypto_major avg `2.5231` n `8`; equity avg `1.6275` n `166`; fx avg `0.0084` n `6`; index avg `0.1932` n `27`; metal avg `0.1092` n `20`; unknown avg `0.8581` n `1086`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
