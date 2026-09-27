# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T04:37:31.149595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.271` n `234`; crypto_major avg `-0.2548` n `8`; equity avg `-0.0024` n `141`; fx avg `-0.0031` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0035` n `20`; unknown avg `103.1049` n `961`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `-0.3884` n `234`; crypto_major avg `-0.1911` n `8`; equity avg `0.0099` n `141`; fx avg `-0.0031` n `6`; index avg `0.0057` n `26`; metal avg `-0.0051` n `20`; unknown avg `58.6437` n `953`
- 4h: commodity avg `0.0498` n `12`; crypto_alt avg `-0.4429` n `234`; crypto_major avg `-0.2153` n `8`; equity avg `0.0472` n `141`; fx avg `-0.0124` n `6`; index avg `0.0105` n `26`; metal avg `-0.0104` n `20`; unknown avg `-0.024` n `947`
- 24h: commodity avg `-0.0207` n `12`; crypto_alt avg `0.5356` n `234`; crypto_major avg `-0.36` n `8`; equity avg `0.2809` n `141`; fx avg `-0.0009` n `6`; index avg `0.0079` n `26`; metal avg `-0.0108` n `20`; unknown avg `4.4539` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
