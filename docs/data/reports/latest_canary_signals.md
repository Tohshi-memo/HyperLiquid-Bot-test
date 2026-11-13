# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T01:37:28.750105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0797` n `13`; crypto_alt avg `0.0662` n `239`; crypto_major avg `0.0525` n `8`; equity avg `-0.1006` n `162`; fx avg `-0.0008` n `6`; index avg `-0.0114` n `27`; metal avg `0.0245` n `20`; unknown avg `2.9231` n `1262`
- 1h: commodity avg `-0.064` n `13`; crypto_alt avg `0.2536` n `239`; crypto_major avg `0.1419` n `8`; equity avg `0.2645` n `162`; fx avg `-0.0416` n `6`; index avg `0.0551` n `27`; metal avg `0.2299` n `20`; unknown avg `4.2746` n `1259`
- 4h: commodity avg `-0.1475` n `13`; crypto_alt avg `0.0365` n `239`; crypto_major avg `-0.1454` n `8`; equity avg `0.667` n `162`; fx avg `-0.0432` n `6`; index avg `0.1221` n `27`; metal avg `0.3382` n `20`; unknown avg `12.5848` n `1213`
- 24h: commodity avg `0.8705` n `13`; crypto_alt avg `-0.5489` n `239`; crypto_major avg `-1.548` n `8`; equity avg `-0.2106` n `162`; fx avg `-0.1367` n `6`; index avg `0.1411` n `27`; metal avg `-0.451` n `20`; unknown avg `73.7464` n `1121`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
