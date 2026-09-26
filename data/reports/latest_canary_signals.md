# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T11:07:30.000887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.0912` n `234`; crypto_major avg `-0.0753` n `8`; equity avg `0.0058` n `141`; fx avg `0.0094` n `6`; index avg `0.002` n `26`; metal avg `-0.0055` n `20`; unknown avg `3.2495` n `959`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `0.5459` n `234`; crypto_major avg `0.1742` n `8`; equity avg `0.0412` n `141`; fx avg `0.0128` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0003` n `20`; unknown avg `3.3045` n `959`
- 4h: commodity avg `0.0004` n `12`; crypto_alt avg `0.6715` n `234`; crypto_major avg `-0.0036` n `8`; equity avg `0.0421` n `141`; fx avg `0.0232` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0158` n `20`; unknown avg `2.7837` n `943`
- 24h: commodity avg `0.1149` n `12`; crypto_alt avg `1.8865` n `234`; crypto_major avg `-1.0432` n `8`; equity avg `-0.9058` n `141`; fx avg `-0.0242` n `6`; index avg `0.003` n `26`; metal avg `-0.1518` n `20`; unknown avg `1122.6377` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
