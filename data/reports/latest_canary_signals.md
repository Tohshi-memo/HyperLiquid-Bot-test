# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T17:37:34.944505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.0824` n `8`; equity avg `0.0231` n `102`; fx avg `0.0001` n `6`; index avg `0.018` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.1451` n `774`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `0.0646` n `8`; equity avg `-0.4928` n `102`; fx avg `-0.0413` n `6`; index avg `-0.0998` n `25`; metal avg `-0.1721` n `20`; unknown avg `-0.2887` n `774`
- 4h: commodity avg `-0.271` n `12`; crypto_alt avg `-1.2603` n `230`; crypto_major avg `-1.1629` n `8`; equity avg `-2.5236` n `102`; fx avg `-0.1153` n `6`; index avg `-0.5439` n `25`; metal avg `-0.0493` n `20`; unknown avg `-0.3928` n `774`
- 24h: commodity avg `-0.6899` n `12`; crypto_alt avg `-0.9833` n `230`; crypto_major avg `-0.1353` n `8`; equity avg `-1.8477` n `102`; fx avg `-0.011` n `6`; index avg `-0.5352` n `25`; metal avg `0.186` n `20`; unknown avg `-0.4147` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
