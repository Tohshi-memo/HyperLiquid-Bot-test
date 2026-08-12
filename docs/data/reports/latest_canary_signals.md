# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T09:07:26.942274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0424` n `12`; crypto_alt avg `0.0764` n `230`; crypto_major avg `0.0368` n `8`; equity avg `0.069` n `113`; fx avg `0.0002` n `6`; index avg `0.0149` n `25`; metal avg `0.0285` n `20`; unknown avg `0.0232` n `786`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.3246` n `230`; crypto_major avg `-0.1173` n `8`; equity avg `0.2104` n `113`; fx avg `-0.0028` n `6`; index avg `0.0511` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.1188` n `786`
- 4h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.6573` n `230`; crypto_major avg `0.0183` n `8`; equity avg `0.524` n `113`; fx avg `0.0106` n `6`; index avg `0.1031` n `25`; metal avg `0.1008` n `20`; unknown avg `-0.1494` n `770`
- 24h: commodity avg `-0.1708` n `12`; crypto_alt avg `-1.3597` n `230`; crypto_major avg `0.5566` n `8`; equity avg `2.8578` n `113`; fx avg `0.0061` n `6`; index avg `0.2986` n `25`; metal avg `0.1906` n `20`; unknown avg `-0.2308` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.226`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
