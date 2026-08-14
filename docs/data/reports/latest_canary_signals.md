# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T18:07:29.497763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `0.0018` n `230`; crypto_major avg `-0.1029` n `8`; equity avg `0.0454` n `114`; fx avg `0.0057` n `6`; index avg `0.0139` n `25`; metal avg `0.0094` n `20`; unknown avg `0.0659` n `791`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `-0.1728` n `8`; equity avg `-0.0013` n `114`; fx avg `-0.0049` n `6`; index avg `0.0084` n `25`; metal avg `-0.0297` n `20`; unknown avg `1.277` n `791`
- 4h: commodity avg `0.0658` n `12`; crypto_alt avg `0.7472` n `230`; crypto_major avg `0.1746` n `8`; equity avg `-0.9482` n `114`; fx avg `0.0467` n `6`; index avg `-0.1821` n `25`; metal avg `-0.0947` n `20`; unknown avg `37.8637` n `786`
- 24h: commodity avg `0.1914` n `12`; crypto_alt avg `0.4996` n `230`; crypto_major avg `-0.7099` n `8`; equity avg `-0.5019` n `114`; fx avg `0.0712` n `6`; index avg `-0.0939` n `25`; metal avg `0.1433` n `20`; unknown avg `0.1449` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
