# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T05:22:24.645374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0782` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `0.1033` n `230`; crypto_major avg `0.0021` n `8`; equity avg `-0.1678` n `92`; fx avg `-0.0021` n `6`; index avg `-0.0374` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0275` n `766`
- 1h: commodity avg `0.0369` n `12`; crypto_alt avg `0.1911` n `230`; crypto_major avg `-0.1964` n `8`; equity avg `-0.1208` n `92`; fx avg `-0.0132` n `6`; index avg `-0.0362` n `25`; metal avg `0.0601` n `20`; unknown avg `-0.1843` n `766`
- 4h: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.9393` n `230`; crypto_major avg `-1.3642` n `8`; equity avg `-1.3881` n `92`; fx avg `0.0289` n `6`; index avg `-0.286` n `25`; metal avg `-0.1051` n `20`; unknown avg `2.6052` n `766`
- 24h: commodity avg `0.1197` n `12`; crypto_alt avg `-1.6355` n `230`; crypto_major avg `-1.1217` n `8`; equity avg `-2.4713` n `92`; fx avg `0.0214` n `6`; index avg `-0.5425` n `25`; metal avg `-0.4258` n `20`; unknown avg `-0.0548` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
