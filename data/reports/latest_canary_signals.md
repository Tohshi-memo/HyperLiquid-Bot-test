# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T20:07:27.559305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0517` n `12`; crypto_alt avg `0.02` n `234`; crypto_major avg `-0.0851` n `8`; equity avg `-0.0797` n `141`; fx avg `-0.0022` n `6`; index avg `-0.018` n `26`; metal avg `-0.012` n `20`; unknown avg `274.0566` n `916`
- 1h: commodity avg `0.0662` n `12`; crypto_alt avg `0.021` n `234`; crypto_major avg `-0.0468` n `8`; equity avg `-0.1705` n `141`; fx avg `0.0116` n `6`; index avg `0.0047` n `26`; metal avg `-0.0369` n `20`; unknown avg `163.135` n `916`
- 4h: commodity avg `0.1587` n `12`; crypto_alt avg `0.7651` n `234`; crypto_major avg `0.0645` n `8`; equity avg `-0.3529` n `141`; fx avg `0.0161` n `6`; index avg `-0.0133` n `26`; metal avg `-0.0573` n `20`; unknown avg `3.1451` n `914`
- 24h: commodity avg `-0.7718` n `12`; crypto_alt avg `1.9972` n `234`; crypto_major avg `0.5361` n `8`; equity avg `0.11` n `141`; fx avg `-0.2495` n `6`; index avg `0.2345` n `26`; metal avg `0.1394` n `20`; unknown avg `1601.1111` n `804`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
