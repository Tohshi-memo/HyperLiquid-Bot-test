# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T03:37:29.327294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `12`; crypto_alt avg `-0.1384` n `230`; crypto_major avg `-0.1461` n `8`; equity avg `0.0071` n `113`; fx avg `0.0004` n `6`; index avg `-0.0046` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.0873` n `787`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.2334` n `230`; crypto_major avg `-0.2093` n `8`; equity avg `-0.0344` n `113`; fx avg `-0.0057` n `6`; index avg `-0.0083` n `25`; metal avg `0.0239` n `20`; unknown avg `-0.2242` n `787`
- 4h: commodity avg `0.0562` n `12`; crypto_alt avg `-0.2849` n `230`; crypto_major avg `-0.1974` n `8`; equity avg `-0.3293` n `113`; fx avg `-0.0636` n `6`; index avg `-0.0688` n `25`; metal avg `-0.151` n `20`; unknown avg `0.1753` n `787`
- 24h: commodity avg `-0.3077` n `12`; crypto_alt avg `-0.2144` n `230`; crypto_major avg `-0.1035` n `8`; equity avg `0.8795` n `113`; fx avg `-0.0178` n `6`; index avg `0.2156` n `25`; metal avg `-0.546` n `20`; unknown avg `0.989` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2428`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
