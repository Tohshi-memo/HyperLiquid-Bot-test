# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T23:52:24.267466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `0.1304` n `239`; crypto_major avg `-0.0092` n `8`; equity avg `-0.0072` n `166`; fx avg `-0.0251` n `6`; index avg `0.0566` n `27`; metal avg `0.0203` n `20`; unknown avg `-0.2888` n `1265`
- 1h: commodity avg `-0.3195` n `13`; crypto_alt avg `0.3792` n `239`; crypto_major avg `0.4037` n `8`; equity avg `0.2056` n `166`; fx avg `0.0092` n `6`; index avg `0.0566` n `27`; metal avg `0.3738` n `20`; unknown avg `39.8265` n `1250`
- 4h: commodity avg `-0.3669` n `13`; crypto_alt avg `0.1825` n `239`; crypto_major avg `0.4814` n `8`; equity avg `0.3642` n `166`; fx avg `0.0923` n `6`; index avg `0.0418` n `27`; metal avg `0.3302` n `20`; unknown avg `1.9869` n `1202`
- 24h: commodity avg `-0.4721` n `13`; crypto_alt avg `0.585` n `239`; crypto_major avg `1.0825` n `8`; equity avg `1.139` n `166`; fx avg `0.088` n `6`; index avg `0.1208` n `27`; metal avg `0.3589` n `20`; unknown avg `241.7512` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
