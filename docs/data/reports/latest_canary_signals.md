# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T01:52:35.182605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0383` n `12`; crypto_alt avg `0.451` n `230`; crypto_major avg `0.5998` n `8`; equity avg `0.1445` n `112`; fx avg `0.0213` n `6`; index avg `0.0314` n `25`; metal avg `0.071` n `20`; unknown avg `0.6631` n `785`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.3345` n `230`; crypto_major avg `0.4697` n `8`; equity avg `0.0158` n `112`; fx avg `0.0614` n `6`; index avg `0.0554` n `25`; metal avg `-0.062` n `20`; unknown avg `0.1235` n `785`
- 4h: commodity avg `0.24` n `12`; crypto_alt avg `-0.3228` n `230`; crypto_major avg `-0.2416` n `8`; equity avg `-0.3018` n `112`; fx avg `0.1335` n `6`; index avg `0.0187` n `25`; metal avg `-0.2141` n `20`; unknown avg `-0.0698` n `785`
- 24h: commodity avg `0.434` n `12`; crypto_alt avg `1.2301` n `230`; crypto_major avg `0.29` n `8`; equity avg `-0.0452` n `112`; fx avg `0.1157` n `6`; index avg `0.0552` n `25`; metal avg `-0.2074` n `20`; unknown avg `-0.2833` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
