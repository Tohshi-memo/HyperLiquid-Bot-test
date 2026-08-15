# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T20:02:53.357027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0552` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `-0.0135` n `8`; equity avg `-0.0119` n `114`; fx avg `-0.0025` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0783` n `791`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `0.1323` n `8`; equity avg `0.035` n `114`; fx avg `-0.0016` n `6`; index avg `-0.0011` n `25`; metal avg `0.008` n `20`; unknown avg `-0.1227` n `791`
- 4h: commodity avg `0.0645` n `12`; crypto_alt avg `0.0067` n `230`; crypto_major avg `0.1405` n `8`; equity avg `0.0777` n `114`; fx avg `-0.0012` n `6`; index avg `0.002` n `25`; metal avg `0.0078` n `20`; unknown avg `0.0676` n `791`
- 24h: commodity avg `-0.0286` n `12`; crypto_alt avg `1.0028` n `230`; crypto_major avg `0.6344` n `8`; equity avg `0.2142` n `114`; fx avg `0.0181` n `6`; index avg `0.006` n `25`; metal avg `0.0531` n `20`; unknown avg `0.0997` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
