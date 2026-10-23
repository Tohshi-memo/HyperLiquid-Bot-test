# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T16:37:37.294759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0447` n `13`; crypto_alt avg `0.0938` n `237`; crypto_major avg `0.1528` n `8`; equity avg `0.0488` n `152`; fx avg `0.0031` n `6`; index avg `-0.0113` n `26`; metal avg `-0.031` n `20`; unknown avg `0.3192` n `1215`
- 1h: commodity avg `0.1133` n `13`; crypto_alt avg `0.5774` n `237`; crypto_major avg `0.2705` n `8`; equity avg `0.0743` n `152`; fx avg `0.0024` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.139` n `1207`
- 4h: commodity avg `0.2351` n `13`; crypto_alt avg `0.0779` n `237`; crypto_major avg `0.1065` n `8`; equity avg `0.5895` n `152`; fx avg `0.0548` n `6`; index avg `0.1299` n `26`; metal avg `-0.0111` n `20`; unknown avg `-0.2814` n `1159`
- 24h: commodity avg `0.5126` n `13`; crypto_alt avg `1.114` n `237`; crypto_major avg `0.556` n `8`; equity avg `0.8755` n `152`; fx avg `-0.0812` n `6`; index avg `0.0157` n `26`; metal avg `-0.1538` n `20`; unknown avg `-0.7012` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
