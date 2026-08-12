# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T10:37:24.535075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0217` n `12`; crypto_alt avg `-0.0726` n `230`; crypto_major avg `-0.0344` n `8`; equity avg `-0.0649` n `113`; fx avg `0.0106` n `6`; index avg `0.0004` n `25`; metal avg `-0.0184` n `20`; unknown avg `0.0106` n `786`
- 1h: commodity avg `0.0733` n `12`; crypto_alt avg `-0.096` n `230`; crypto_major avg `0.0269` n `8`; equity avg `-0.0401` n `113`; fx avg `0.0225` n `6`; index avg `-0.0198` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.0163` n `786`
- 4h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.0938` n `230`; crypto_major avg `0.6054` n `8`; equity avg `0.6767` n `113`; fx avg `-0.011` n `6`; index avg `0.0971` n `25`; metal avg `0.2406` n `20`; unknown avg `-0.0443` n `786`
- 24h: commodity avg `-0.0095` n `12`; crypto_alt avg `-1.0717` n `230`; crypto_major avg `0.9348` n `8`; equity avg `2.4808` n `113`; fx avg `0.0248` n `6`; index avg `0.227` n `25`; metal avg `0.2064` n `20`; unknown avg `-0.1794` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2312`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
