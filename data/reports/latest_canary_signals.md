# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T09:21:47.842910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `0.1161` n `230`; crypto_major avg `0.0143` n `8`; equity avg `-0.1168` n `113`; fx avg `-0.0062` n `6`; index avg `-0.0173` n `25`; metal avg `0.0531` n `20`; unknown avg `-0.033` n `787`
- 1h: commodity avg `-0.1554` n `12`; crypto_alt avg `0.0562` n `230`; crypto_major avg `-0.1645` n `8`; equity avg `-0.0253` n `113`; fx avg `-0.0014` n `6`; index avg `-0.0128` n `25`; metal avg `0.073` n `20`; unknown avg `0.5034` n `787`
- 4h: commodity avg `-0.3409` n `12`; crypto_alt avg `-0.0168` n `230`; crypto_major avg `-0.1765` n `8`; equity avg `-0.8923` n `113`; fx avg `0.0749` n `6`; index avg `-0.0991` n `25`; metal avg `-0.2735` n `20`; unknown avg `-0.1214` n `755`
- 24h: commodity avg `-0.3934` n `12`; crypto_alt avg `-0.4408` n `230`; crypto_major avg `-0.006` n `8`; equity avg `1.1595` n `113`; fx avg `0.0256` n `6`; index avg `0.1151` n `25`; metal avg `-0.6123` n `20`; unknown avg `0.7145` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2436`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
