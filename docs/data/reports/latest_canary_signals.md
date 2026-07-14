# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T13:07:27.835851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1107` n `12`; crypto_alt avg `0.0471` n `230`; crypto_major avg `0.1171` n `8`; equity avg `0.0803` n `92`; fx avg `-0.0074` n `6`; index avg `0.0199` n `25`; metal avg `0.062` n `20`; unknown avg `-0.2303` n `766`
- 1h: commodity avg `-0.0343` n `12`; crypto_alt avg `1.1774` n `230`; crypto_major avg `1.6552` n `8`; equity avg `1.0673` n `92`; fx avg `-0.02` n `6`; index avg `0.1967` n `25`; metal avg `0.4702` n `20`; unknown avg `0.6815` n `766`
- 4h: commodity avg `-0.2127` n `12`; crypto_alt avg `1.1092` n `230`; crypto_major avg `1.7249` n `8`; equity avg `0.7464` n `92`; fx avg `-0.0085` n `6`; index avg `0.2334` n `25`; metal avg `0.3565` n `20`; unknown avg `0.7568` n `766`
- 24h: commodity avg `1.2192` n `12`; crypto_alt avg `0.6089` n `230`; crypto_major avg `1.7711` n `8`; equity avg `0.2775` n `92`; fx avg `-0.032` n `6`; index avg `0.1021` n `25`; metal avg `0.2168` n `20`; unknown avg `-0.1295` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
