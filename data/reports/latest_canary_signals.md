# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T16:37:28.169245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0023` n `230`; crypto_major avg `0.0558` n `8`; equity avg `0.0094` n `114`; fx avg `0.0044` n `6`; index avg `0.0075` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0448` n `791`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.0681` n `230`; crypto_major avg `0.2143` n `8`; equity avg `0.027` n `114`; fx avg `0.007` n `6`; index avg `0.0117` n `25`; metal avg `0.0069` n `20`; unknown avg `-0.1616` n `791`
- 4h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.2664` n `230`; crypto_major avg `0.3943` n `8`; equity avg `0.1144` n `114`; fx avg `0.0048` n `6`; index avg `0.0067` n `25`; metal avg `-0.001` n `20`; unknown avg `0.0178` n `791`
- 24h: commodity avg `0.0452` n `12`; crypto_alt avg `-0.0433` n `230`; crypto_major avg `0.2991` n `8`; equity avg `0.3503` n `114`; fx avg `0.0005` n `6`; index avg `0.0344` n `25`; metal avg `0.0483` n `20`; unknown avg `0.0949` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
