# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T18:41:15.775346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `12`; crypto_alt avg `-0.164` n `230`; crypto_major avg `-0.2582` n `8`; equity avg `-0.176` n `113`; fx avg `0.0034` n `6`; index avg `-0.0254` n `25`; metal avg `0.0401` n `20`; unknown avg `-0.1173` n `785`
- 1h: commodity avg `-0.0224` n `12`; crypto_alt avg `-0.1263` n `230`; crypto_major avg `-0.1348` n `8`; equity avg `-0.2118` n `113`; fx avg `0.0075` n `6`; index avg `-0.0529` n `25`; metal avg `-0.0409` n `20`; unknown avg `0.0471` n `785`
- 4h: commodity avg `0.1463` n `12`; crypto_alt avg `-1.1257` n `230`; crypto_major avg `-0.3425` n `8`; equity avg `-0.4653` n `113`; fx avg `0.0066` n `6`; index avg `-0.1403` n `25`; metal avg `-0.1812` n `20`; unknown avg `-0.1652` n `785`
- 24h: commodity avg `0.0671` n `12`; crypto_alt avg `-1.9428` n `230`; crypto_major avg `-0.1841` n `8`; equity avg `0.0115` n `113`; fx avg `-0.0524` n `6`; index avg `0.0284` n `25`; metal avg `-0.1557` n `20`; unknown avg `-0.2951` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
