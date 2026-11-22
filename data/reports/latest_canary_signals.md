# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T20:37:25.041565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `13`; crypto_alt avg `0.0613` n `239`; crypto_major avg `0.0767` n `8`; equity avg `-0.0013` n `166`; fx avg `-0.005` n `6`; index avg `-0.0053` n `27`; metal avg `-0.0248` n `20`; unknown avg `174.0564` n `1264`
- 1h: commodity avg `0.0112` n `13`; crypto_alt avg `0.1219` n `239`; crypto_major avg `-0.054` n `8`; equity avg `0.0006` n `166`; fx avg `0.0109` n `6`; index avg `-0.012` n `27`; metal avg `-0.0219` n `20`; unknown avg `16.3279` n `1254`
- 4h: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.4374` n `239`; crypto_major avg `-0.606` n `8`; equity avg `0.0946` n `166`; fx avg `0.0038` n `6`; index avg `-0.0131` n `27`; metal avg `-0.0846` n `20`; unknown avg `163.2196` n `1231`
- 24h: commodity avg `-0.1167` n `13`; crypto_alt avg `0.5574` n `239`; crypto_major avg `0.2771` n `8`; equity avg `0.7417` n `166`; fx avg `-0.0116` n `6`; index avg `0.0962` n `27`; metal avg `-0.0425` n `20`; unknown avg `235.1241` n `1058`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
