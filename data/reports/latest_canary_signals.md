# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T14:52:25.764173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `0.3524` n `234`; crypto_major avg `0.0662` n `8`; equity avg `0.0418` n `141`; fx avg `0.0` n `6`; index avg `0.0023` n `26`; metal avg `0.0005` n `20`; unknown avg `18.0064` n `961`
- 1h: commodity avg `0.0313` n `12`; crypto_alt avg `0.6293` n `234`; crypto_major avg `0.301` n `8`; equity avg `0.0721` n `141`; fx avg `0.0019` n `6`; index avg `0.0094` n `26`; metal avg `0.0042` n `20`; unknown avg `16.3811` n `959`
- 4h: commodity avg `0.073` n `12`; crypto_alt avg `0.4831` n `234`; crypto_major avg `0.0163` n `8`; equity avg `0.0961` n `141`; fx avg `0.0213` n `6`; index avg `0.0056` n `26`; metal avg `0.0046` n `20`; unknown avg `2.1978` n `949`
- 24h: commodity avg `0.1984` n `12`; crypto_alt avg `3.3329` n `234`; crypto_major avg `0.3148` n `8`; equity avg `0.4143` n `141`; fx avg `-0.0058` n `6`; index avg `0.1381` n `26`; metal avg `0.1563` n `20`; unknown avg `1.555` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
