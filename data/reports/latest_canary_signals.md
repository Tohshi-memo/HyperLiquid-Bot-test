# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T18:22:34.803319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `12`; crypto_alt avg `0.0296` n `230`; crypto_major avg `0.0139` n `8`; equity avg `-0.0732` n `113`; fx avg `0.0017` n `6`; index avg `-0.0142` n `25`; metal avg `-0.0175` n `20`; unknown avg `0.0676` n `785`
- 1h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.0188` n `230`; crypto_major avg `0.2169` n `8`; equity avg `0.0251` n `113`; fx avg `0.0135` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0978` n `20`; unknown avg `0.1597` n `785`
- 4h: commodity avg `0.1634` n `12`; crypto_alt avg `-1.0568` n `230`; crypto_major avg `-0.3241` n `8`; equity avg `-0.4415` n `113`; fx avg `0.0005` n `6`; index avg `-0.1146` n `25`; metal avg `-0.1342` n `20`; unknown avg `-0.0681` n `785`
- 24h: commodity avg `-0.0031` n `12`; crypto_alt avg `-1.9751` n `230`; crypto_major avg `-0.0785` n `8`; equity avg `0.1826` n `113`; fx avg `-0.0542` n `6`; index avg `0.0525` n `25`; metal avg `-0.0807` n `20`; unknown avg `-0.3105` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1995`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1936`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
