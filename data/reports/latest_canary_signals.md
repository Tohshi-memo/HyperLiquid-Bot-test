# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T05:37:33.472313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `12`; crypto_alt avg `0.4087` n `229`; crypto_major avg `0.4371` n `8`; equity avg `0.3439` n `91`; fx avg `-0.0129` n `6`; index avg `0.047` n `25`; metal avg `-0.0262` n `20`; unknown avg `2.3078` n `763`
- 1h: commodity avg `0.0493` n `12`; crypto_alt avg `0.0128` n `229`; crypto_major avg `0.0952` n `8`; equity avg `0.2115` n `91`; fx avg `0.0027` n `6`; index avg `0.0144` n `25`; metal avg `-0.1498` n `20`; unknown avg `-0.3077` n `763`
- 4h: commodity avg `0.0151` n `12`; crypto_alt avg `-0.7396` n `229`; crypto_major avg `-1.065` n `8`; equity avg `-0.4547` n `91`; fx avg `-0.061` n `6`; index avg `-0.1474` n `25`; metal avg `-0.2938` n `20`; unknown avg `14.8883` n `761`
- 24h: commodity avg `0.2078` n `12`; crypto_alt avg `0.2628` n `229`; crypto_major avg `-0.6214` n `8`; equity avg `-1.496` n `90`; fx avg `0.0007` n `6`; index avg `-0.3215` n `25`; metal avg `-0.489` n `20`; unknown avg `-0.4158` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0462`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
