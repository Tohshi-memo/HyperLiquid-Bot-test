# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T12:03:49.527293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `0.0855` n `230`; crypto_major avg `0.1135` n `8`; equity avg `0.1442` n `113`; fx avg `0.003` n `6`; index avg `0.0193` n `25`; metal avg `-0.0373` n `20`; unknown avg `-0.0333` n `786`
- 1h: commodity avg `0.0787` n `12`; crypto_alt avg `0.1763` n `230`; crypto_major avg `0.2528` n `8`; equity avg `0.3261` n `113`; fx avg `0.0287` n `6`; index avg `0.0358` n `25`; metal avg `0.0343` n `20`; unknown avg `-0.0549` n `786`
- 4h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.2084` n `230`; crypto_major avg `0.6418` n `8`; equity avg `0.5746` n `113`; fx avg `0.0021` n `6`; index avg `0.094` n `25`; metal avg `0.1843` n `20`; unknown avg `-0.1034` n `786`
- 24h: commodity avg `0.3353` n `12`; crypto_alt avg `-0.9337` n `230`; crypto_major avg `0.861` n `8`; equity avg `2.4705` n `113`; fx avg `0.0748` n `6`; index avg `0.2167` n `25`; metal avg `0.2552` n `20`; unknown avg `-0.0856` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
