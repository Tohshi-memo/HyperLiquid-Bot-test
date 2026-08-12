# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T18:52:29.465842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.1289` n `230`; crypto_major avg `-0.1038` n `8`; equity avg `-0.086` n `113`; fx avg `-0.0035` n `6`; index avg `-0.0058` n `25`; metal avg `0.0163` n `20`; unknown avg `-0.0364` n `786`
- 1h: commodity avg `0.0287` n `12`; crypto_alt avg `-0.1726` n `230`; crypto_major avg `-0.1952` n `8`; equity avg `-0.1119` n `113`; fx avg `-0.0015` n `6`; index avg `0.008` n `25`; metal avg `0.0415` n `20`; unknown avg `-0.0521` n `786`
- 4h: commodity avg `0.038` n `12`; crypto_alt avg `0.043` n `230`; crypto_major avg `0.1511` n `8`; equity avg `0.6299` n `113`; fx avg `0.0032` n `6`; index avg `0.0288` n `25`; metal avg `-0.1123` n `20`; unknown avg `0.2578` n `786`
- 24h: commodity avg `0.0711` n `12`; crypto_alt avg `-0.1743` n `230`; crypto_major avg `0.7857` n `8`; equity avg `3.9037` n `113`; fx avg `0.0282` n `6`; index avg `0.4637` n `25`; metal avg `0.2487` n `20`; unknown avg `0.1157` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2254`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
