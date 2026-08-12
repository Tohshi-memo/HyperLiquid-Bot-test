# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T03:22:26.098890+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.1379` n `230`; crypto_major avg `0.0208` n `8`; equity avg `0.0315` n `113`; fx avg `0.0041` n `6`; index avg `0.0144` n `25`; metal avg `-0.0705` n `20`; unknown avg `0.3115` n `786`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `0.1024` n `230`; crypto_major avg `-0.0188` n `8`; equity avg `0.3292` n `113`; fx avg `0.0241` n `6`; index avg `0.0894` n `25`; metal avg `0.0517` n `20`; unknown avg `-0.0895` n `786`
- 4h: commodity avg `0.1361` n `12`; crypto_alt avg `0.412` n `230`; crypto_major avg `0.242` n `8`; equity avg `0.8628` n `113`; fx avg `0.0665` n `6`; index avg `0.1896` n `25`; metal avg `0.1953` n `20`; unknown avg `-0.1818` n `786`
- 24h: commodity avg `0.2594` n `12`; crypto_alt avg `-0.962` n `230`; crypto_major avg `0.5665` n `8`; equity avg `1.7881` n `113`; fx avg `0.0397` n `6`; index avg `0.1631` n `25`; metal avg `-0.1355` n `20`; unknown avg `0.0267` n `753`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2286`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.225`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2162`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
