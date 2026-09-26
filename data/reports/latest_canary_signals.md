# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T21:22:26.619966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.2348` n `234`; crypto_major avg `0.1619` n `8`; equity avg `0.0064` n `141`; fx avg `0.0053` n `6`; index avg `-0.0001` n `26`; metal avg `0.0017` n `20`; unknown avg `0.8518` n `961`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.1504` n `234`; crypto_major avg `0.026` n `8`; equity avg `-0.0193` n `141`; fx avg `-0.007` n `6`; index avg `-0.0081` n `26`; metal avg `0.0009` n `20`; unknown avg `7.0987` n `959`
- 4h: commodity avg `0.0723` n `12`; crypto_alt avg `-1.2451` n `234`; crypto_major avg `-0.4776` n `8`; equity avg `-0.0631` n `141`; fx avg `-0.0025` n `6`; index avg `-0.0273` n `26`; metal avg `0.003` n `20`; unknown avg `0.8993` n `953`
- 24h: commodity avg `0.3464` n `12`; crypto_alt avg `1.3275` n `234`; crypto_major avg `-0.3355` n `8`; equity avg `0.0145` n `141`; fx avg `0.0189` n `6`; index avg `-0.0477` n `26`; metal avg `-0.0127` n `20`; unknown avg `4.4936` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
