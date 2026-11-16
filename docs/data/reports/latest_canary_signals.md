# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T16:37:38.204761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `13`; crypto_alt avg `-0.0674` n `239`; crypto_major avg `-0.0794` n `8`; equity avg `-0.1834` n `162`; fx avg `0.0065` n `6`; index avg `-0.0253` n `27`; metal avg `0.0005` n `20`; unknown avg `0.0457` n `1265`
- 1h: commodity avg `-0.1117` n `13`; crypto_alt avg `0.8666` n `239`; crypto_major avg `0.903` n `8`; equity avg `0.9875` n `162`; fx avg `0.0013` n `6`; index avg `0.1129` n `27`; metal avg `-0.0121` n `20`; unknown avg `0.328` n `1241`
- 4h: commodity avg `-0.403` n `13`; crypto_alt avg `1.0776` n `239`; crypto_major avg `0.9833` n `8`; equity avg `-0.2012` n `162`; fx avg `0.0111` n `6`; index avg `0.0348` n `27`; metal avg `-0.2455` n `20`; unknown avg `13.1308` n `1227`
- 24h: commodity avg `-0.8524` n `13`; crypto_alt avg `-0.08` n `239`; crypto_major avg `0.1029` n `8`; equity avg `-2.0102` n `162`; fx avg `-0.033` n `6`; index avg `-0.1467` n `27`; metal avg `-0.2017` n `20`; unknown avg `253.1219` n `1037`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
