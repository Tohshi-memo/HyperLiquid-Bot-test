# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T12:52:33.398867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.0326` n `234`; crypto_major avg `-0.0035` n `8`; equity avg `-0.0018` n `141`; fx avg `0.003` n `6`; index avg `-0.0078` n `26`; metal avg `0.0044` n `20`; unknown avg `0.2966` n `961`
- 1h: commodity avg `0.0348` n `12`; crypto_alt avg `-0.3179` n `234`; crypto_major avg `-0.2148` n `8`; equity avg `-0.0128` n `141`; fx avg `-0.0082` n `6`; index avg `-0.0136` n `26`; metal avg `0.0012` n `20`; unknown avg `2.4961` n `949`
- 4h: commodity avg `0.0306` n `12`; crypto_alt avg `0.1349` n `234`; crypto_major avg `-0.1098` n `8`; equity avg `0.0293` n `141`; fx avg `0.0481` n `6`; index avg `-0.0151` n `26`; metal avg `0.0002` n `20`; unknown avg `2.5793` n `949`
- 24h: commodity avg `0.1324` n `12`; crypto_alt avg `1.6461` n `234`; crypto_major avg `-1.0048` n `8`; equity avg `-0.7619` n `141`; fx avg `-0.0462` n `6`; index avg `0.0121` n `26`; metal avg `0.0002` n `20`; unknown avg `1121.4789` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
