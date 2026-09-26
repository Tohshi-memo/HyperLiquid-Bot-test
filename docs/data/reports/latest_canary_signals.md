# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T01:22:27.938445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.2427` n `234`; crypto_major avg `0.149` n `8`; equity avg `0.0012` n `141`; fx avg `0.0009` n `6`; index avg `-0.003` n `26`; metal avg `-0.0082` n `20`; unknown avg `0.6291` n `960`
- 1h: commodity avg `0.3556` n `12`; crypto_alt avg `-0.3979` n `234`; crypto_major avg `-0.0521` n `8`; equity avg `-0.1972` n `141`; fx avg `-0.0061` n `6`; index avg `-0.068` n `26`; metal avg `-0.0282` n `20`; unknown avg `0.5536` n `958`
- 4h: commodity avg `0.3828` n `12`; crypto_alt avg `1.134` n `234`; crypto_major avg `0.6668` n `8`; equity avg `-0.1214` n `141`; fx avg `-0.0042` n `6`; index avg `-0.0499` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.6603` n `926`
- 24h: commodity avg `0.0874` n `12`; crypto_alt avg `2.5747` n `234`; crypto_major avg `0.9605` n `8`; equity avg `-0.4391` n `141`; fx avg `-0.2022` n `6`; index avg `0.1251` n `26`; metal avg `0.0556` n `20`; unknown avg `1125.7262` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
