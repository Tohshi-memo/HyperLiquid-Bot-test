# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T03:37:26.352567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `0.356` n `234`; crypto_major avg `0.0477` n `8`; equity avg `-0.003` n `141`; fx avg `-0.0038` n `6`; index avg `-0.0002` n `26`; metal avg `0.0001` n `20`; unknown avg `0.265` n `961`
- 1h: commodity avg `-0.0232` n `12`; crypto_alt avg `-0.1635` n `234`; crypto_major avg `-0.225` n `8`; equity avg `-0.0044` n `141`; fx avg `0.0039` n `6`; index avg `0.0062` n `26`; metal avg `-0.0031` n `20`; unknown avg `-0.0066` n `959`
- 4h: commodity avg `0.2911` n `12`; crypto_alt avg `-0.3299` n `234`; crypto_major avg `-0.3584` n `8`; equity avg `-0.1544` n `141`; fx avg `0.0028` n `6`; index avg `-0.0408` n `26`; metal avg `-0.0115` n `20`; unknown avg `0.0621` n `952`
- 24h: commodity avg `0.0604` n `12`; crypto_alt avg `3.518` n `234`; crypto_major avg `1.2277` n `8`; equity avg `-0.3816` n `141`; fx avg `-0.1086` n `6`; index avg `0.1332` n `26`; metal avg `0.2116` n `20`; unknown avg `1126.3973` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
