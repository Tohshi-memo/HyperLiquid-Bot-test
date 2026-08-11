# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T10:37:28.368641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.096` n `12`; crypto_alt avg `0.1256` n `230`; crypto_major avg `0.0821` n `8`; equity avg `0.1076` n `113`; fx avg `-0.0123` n `6`; index avg `0.0265` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.0074` n `785`
- 1h: commodity avg `-0.1519` n `12`; crypto_alt avg `-0.0578` n `230`; crypto_major avg `0.051` n `8`; equity avg `0.2181` n `113`; fx avg `-0.0322` n `6`; index avg `0.0371` n `25`; metal avg `0.045` n `20`; unknown avg `-0.0389` n `785`
- 4h: commodity avg `-0.0593` n `12`; crypto_alt avg `-0.2302` n `230`; crypto_major avg `0.2767` n `8`; equity avg `0.1235` n `113`; fx avg `-0.0464` n `6`; index avg `0.0565` n `25`; metal avg `0.219` n `20`; unknown avg `0.0682` n `785`
- 24h: commodity avg `0.8397` n `12`; crypto_alt avg `-1.1616` n `230`; crypto_major avg `-0.5282` n `8`; equity avg `-1.1659` n `113`; fx avg `-0.0065` n `6`; index avg `0.0285` n `25`; metal avg `0.3958` n `20`; unknown avg `0.103` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
