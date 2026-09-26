# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T12:22:26.756403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.024` n `12`; crypto_alt avg `0.0673` n `234`; crypto_major avg `-0.0273` n `8`; equity avg `0.0117` n `141`; fx avg `-0.0016` n `6`; index avg `-0.0` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.8848` n `961`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `-0.0253` n `234`; crypto_major avg `0.0124` n `8`; equity avg `0.0212` n `141`; fx avg `0.0158` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0002` n `20`; unknown avg `3.0205` n `949`
- 4h: commodity avg `0.0303` n `12`; crypto_alt avg `0.8015` n `234`; crypto_major avg `0.162` n `8`; equity avg `0.0587` n `141`; fx avg `0.015` n `6`; index avg `-0.0029` n `26`; metal avg `0.0028` n `20`; unknown avg `0.8636` n `949`
- 24h: commodity avg `0.1495` n `12`; crypto_alt avg `2.4788` n `234`; crypto_major avg `-0.483` n `8`; equity avg `-0.7819` n `141`; fx avg `-0.0338` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0823` n `20`; unknown avg `1122.3313` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
