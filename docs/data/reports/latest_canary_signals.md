# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T22:22:15.737325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.1908` n `228`; crypto_major avg `0.0018` n `8`; equity avg `-0.1382` n `66`; fx avg `0.0039` n `6`; index avg `-0.0899` n `23`; metal avg `-0.2122` n `18`; unknown avg `-0.1717` n `384`
- 1h: commodity avg `-0.1106` n `12`; crypto_alt avg `-0.434` n `228`; crypto_major avg `-0.1552` n `8`; equity avg `-0.4529` n `66`; fx avg `-0.004` n `6`; index avg `-0.2213` n `23`; metal avg `-0.2776` n `18`; unknown avg `-0.1292` n `384`
- 4h: commodity avg `0.2516` n `12`; crypto_alt avg `-0.3831` n `228`; crypto_major avg `-0.1781` n `8`; equity avg `-0.5079` n `66`; fx avg `-0.0403` n `6`; index avg `-0.1584` n `23`; metal avg `-0.3294` n `18`; unknown avg `-0.5025` n `384`
- 24h: commodity avg `-2.4493` n `12`; crypto_alt avg `2.6473` n `228`; crypto_major avg `2.0283` n `8`; equity avg `1.191` n `66`; fx avg `-0.0763` n `6`; index avg `0.9276` n `23`; metal avg `1.2628` n `18`; unknown avg `0.8501` n `373`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
