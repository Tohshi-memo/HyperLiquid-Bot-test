# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T20:37:18.542542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0462` n `230`; crypto_major avg `0.0219` n `8`; equity avg `0.0315` n `113`; fx avg `0.0008` n `6`; index avg `0.006` n `25`; metal avg `0.0106` n `20`; unknown avg `0.0477` n `785`
- 1h: commodity avg `-0.045` n `12`; crypto_alt avg `0.3485` n `230`; crypto_major avg `0.5744` n `8`; equity avg `0.3662` n `113`; fx avg `-0.008` n `6`; index avg `0.033` n `25`; metal avg `0.0086` n `20`; unknown avg `0.3844` n `785`
- 4h: commodity avg `0.0788` n `12`; crypto_alt avg `0.3926` n `230`; crypto_major avg `0.8624` n `8`; equity avg `0.5447` n `113`; fx avg `0.0151` n `6`; index avg `0.0013` n `25`; metal avg `-0.0593` n `20`; unknown avg `0.5645` n `785`
- 24h: commodity avg `0.1166` n `12`; crypto_alt avg `-1.5599` n `230`; crypto_major avg `0.1428` n `8`; equity avg `1.0546` n `113`; fx avg `-0.0697` n `6`; index avg `0.1337` n `25`; metal avg `-0.2126` n `20`; unknown avg `-0.2275` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2164`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
