# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T14:37:54.750657+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.1849` n `230`; crypto_major avg `0.197` n `8`; equity avg `0.1395` n `113`; fx avg `-0.0009` n `6`; index avg `0.0489` n `25`; metal avg `0.0237` n `20`; unknown avg `-0.039` n `787`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `0.3475` n `230`; crypto_major avg `0.2289` n `8`; equity avg `0.8161` n `113`; fx avg `-0.0173` n `6`; index avg `0.1924` n `25`; metal avg `-0.0176` n `20`; unknown avg `0.015` n `787`
- 4h: commodity avg `-0.2162` n `12`; crypto_alt avg `0.4056` n `230`; crypto_major avg `0.5113` n `8`; equity avg `1.9365` n `113`; fx avg `-0.0489` n `6`; index avg `0.3224` n `25`; metal avg `-0.1311` n `20`; unknown avg `0.14` n `787`
- 24h: commodity avg `-0.5926` n `12`; crypto_alt avg `0.2386` n `230`; crypto_major avg `0.7208` n `8`; equity avg `2.0938` n `113`; fx avg `-0.0083` n `6`; index avg `0.3142` n `25`; metal avg `-0.5997` n `20`; unknown avg `0.3117` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2284`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
