# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T15:22:31.243894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.059` n `12`; crypto_alt avg `0.0429` n `234`; crypto_major avg `0.0977` n `8`; equity avg `0.0319` n `141`; fx avg `-0.0034` n `6`; index avg `0.0035` n `26`; metal avg `0.002` n `20`; unknown avg `7.1457` n `962`
- 1h: commodity avg `-0.0593` n `12`; crypto_alt avg `-0.7448` n `234`; crypto_major avg `-0.5158` n `8`; equity avg `-0.0174` n `141`; fx avg `0.0057` n `6`; index avg `0.0105` n `26`; metal avg `-0.0026` n `20`; unknown avg `7.6251` n `960`
- 4h: commodity avg `-0.1002` n `12`; crypto_alt avg `-1.2429` n `234`; crypto_major avg `-0.9092` n `8`; equity avg `-0.0853` n `141`; fx avg `0.0055` n `6`; index avg `-0.0237` n `26`; metal avg `-0.0135` n `20`; unknown avg `13.5063` n `954`
- 24h: commodity avg `-0.0816` n `12`; crypto_alt avg `-1.3569` n `234`; crypto_major avg `-0.3617` n `8`; equity avg `0.1805` n `141`; fx avg `-0.0279` n `6`; index avg `0.0055` n `26`; metal avg `-0.0238` n `20`; unknown avg `233.2266` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
