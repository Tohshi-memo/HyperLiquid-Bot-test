# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T19:37:31.763051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `0.1453` n `234`; crypto_major avg `0.0438` n `8`; equity avg `0.0874` n `140`; fx avg `0.0056` n `6`; index avg `0.0156` n `26`; metal avg `0.0418` n `20`; unknown avg `15.0171` n `946`
- 1h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.3095` n `234`; crypto_major avg `0.3627` n `8`; equity avg `0.1721` n `140`; fx avg `0.0074` n `6`; index avg `0.0504` n `26`; metal avg `0.0469` n `20`; unknown avg `15.403` n `940`
- 4h: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.0974` n `234`; crypto_major avg `0.6552` n `8`; equity avg `0.4865` n `140`; fx avg `-0.0005` n `6`; index avg `0.1399` n `26`; metal avg `0.0361` n `20`; unknown avg `12.4021` n `928`
- 24h: commodity avg `-1.0632` n `12`; crypto_alt avg `3.7845` n `234`; crypto_major avg `5.1546` n `8`; equity avg `3.0491` n `140`; fx avg `-0.0677` n `6`; index avg `0.6769` n `26`; metal avg `0.0965` n `20`; unknown avg `8.4351` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
