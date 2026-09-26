# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T21:04:41.564714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `0.477` n `234`; crypto_major avg `0.2616` n `8`; equity avg `0.0342` n `141`; fx avg `-0.0068` n `6`; index avg `0.0004` n `26`; metal avg `0.0039` n `20`; unknown avg `5.8047` n `959`
- 1h: commodity avg `0.015` n `12`; crypto_alt avg `-0.6236` n `234`; crypto_major avg `-0.2184` n `8`; equity avg `-0.0527` n `141`; fx avg `-0.0147` n `6`; index avg `-0.0096` n `26`; metal avg `0.0022` n `20`; unknown avg `7.486` n `959`
- 4h: commodity avg `0.0557` n `12`; crypto_alt avg `-1.6385` n `234`; crypto_major avg `-0.6983` n `8`; equity avg `-0.0925` n `141`; fx avg `-0.0129` n `6`; index avg `-0.0289` n `26`; metal avg `0.0028` n `20`; unknown avg `19.6247` n `953`
- 24h: commodity avg `0.322` n `12`; crypto_alt avg `0.9215` n `234`; crypto_major avg `-0.4428` n `8`; equity avg `-0.0029` n `141`; fx avg `0.0117` n `6`; index avg `-0.0448` n `26`; metal avg `-0.0143` n `20`; unknown avg `4.239` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
