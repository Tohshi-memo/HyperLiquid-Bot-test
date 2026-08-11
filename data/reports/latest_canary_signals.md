# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T19:37:29.013540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.0041` n `230`; crypto_major avg `0.1374` n `8`; equity avg `0.1134` n `113`; fx avg `0.0008` n `6`; index avg `0.0271` n `25`; metal avg `0.0386` n `20`; unknown avg `0.1044` n `785`
- 1h: commodity avg `0.0437` n `12`; crypto_alt avg `0.173` n `230`; crypto_major avg `0.2448` n `8`; equity avg `0.4242` n `113`; fx avg `0.0058` n `6`; index avg `0.0567` n `25`; metal avg `0.0279` n `20`; unknown avg `0.167` n `785`
- 4h: commodity avg `0.0711` n `12`; crypto_alt avg `0.3481` n `230`; crypto_major avg `0.5259` n `8`; equity avg `0.0392` n `113`; fx avg `0.0067` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.1741` n `785`
- 24h: commodity avg `0.1771` n `12`; crypto_alt avg `-1.9565` n `230`; crypto_major avg `-0.3813` n `8`; equity avg `0.3452` n `113`; fx avg `-0.0676` n `6`; index avg `0.0629` n `25`; metal avg `-0.227` n `20`; unknown avg `-0.3125` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2039`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2026`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
