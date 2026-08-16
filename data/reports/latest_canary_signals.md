# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T12:57:13.042286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0575` n `230`; crypto_major avg `-0.0164` n `8`; equity avg `-0.0231` n `114`; fx avg `-0.0049` n `6`; index avg `0.0034` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.0086` n `791`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `0.0581` n `230`; crypto_major avg `-0.0153` n `8`; equity avg `-0.0812` n `114`; fx avg `-0.0011` n `6`; index avg `0.0041` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.0461` n `791`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `0.1137` n `230`; crypto_major avg `-0.1318` n `8`; equity avg `-0.1501` n `114`; fx avg `-0.0133` n `6`; index avg `-0.0038` n `25`; metal avg `0.001` n `20`; unknown avg `0.0951` n `791`
- 24h: commodity avg `0.0561` n `12`; crypto_alt avg `0.1707` n `230`; crypto_major avg `0.1116` n `8`; equity avg `0.24` n `114`; fx avg `-0.018` n `6`; index avg `0.0381` n `25`; metal avg `0.0324` n `20`; unknown avg `0.0667` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
