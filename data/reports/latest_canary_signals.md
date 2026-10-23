# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T19:52:32.906114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.2436` n `237`; crypto_major avg `-0.1157` n `8`; equity avg `-0.1254` n `152`; fx avg `0.0011` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0088` n `20`; unknown avg `111.264` n `1230`
- 1h: commodity avg `0.0533` n `13`; crypto_alt avg `-0.784` n `237`; crypto_major avg `-0.438` n `8`; equity avg `-0.418` n `152`; fx avg `0.0058` n `6`; index avg `-0.0242` n `26`; metal avg `-0.015` n `20`; unknown avg `179.7816` n `1228`
- 4h: commodity avg `0.159` n `13`; crypto_alt avg `-0.8569` n `237`; crypto_major avg `-0.7133` n `8`; equity avg `-0.6995` n `152`; fx avg `-0.0156` n `6`; index avg `-0.0909` n `26`; metal avg `-0.1196` n `20`; unknown avg `7.3955` n `1197`
- 24h: commodity avg `0.3999` n `13`; crypto_alt avg `0.3221` n `237`; crypto_major avg `0.1453` n `8`; equity avg `0.8804` n `152`; fx avg `-0.086` n `6`; index avg `0.033` n `26`; metal avg `-0.1292` n `20`; unknown avg `0.9421` n `1034`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
