# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T10:22:26.907231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `-0.0389` n `230`; crypto_major avg `0.0329` n `8`; equity avg `0.0545` n `113`; fx avg `0.0029` n `6`; index avg `0.0012` n `25`; metal avg `0.0264` n `20`; unknown avg `0.0103` n `786`
- 1h: commodity avg `-0.0564` n `12`; crypto_alt avg `0.1869` n `230`; crypto_major avg `0.4064` n `8`; equity avg `0.1276` n `113`; fx avg `-0.0099` n `6`; index avg `0.0029` n `25`; metal avg `0.0075` n `20`; unknown avg `0.0399` n `786`
- 4h: commodity avg `-0.1114` n `12`; crypto_alt avg `-0.1705` n `230`; crypto_major avg `0.6285` n `8`; equity avg `0.7827` n `113`; fx avg `-0.0179` n `6`; index avg `0.1179` n `25`; metal avg `0.2978` n `20`; unknown avg `-0.0482` n `786`
- 24h: commodity avg `-0.1266` n `12`; crypto_alt avg `-0.8745` n `230`; crypto_major avg `1.0531` n `8`; equity avg `2.6636` n `113`; fx avg `0.0018` n `6`; index avg `0.2538` n `25`; metal avg `0.2453` n `20`; unknown avg `-0.1719` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2396`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2007`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
