# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T09:52:31.084119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `-0.0501` n `230`; crypto_major avg `-0.0196` n `8`; equity avg `-0.0682` n `113`; fx avg `0.0008` n `6`; index avg `-0.0261` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0324` n `786`
- 1h: commodity avg `-0.0495` n `12`; crypto_alt avg `0.3993` n `230`; crypto_major avg `0.4788` n `8`; equity avg `0.1075` n `113`; fx avg `-0.0346` n `6`; index avg `0.0227` n `25`; metal avg `0.1296` n `20`; unknown avg `0.0684` n `786`
- 4h: commodity avg `-0.1368` n `12`; crypto_alt avg `-0.2986` n `230`; crypto_major avg `0.3444` n `8`; equity avg `0.6214` n `113`; fx avg `-0.0265` n `6`; index avg `0.0904` n `25`; metal avg `0.2935` n `20`; unknown avg `-0.0869` n `770`
- 24h: commodity avg `-0.2035` n `12`; crypto_alt avg `-1.1984` n `230`; crypto_major avg `0.8208` n `8`; equity avg `2.5883` n `113`; fx avg `-0.0248` n `6`; index avg `0.259` n `25`; metal avg `0.2197` n `20`; unknown avg `-0.2177` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2328`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2224`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.22`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2011`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
