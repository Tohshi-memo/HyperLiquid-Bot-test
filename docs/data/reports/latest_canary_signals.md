# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T08:22:32.040682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.0296` n `230`; crypto_major avg `-0.155` n `8`; equity avg `-0.1314` n `113`; fx avg `-0.0075` n `6`; index avg `-0.0095` n `25`; metal avg `0.0259` n `20`; unknown avg `0.0124` n `787`
- 1h: commodity avg `-0.1712` n `12`; crypto_alt avg `-0.1202` n `230`; crypto_major avg `-0.2022` n `8`; equity avg `-0.1613` n `113`; fx avg `-0.0066` n `6`; index avg `-0.0184` n `25`; metal avg `-0.0742` n `20`; unknown avg `-0.0692` n `787`
- 4h: commodity avg `-0.1687` n `12`; crypto_alt avg `0.0707` n `230`; crypto_major avg `0.3396` n `8`; equity avg `-0.6227` n `113`; fx avg `0.0636` n `6`; index avg `-0.056` n `25`; metal avg `-0.2695` n `20`; unknown avg `-0.0048` n `755`
- 24h: commodity avg `-0.2954` n `12`; crypto_alt avg `-0.5059` n `230`; crypto_major avg `0.2095` n `8`; equity avg `1.2399` n `113`; fx avg `0.0155` n `6`; index avg `0.1621` n `25`; metal avg `-0.5562` n `20`; unknown avg `0.0077` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2489`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
