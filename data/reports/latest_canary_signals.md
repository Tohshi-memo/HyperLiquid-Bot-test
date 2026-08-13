# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T07:52:31.180928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0367` n `12`; crypto_alt avg `-0.1233` n `230`; crypto_major avg `-0.0671` n `8`; equity avg `0.0452` n `113`; fx avg `0.0122` n `6`; index avg `0.0001` n `25`; metal avg `-0.0519` n `20`; unknown avg `0.2584` n `787`
- 1h: commodity avg `-0.1613` n `12`; crypto_alt avg `-0.0441` n `230`; crypto_major avg `0.0451` n `8`; equity avg `-0.0796` n `113`; fx avg `-0.0079` n `6`; index avg `-0.0056` n `25`; metal avg `-0.1266` n `20`; unknown avg `0.3125` n `787`
- 4h: commodity avg `-0.0585` n `12`; crypto_alt avg `0.0678` n `230`; crypto_major avg `0.417` n `8`; equity avg `-0.4467` n `113`; fx avg `0.0691` n `6`; index avg `-0.0588` n `25`; metal avg `-0.3173` n `20`; unknown avg `0.3225` n `755`
- 24h: commodity avg `-0.3068` n `12`; crypto_alt avg `-0.5096` n `230`; crypto_major avg `0.4139` n `8`; equity avg `1.8694` n `113`; fx avg `0.0111` n `6`; index avg `0.2492` n `25`; metal avg `-0.5286` n `20`; unknown avg `0.3511` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2484`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
