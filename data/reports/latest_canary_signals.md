# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T20:52:27.692077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0809` n `12`; crypto_alt avg `0.2278` n `234`; crypto_major avg `0.1346` n `8`; equity avg `0.1001` n `141`; fx avg `-0.0017` n `6`; index avg `0.0216` n `26`; metal avg `0.0406` n `20`; unknown avg `3.6092` n `946`
- 1h: commodity avg `-0.2157` n `12`; crypto_alt avg `-0.2463` n `234`; crypto_major avg `-0.2221` n `8`; equity avg `-0.1137` n `141`; fx avg `-0.0125` n `6`; index avg `-0.0339` n `26`; metal avg `-0.0456` n `20`; unknown avg `5.039` n `898`
- 4h: commodity avg `0.073` n `12`; crypto_alt avg `-0.065` n `234`; crypto_major avg `-0.0326` n `8`; equity avg `-0.1701` n `141`; fx avg `0.0028` n `6`; index avg `-0.0829` n `26`; metal avg `-0.0464` n `20`; unknown avg `7.055` n `869`
- 24h: commodity avg `0.7578` n `12`; crypto_alt avg `4.305` n `234`; crypto_major avg `1.7428` n `8`; equity avg `-0.2703` n `141`; fx avg `0.0373` n `6`; index avg `-0.1179` n `26`; metal avg `-0.116` n `20`; unknown avg `15.5126` n `849`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
