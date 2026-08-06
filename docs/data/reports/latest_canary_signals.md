# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T08:07:29.803466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0249` n `230`; crypto_major avg `0.0034` n `8`; equity avg `-0.1226` n `108`; fx avg `-0.0069` n `6`; index avg `-0.0008` n `25`; metal avg `0.0901` n `20`; unknown avg `0.0077` n `782`
- 1h: commodity avg `0.0489` n `12`; crypto_alt avg `-0.0407` n `230`; crypto_major avg `-0.0691` n `8`; equity avg `-0.2224` n `108`; fx avg `0.0426` n `6`; index avg `-0.0302` n `25`; metal avg `0.0114` n `20`; unknown avg `0.0047` n `782`
- 4h: commodity avg `0.1659` n `12`; crypto_alt avg `0.4587` n `230`; crypto_major avg `0.1954` n `8`; equity avg `-0.2604` n `108`; fx avg `0.0923` n `6`; index avg `-0.043` n `25`; metal avg `-0.0561` n `20`; unknown avg `0.0887` n `750`
- 24h: commodity avg `-0.0812` n `12`; crypto_alt avg `0.1032` n `230`; crypto_major avg `-0.222` n `8`; equity avg `-2.1492` n `108`; fx avg `0.0232` n `6`; index avg `-0.3881` n `25`; metal avg `0.1922` n `20`; unknown avg `0.8349` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
