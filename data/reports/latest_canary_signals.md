# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T12:37:29.256113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.085` n `230`; crypto_major avg `-0.1213` n `8`; equity avg `0.4716` n `113`; fx avg `-0.0012` n `6`; index avg `0.0387` n `25`; metal avg `0.1486` n `20`; unknown avg `-0.0203` n `786`
- 1h: commodity avg `0.0865` n `12`; crypto_alt avg `0.3467` n `230`; crypto_major avg `0.0708` n `8`; equity avg `0.728` n `113`; fx avg `0.0028` n `6`; index avg `0.0584` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.1259` n `786`
- 4h: commodity avg `0.0543` n `12`; crypto_alt avg `0.5639` n `230`; crypto_major avg `0.6709` n `8`; equity avg `0.8842` n `113`; fx avg `-0.0084` n `6`; index avg `0.1066` n `25`; metal avg `0.2037` n `20`; unknown avg `-0.168` n `786`
- 24h: commodity avg `0.2745` n `12`; crypto_alt avg `-0.5815` n `230`; crypto_major avg `0.8999` n `8`; equity avg `2.853` n `113`; fx avg `0.0438` n `6`; index avg `0.2233` n `25`; metal avg `0.3908` n `20`; unknown avg `-0.1474` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2473`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2378`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
