# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T11:37:30.814160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `12`; crypto_alt avg `-0.082` n `230`; crypto_major avg `0.0034` n `8`; equity avg `0.0626` n `113`; fx avg `0.0118` n `6`; index avg `0.0093` n `25`; metal avg `0.0491` n `20`; unknown avg `0.0312` n `786`
- 1h: commodity avg `0.0496` n `12`; crypto_alt avg `0.0581` n `230`; crypto_major avg `0.0903` n `8`; equity avg `-0.0239` n `113`; fx avg `0.0027` n `6`; index avg `-0.0048` n `25`; metal avg `0.0793` n `20`; unknown avg `-0.0236` n `786`
- 4h: commodity avg `-0.057` n `12`; crypto_alt avg `0.1511` n `230`; crypto_major avg `0.5884` n `8`; equity avg `0.417` n `113`; fx avg `-0.0288` n `6`; index avg `0.0849` n `25`; metal avg `0.2452` n `20`; unknown avg `-0.0441` n `786`
- 24h: commodity avg `0.3044` n `12`; crypto_alt avg `-1.0707` n `230`; crypto_major avg `0.7888` n `8`; equity avg `2.1372` n `113`; fx avg `0.0526` n `6`; index avg `0.1947` n `25`; metal avg `0.2835` n `20`; unknown avg `-0.1083` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.245`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
