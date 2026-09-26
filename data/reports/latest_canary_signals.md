# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T01:08:06.323498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `-0.0033` n `234`; crypto_major avg `0.0945` n `8`; equity avg `0.0074` n `141`; fx avg `-0.0059` n `6`; index avg `0.0088` n `26`; metal avg `0.0125` n `20`; unknown avg `0.4223` n `958`
- 1h: commodity avg `0.3647` n `12`; crypto_alt avg `-0.4012` n `234`; crypto_major avg `-0.1439` n `8`; equity avg `-0.2047` n `141`; fx avg `-0.0026` n `6`; index avg `-0.0636` n `26`; metal avg `-0.0198` n `20`; unknown avg `-0.0384` n `958`
- 4h: commodity avg `0.3912` n `12`; crypto_alt avg `0.7239` n `234`; crypto_major avg `0.57` n `8`; equity avg `-0.1256` n `141`; fx avg `-0.0072` n `6`; index avg `-0.0443` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.5359` n `926`
- 24h: commodity avg `0.0701` n `12`; crypto_alt avg `2.1788` n `234`; crypto_major avg `0.6796` n `8`; equity avg `-0.1832` n `141`; fx avg `-0.2257` n `6`; index avg `0.1853` n `26`; metal avg `0.142` n `20`; unknown avg `1125.579` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
