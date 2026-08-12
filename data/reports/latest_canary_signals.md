# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T12:07:28.647753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `0.0933` n `230`; crypto_major avg `0.1064` n `8`; equity avg `0.1232` n `113`; fx avg `0.0055` n `6`; index avg `0.0147` n `25`; metal avg `-0.1151` n `20`; unknown avg `-0.0427` n `786`
- 1h: commodity avg `0.1023` n `12`; crypto_alt avg `0.1838` n `230`; crypto_major avg `0.2456` n `8`; equity avg `0.3052` n `113`; fx avg `0.0311` n `6`; index avg `0.0312` n `25`; metal avg `-0.0439` n `20`; unknown avg `-0.068` n `786`
- 4h: commodity avg `0.0124` n `12`; crypto_alt avg `0.2154` n `230`; crypto_major avg `0.6346` n `8`; equity avg `0.5535` n `113`; fx avg `0.0046` n `6`; index avg `0.0894` n `25`; metal avg `0.1053` n `20`; unknown avg `-0.1229` n `786`
- 24h: commodity avg `0.3591` n `12`; crypto_alt avg `-0.927` n `230`; crypto_major avg `0.8538` n `8`; equity avg `2.449` n `113`; fx avg `0.0773` n `6`; index avg `0.2121` n `25`; metal avg `0.1763` n `20`; unknown avg `-0.1133` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2361`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
