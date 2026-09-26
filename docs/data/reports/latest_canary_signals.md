# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T17:22:24.895861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.161` n `234`; crypto_major avg `-0.061` n `8`; equity avg `-0.0151` n `141`; fx avg `-0.0052` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0008` n `20`; unknown avg `18.9508` n `961`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.5007` n `234`; crypto_major avg `-0.1937` n `8`; equity avg `-0.0257` n `141`; fx avg `-0.0069` n `6`; index avg `0.0026` n `26`; metal avg `0.0059` n `20`; unknown avg `11.6474` n `959`
- 4h: commodity avg `0.0146` n `12`; crypto_alt avg `0.9601` n `234`; crypto_major avg `0.2209` n `8`; equity avg `0.0785` n `141`; fx avg `-0.0141` n `6`; index avg `0.023` n `26`; metal avg `0.003` n `20`; unknown avg `19.7773` n `945`
- 24h: commodity avg `0.4437` n `12`; crypto_alt avg `2.6878` n `234`; crypto_major avg `-0.0016` n `8`; equity avg `-0.1373` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0279` n `20`; unknown avg `4.5192` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
