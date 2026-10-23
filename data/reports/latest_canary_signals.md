# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T20:07:30.507193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `13`; crypto_alt avg `-0.0444` n `237`; crypto_major avg `0.0187` n `8`; equity avg `0.0785` n `152`; fx avg `-0.0168` n `6`; index avg `0.0104` n `26`; metal avg `-0.0218` n `20`; unknown avg `217.5484` n `1202`
- 1h: commodity avg `0.0901` n `13`; crypto_alt avg `-0.5024` n `237`; crypto_major avg `-0.2519` n `8`; equity avg `-0.094` n `152`; fx avg `-0.0163` n `6`; index avg `0.0061` n `26`; metal avg `-0.0274` n `20`; unknown avg `100.033` n `1200`
- 4h: commodity avg `0.2369` n `13`; crypto_alt avg `-1.209` n `237`; crypto_major avg `-0.8681` n `8`; equity avg `-0.7158` n `152`; fx avg `-0.0263` n `6`; index avg `-0.0985` n `26`; metal avg `-0.1273` n `20`; unknown avg `3.1343` n `1175`
- 24h: commodity avg `0.4524` n `13`; crypto_alt avg `0.216` n `237`; crypto_major avg `0.1944` n `8`; equity avg `0.8401` n `152`; fx avg `-0.0984` n `6`; index avg `0.0132` n `26`; metal avg `-0.1542` n `20`; unknown avg `-0.1728` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
