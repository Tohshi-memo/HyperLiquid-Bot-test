# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T02:07:29.123559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0424` n `230`; crypto_major avg `0.0582` n `8`; equity avg `-0.2025` n `92`; fx avg `0.0027` n `6`; index avg `-0.0742` n `25`; metal avg `0.0583` n `20`; unknown avg `0.024` n `766`
- 1h: commodity avg `-0.1121` n `12`; crypto_alt avg `-0.1099` n `230`; crypto_major avg `0.0293` n `8`; equity avg `-0.5596` n `92`; fx avg `0.0068` n `6`; index avg `-0.1361` n `25`; metal avg `0.1167` n `20`; unknown avg `-0.2331` n `766`
- 4h: commodity avg `0.1429` n `12`; crypto_alt avg `0.7509` n `230`; crypto_major avg `0.6653` n `8`; equity avg `-0.1389` n `92`; fx avg `-0.0326` n `6`; index avg `-0.0632` n `25`; metal avg `0.0087` n `20`; unknown avg `0.1425` n `766`
- 24h: commodity avg `0.9047` n `12`; crypto_alt avg `-0.6956` n `230`; crypto_major avg `-1.2869` n `8`; equity avg `-1.5258` n `92`; fx avg `-0.1454` n `6`; index avg `-0.2653` n `25`; metal avg `-0.2424` n `20`; unknown avg `-0.311` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
