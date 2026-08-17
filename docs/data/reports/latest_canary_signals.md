# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T12:52:31.192906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.043` n `12`; crypto_alt avg `-0.0317` n `230`; crypto_major avg `-0.0741` n `8`; equity avg `0.0223` n `114`; fx avg `-0.0047` n `6`; index avg `-0.0052` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0439` n `792`
- 1h: commodity avg `0.1515` n `12`; crypto_alt avg `-0.2358` n `230`; crypto_major avg `-0.311` n `8`; equity avg `-0.3078` n `114`; fx avg `0.0022` n `6`; index avg `-0.0528` n `25`; metal avg `-0.0732` n `20`; unknown avg `-0.0357` n `792`
- 4h: commodity avg `0.1571` n `12`; crypto_alt avg `0.1451` n `230`; crypto_major avg `0.0608` n `8`; equity avg `-0.4555` n `114`; fx avg `0.0203` n `6`; index avg `-0.0493` n `25`; metal avg `-0.0435` n `20`; unknown avg `0.0173` n `792`
- 24h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.1818` n `230`; crypto_major avg `0.6066` n `8`; equity avg `0.9277` n `114`; fx avg `-0.0087` n `6`; index avg `0.0913` n `25`; metal avg `0.0909` n `20`; unknown avg `-0.001` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
