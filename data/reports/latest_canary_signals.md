# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T14:22:35.757355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `-0.0457` n `113`; fx avg `0.013` n `6`; index avg `-0.0154` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.0488` n `785`
- 1h: commodity avg `0.0625` n `12`; crypto_alt avg `-0.0373` n `230`; crypto_major avg `-0.113` n `8`; equity avg `0.3214` n `113`; fx avg `0.0042` n `6`; index avg `-0.0062` n `25`; metal avg `-0.1163` n `20`; unknown avg `-0.0118` n `785`
- 4h: commodity avg `-0.3232` n `12`; crypto_alt avg `-0.0447` n `230`; crypto_major avg `0.0982` n `8`; equity avg `0.8369` n `113`; fx avg `-0.0232` n `6`; index avg `0.0664` n `25`; metal avg `-0.146` n `20`; unknown avg `-0.1108` n `785`
- 24h: commodity avg `0.2463` n `12`; crypto_alt avg `-1.3462` n `230`; crypto_major avg `-0.2647` n `8`; equity avg `0.0847` n `113`; fx avg `-0.0396` n `6`; index avg `0.1013` n `25`; metal avg `0.2309` n `20`; unknown avg `-0.1304` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
