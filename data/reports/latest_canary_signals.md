# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T11:37:27.343333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1121` n `12`; crypto_alt avg `0.0698` n `230`; crypto_major avg `0.0591` n `8`; equity avg `0.0047` n `92`; fx avg `-0.0018` n `6`; index avg `0.01` n `25`; metal avg `0.0338` n `20`; unknown avg `0.012` n `766`
- 1h: commodity avg `-0.1146` n `12`; crypto_alt avg `0.1773` n `230`; crypto_major avg `0.2843` n `8`; equity avg `-0.274` n `92`; fx avg `-0.0005` n `6`; index avg `0.0232` n `25`; metal avg `0.0124` n `20`; unknown avg `0.0561` n `766`
- 4h: commodity avg `-0.1659` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `0.3871` n `8`; equity avg `-0.0374` n `92`; fx avg `0.0515` n `6`; index avg `0.0351` n `25`; metal avg `-0.0771` n `20`; unknown avg `-0.0677` n `766`
- 24h: commodity avg `1.2147` n `12`; crypto_alt avg `-0.8708` n `230`; crypto_major avg `-0.3517` n `8`; equity avg `-0.8947` n `92`; fx avg `-0.0057` n `6`; index avg `-0.0684` n `25`; metal avg `-0.1997` n `20`; unknown avg `-0.2563` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
