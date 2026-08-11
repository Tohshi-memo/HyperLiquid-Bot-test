# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T16:52:35.184141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `-0.0195` n `230`; crypto_major avg `-0.0221` n `8`; equity avg `0.0223` n `113`; fx avg `0.0076` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.0087` n `785`
- 1h: commodity avg `-0.0392` n `12`; crypto_alt avg `0.3378` n `230`; crypto_major avg `0.3006` n `8`; equity avg `-0.0387` n `113`; fx avg `-0.0094` n `6`; index avg `-0.0146` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0725` n `785`
- 4h: commodity avg `-0.0413` n `12`; crypto_alt avg `-1.1536` n `230`; crypto_major avg `-0.7898` n `8`; equity avg `0.1085` n `113`; fx avg `-0.0004` n `6`; index avg `-0.0708` n `25`; metal avg `-0.1033` n `20`; unknown avg `0.1127` n `785`
- 24h: commodity avg `0.1979` n `12`; crypto_alt avg `-1.8355` n `230`; crypto_major avg `-0.0841` n `8`; equity avg `0.2077` n `113`; fx avg `-0.0459` n `6`; index avg `0.09` n `25`; metal avg `0.0604` n `20`; unknown avg `-0.3125` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
