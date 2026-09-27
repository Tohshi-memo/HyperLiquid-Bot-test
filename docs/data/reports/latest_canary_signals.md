# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T00:07:27.088117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.2692` n `234`; crypto_major avg `-0.1177` n `8`; equity avg `0.007` n `141`; fx avg `0.0008` n `6`; index avg `0.006` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.3402` n `953`
- 1h: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.0957` n `234`; crypto_major avg `0.0276` n `8`; equity avg `0.0269` n `141`; fx avg `-0.0034` n `6`; index avg `0.0093` n `26`; metal avg `0.0032` n `20`; unknown avg `1.9737` n `953`
- 4h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0249` n `234`; crypto_major avg `0.2336` n `8`; equity avg `0.0565` n `141`; fx avg `-0.016` n `6`; index avg `0.0035` n `26`; metal avg `0.0037` n `20`; unknown avg `8.0859` n `929`
- 24h: commodity avg `0.2904` n `12`; crypto_alt avg `0.394` n `234`; crypto_major avg `-0.7002` n `8`; equity avg `0.0271` n `141`; fx avg `0.0149` n `6`; index avg `-0.0511` n `26`; metal avg `-0.022` n `20`; unknown avg `3.9884` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
