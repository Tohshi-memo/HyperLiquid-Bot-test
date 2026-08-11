# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T17:44:46.901756+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.0187` n `230`; crypto_major avg `0.0934` n `8`; equity avg `0.0609` n `113`; fx avg `0.0094` n `6`; index avg `0.0213` n `25`; metal avg `-0.017` n `20`; unknown avg `-0.0278` n `785`
- 1h: commodity avg `0.1028` n `12`; crypto_alt avg `-0.0022` n `230`; crypto_major avg `0.1764` n `8`; equity avg `-0.0307` n `113`; fx avg `0.0098` n `6`; index avg `-0.0353` n `25`; metal avg `-0.0548` n `20`; unknown avg `-0.0648` n `785`
- 4h: commodity avg `0.2264` n `12`; crypto_alt avg `-1.107` n `230`; crypto_major avg `-0.4273` n `8`; equity avg `-0.049` n `113`; fx avg `0.0005` n `6`; index avg `-0.0747` n `25`; metal avg `-0.1306` n `20`; unknown avg `-0.1357` n `785`
- 24h: commodity avg `0.1843` n `12`; crypto_alt avg `-2.0851` n `230`; crypto_major avg `-0.3118` n `8`; equity avg `0.0806` n `113`; fx avg `-0.0561` n `6`; index avg `0.069` n `25`; metal avg `-0.0296` n `20`; unknown avg `-0.3617` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
