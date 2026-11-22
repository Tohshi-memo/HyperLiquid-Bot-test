# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T21:22:23.800992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `13`; crypto_alt avg `0.0076` n `239`; crypto_major avg `-0.0179` n `8`; equity avg `-0.0366` n `166`; fx avg `0.0018` n `6`; index avg `-0.0119` n `27`; metal avg `-0.0215` n `20`; unknown avg `-0.328` n `1262`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `0.1659` n `239`; crypto_major avg `0.4509` n `8`; equity avg `0.0434` n `166`; fx avg `-0.0083` n `6`; index avg `-0.016` n `27`; metal avg `-0.0423` n `20`; unknown avg `160.622` n `1244`
- 4h: commodity avg `-0.0265` n `13`; crypto_alt avg `-0.1806` n `239`; crypto_major avg `0.1046` n `8`; equity avg `0.0301` n `166`; fx avg `-0.0008` n `6`; index avg `-0.032` n `27`; metal avg `-0.1071` n `20`; unknown avg `0.4756` n `1221`
- 24h: commodity avg `-0.1387` n `13`; crypto_alt avg `0.7007` n `239`; crypto_major avg `0.6365` n `8`; equity avg `0.7712` n `166`; fx avg `0.0043` n `6`; index avg `0.0749` n `27`; metal avg `-0.059` n `20`; unknown avg `235.0302` n `1058`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
