# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T18:52:30.966179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.2415` n `234`; crypto_major avg `-0.151` n `8`; equity avg `-0.0191` n `141`; fx avg `0.0036` n `6`; index avg `0.0011` n `26`; metal avg `-0.0007` n `20`; unknown avg `0.3049` n `961`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.5401` n `234`; crypto_major avg `-0.3485` n `8`; equity avg `-0.0435` n `141`; fx avg `-0.0031` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0052` n `20`; unknown avg `-0.1501` n `959`
- 4h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.5646` n `234`; crypto_major avg `-0.4845` n `8`; equity avg `-0.0471` n `141`; fx avg `-0.006` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0108` n `20`; unknown avg `4.2014` n `945`
- 24h: commodity avg `0.4856` n `12`; crypto_alt avg `1.4105` n `234`; crypto_major avg `-0.7214` n `8`; equity avg `-0.0736` n `141`; fx avg `0.0196` n `6`; index avg `-0.0233` n `26`; metal avg `-0.0803` n `20`; unknown avg `3.2412` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
