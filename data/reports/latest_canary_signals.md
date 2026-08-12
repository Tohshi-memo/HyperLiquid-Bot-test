# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T05:52:25.486373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0459` n `12`; crypto_alt avg `-0.0236` n `230`; crypto_major avg `-0.0308` n `8`; equity avg `-0.0284` n `113`; fx avg `0.0117` n `6`; index avg `0.004` n `25`; metal avg `-0.04` n `20`; unknown avg `0.0172` n `786`
- 1h: commodity avg `0.0614` n `12`; crypto_alt avg `-0.098` n `230`; crypto_major avg `0.0092` n `8`; equity avg `-0.1077` n `113`; fx avg `0.0006` n `6`; index avg `0.0097` n `25`; metal avg `-0.1007` n `20`; unknown avg `-0.1931` n `786`
- 4h: commodity avg `0.085` n `12`; crypto_alt avg `-0.2194` n `230`; crypto_major avg `-0.2383` n `8`; equity avg `0.2954` n `113`; fx avg `0.005` n `6`; index avg `0.0598` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.2753` n `786`
- 24h: commodity avg `0.212` n `12`; crypto_alt avg `-1.0529` n `230`; crypto_major avg `0.7141` n `8`; equity avg `1.7492` n `113`; fx avg `0.0197` n `6`; index avg `0.1581` n `25`; metal avg `0.1018` n `20`; unknown avg `-0.1262` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2153`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
