# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T22:51:33.465088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `12`; crypto_alt avg `-0.0694` n `234`; crypto_major avg `-0.3763` n `8`; equity avg `-0.0142` n `140`; fx avg `-0.0002` n `6`; index avg `-0.0006` n `26`; metal avg `0.0407` n `20`; unknown avg `0.485` n `944`
- 1h: commodity avg `0.0081` n `12`; crypto_alt avg `0.2677` n `234`; crypto_major avg `0.0211` n `8`; equity avg `0.1052` n `140`; fx avg `-0.0113` n `6`; index avg `0.0471` n `26`; metal avg `0.1162` n `20`; unknown avg `0.5677` n `942`
- 4h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.4257` n `234`; crypto_major avg `0.599` n `8`; equity avg `0.0387` n `140`; fx avg `-0.0154` n `6`; index avg `0.0038` n `26`; metal avg `0.062` n `20`; unknown avg `-0.1427` n `852`
- 24h: commodity avg `-0.69` n `12`; crypto_alt avg `3.7517` n `234`; crypto_major avg `5.7223` n `8`; equity avg `2.6715` n `140`; fx avg `-0.1434` n `6`; index avg `0.5765` n `26`; metal avg `0.0756` n `20`; unknown avg `6.8039` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
