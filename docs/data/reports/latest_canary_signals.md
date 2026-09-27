# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T17:22:34.103745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.1535` n `234`; crypto_major avg `0.112` n `8`; equity avg `0.0222` n `141`; fx avg `-0.0061` n `6`; index avg `0.003` n `26`; metal avg `0.0006` n `20`; unknown avg `0.5391` n `962`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.1534` n `234`; crypto_major avg `-0.0817` n `8`; equity avg `0.0183` n `141`; fx avg `-0.0075` n `6`; index avg `-0.0161` n `26`; metal avg `0.0057` n `20`; unknown avg `3.6017` n `960`
- 4h: commodity avg `-0.1657` n `12`; crypto_alt avg `0.1616` n `234`; crypto_major avg `-0.5045` n `8`; equity avg `0.0102` n `141`; fx avg `0.0026` n `6`; index avg `-0.0086` n `26`; metal avg `0.0106` n `20`; unknown avg `7.3293` n `954`
- 24h: commodity avg `-0.1095` n `12`; crypto_alt avg `-0.4199` n `234`; crypto_major avg `-0.162` n `8`; equity avg `0.2531` n `141`; fx avg `-0.0126` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0094` n `20`; unknown avg `7.1573` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
