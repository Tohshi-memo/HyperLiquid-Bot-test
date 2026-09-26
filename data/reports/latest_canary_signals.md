# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T10:37:30.012439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `0.0338` n `234`; crypto_major avg `-0.0195` n `8`; equity avg `0.0077` n `141`; fx avg `-0.0013` n `6`; index avg `-0.0001` n `26`; metal avg `0.0023` n `20`; unknown avg `2.0514` n `961`
- 1h: commodity avg `0.0329` n `12`; crypto_alt avg `0.7118` n `234`; crypto_major avg `0.336` n `8`; equity avg `0.0456` n `141`; fx avg `0.0052` n `6`; index avg `-0.0047` n `26`; metal avg `0.0008` n `20`; unknown avg `1.073` n `959`
- 4h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.7643` n `234`; crypto_major avg `0.1873` n `8`; equity avg `0.0542` n `141`; fx avg `0.0279` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0107` n `20`; unknown avg `0.0757` n `943`
- 24h: commodity avg `0.1329` n `12`; crypto_alt avg `2.3379` n `234`; crypto_major avg `-0.3189` n `8`; equity avg `-0.8804` n `141`; fx avg `-0.0378` n `6`; index avg `0.0133` n `26`; metal avg `-0.0757` n `20`; unknown avg `1119.7924` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
