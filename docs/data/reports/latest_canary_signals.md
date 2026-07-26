# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T01:53:21.157994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0378` n `12`; crypto_alt avg `0.0238` n `230`; crypto_major avg `0.0321` n `8`; equity avg `-0.019` n `100`; fx avg `0.0045` n `6`; index avg `0.0044` n `25`; metal avg `0.0012` n `20`; unknown avg `0.1238` n `774`
- 1h: commodity avg `0.0566` n `12`; crypto_alt avg `0.1016` n `230`; crypto_major avg `0.1` n `8`; equity avg `0.1547` n `100`; fx avg `0.0021` n `6`; index avg `0.0356` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.1235` n `774`
- 4h: commodity avg `-0.0577` n `12`; crypto_alt avg `-0.0123` n `230`; crypto_major avg `0.1178` n `8`; equity avg `0.2411` n `100`; fx avg `-0.004` n `6`; index avg `0.0462` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.3029` n `774`
- 24h: commodity avg `-0.5996` n `12`; crypto_alt avg `0.577` n `230`; crypto_major avg `1.1476` n `8`; equity avg `0.62` n `100`; fx avg `-0.0342` n `6`; index avg `0.1682` n `25`; metal avg `0.0273` n `20`; unknown avg `-0.2457` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1353`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1233`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1178`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1164`, n `666`, weak_sample_signal
