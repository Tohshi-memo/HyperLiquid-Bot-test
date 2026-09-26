# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T16:52:26.997952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.1192` n `234`; crypto_major avg `-0.0256` n `8`; equity avg `-0.0049` n `141`; fx avg `-0.0031` n `6`; index avg `0.0012` n `26`; metal avg `-0.0004` n `20`; unknown avg `8.5888` n `961`
- 1h: commodity avg `0.016` n `12`; crypto_alt avg `-0.0087` n `234`; crypto_major avg `-0.1009` n `8`; equity avg `0.0315` n `141`; fx avg `0.0022` n `6`; index avg `0.0049` n `26`; metal avg `0.0046` n `20`; unknown avg `4.4404` n `945`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `1.2473` n `234`; crypto_major avg `0.3194` n `8`; equity avg `0.1174` n `141`; fx avg `-0.0075` n `6`; index avg `0.0282` n `26`; metal avg `-0.0018` n `20`; unknown avg `7.2297` n `945`
- 24h: commodity avg `0.4101` n `12`; crypto_alt avg `3.0268` n `234`; crypto_major avg `0.095` n `8`; equity avg `-0.1025` n `141`; fx avg `0.0084` n `6`; index avg `0.0061` n `26`; metal avg `-0.0081` n `20`; unknown avg `0.6604` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
