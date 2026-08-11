# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T13:07:34.454404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1955` n `12`; crypto_alt avg `0.0933` n `230`; crypto_major avg `0.0265` n `8`; equity avg `0.134` n `113`; fx avg `0.001` n `6`; index avg `0.0161` n `25`; metal avg `0.0307` n `20`; unknown avg `0.035` n `785`
- 1h: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.1476` n `230`; crypto_major avg `-0.1518` n `8`; equity avg `0.0834` n `113`; fx avg `0.0166` n `6`; index avg `0.0136` n `25`; metal avg `-0.0829` n `20`; unknown avg `-0.0121` n `785`
- 4h: commodity avg `-0.4854` n `12`; crypto_alt avg `-0.0466` n `230`; crypto_major avg `0.3026` n `8`; equity avg `0.8191` n `113`; fx avg `-0.0471` n `6`; index avg `0.1368` n `25`; metal avg `0.0425` n `20`; unknown avg `-0.1566` n `785`
- 24h: commodity avg `0.4532` n `12`; crypto_alt avg `-1.368` n `230`; crypto_major avg `-0.2309` n `8`; equity avg `-0.1812` n `113`; fx avg `-0.0315` n `6`; index avg `0.1648` n `25`; metal avg `0.3768` n `20`; unknown avg `0.0539` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
