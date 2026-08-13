# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T22:52:29.462194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.0467` n `230`; crypto_major avg `-0.074` n `8`; equity avg `0.0182` n `113`; fx avg `0.001` n `6`; index avg `-0.0` n `25`; metal avg `-0.0153` n `20`; unknown avg `0.2807` n `787`
- 1h: commodity avg `-0.0369` n `12`; crypto_alt avg `0.0457` n `230`; crypto_major avg `0.1382` n `8`; equity avg `0.0779` n `113`; fx avg `-0.004` n `6`; index avg `0.023` n `25`; metal avg `0.0027` n `20`; unknown avg `0.301` n `787`
- 4h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.3871` n `230`; crypto_major avg `0.2019` n `8`; equity avg `0.0794` n `113`; fx avg `0.0084` n `6`; index avg `0.0038` n `25`; metal avg `-0.0428` n `20`; unknown avg `0.1461` n `787`
- 24h: commodity avg `-0.4603` n `12`; crypto_alt avg `0.6975` n `230`; crypto_major avg `0.7845` n `8`; equity avg `1.7794` n `113`; fx avg `0.0175` n `6`; index avg `0.3361` n `25`; metal avg `-0.4272` n `20`; unknown avg `0.2344` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.242`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
