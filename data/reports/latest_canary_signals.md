# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T12:52:35.241447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0607` n `12`; crypto_alt avg `-0.0944` n `234`; crypto_major avg `-0.1589` n `8`; equity avg `-0.0312` n `141`; fx avg `-0.0087` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0658` n `20`; unknown avg `0.0804` n `944`
- 1h: commodity avg `0.1216` n `12`; crypto_alt avg `-0.1746` n `234`; crypto_major avg `-0.0275` n `8`; equity avg `-0.1854` n `141`; fx avg `0.0398` n `6`; index avg `-0.0415` n `26`; metal avg `-0.0498` n `20`; unknown avg `4.0478` n `936`
- 4h: commodity avg `0.0251` n `12`; crypto_alt avg `0.9942` n `234`; crypto_major avg `1.3531` n `8`; equity avg `-0.0812` n `141`; fx avg `-0.0074` n `6`; index avg `-0.0298` n `26`; metal avg `0.0237` n `20`; unknown avg `4.6377` n `936`
- 24h: commodity avg `0.1389` n `12`; crypto_alt avg `5.3221` n `234`; crypto_major avg `3.534` n `8`; equity avg `1.85` n `141`; fx avg `-0.1759` n `6`; index avg `0.2588` n `26`; metal avg `0.16` n `20`; unknown avg `14.4124` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
