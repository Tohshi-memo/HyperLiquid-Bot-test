# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T06:37:28.478571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.041` n `12`; crypto_alt avg `-0.0178` n `230`; crypto_major avg `-0.11` n `8`; equity avg `-0.1124` n `113`; fx avg `0.0346` n `6`; index avg `-0.0027` n `25`; metal avg `-0.047` n `20`; unknown avg `-0.1133` n `787`
- 1h: commodity avg `0.0592` n `12`; crypto_alt avg `-0.0743` n `230`; crypto_major avg `-0.0628` n `8`; equity avg `-0.3299` n `113`; fx avg `0.0592` n `6`; index avg `-0.0256` n `25`; metal avg `-0.2053` n `20`; unknown avg `-0.1976` n `755`
- 4h: commodity avg `0.1962` n `12`; crypto_alt avg `0.5293` n `230`; crypto_major avg `0.7035` n `8`; equity avg `-0.1868` n `113`; fx avg `0.056` n `6`; index avg `-0.0191` n `25`; metal avg `-0.187` n `20`; unknown avg `0.0178` n `754`
- 24h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.652` n `230`; crypto_major avg `0.3974` n `8`; equity avg `2.3265` n `113`; fx avg `0.0027` n `6`; index avg `0.2624` n `25`; metal avg `-0.3131` n `20`; unknown avg `0.0229` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
