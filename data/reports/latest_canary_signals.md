# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T18:37:10.720457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0501` n `12`; crypto_alt avg `-0.1982` n `230`; crypto_major avg `-0.1535` n `8`; equity avg `-0.0086` n `113`; fx avg `0.0016` n `6`; index avg `-0.0016` n `25`; metal avg `0.1157` n `20`; unknown avg `-0.0856` n `785`
- 1h: commodity avg `0.0944` n `12`; crypto_alt avg `-0.2744` n `230`; crypto_major avg `-0.2646` n `8`; equity avg `-0.1433` n `113`; fx avg `0.0038` n `6`; index avg `-0.0126` n `25`; metal avg `0.0858` n `20`; unknown avg `-0.2861` n `785`
- 4h: commodity avg `0.3377` n `12`; crypto_alt avg `-0.6219` n `230`; crypto_major avg `-0.7466` n `8`; equity avg `-0.6399` n `113`; fx avg `-0.0022` n `6`; index avg `-0.088` n `25`; metal avg `0.2119` n `20`; unknown avg `-0.0929` n `784`
- 24h: commodity avg `1.3058` n `12`; crypto_alt avg `-0.9255` n `230`; crypto_major avg `-1.378` n `8`; equity avg `-1.4745` n `113`; fx avg `0.2501` n `6`; index avg `-0.1012` n `25`; metal avg `0.1036` n `20`; unknown avg `103.2943` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
