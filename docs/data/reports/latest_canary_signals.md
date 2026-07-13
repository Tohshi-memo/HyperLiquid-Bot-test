# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T18:37:27.485251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1419` n `12`; crypto_alt avg `0.1085` n `230`; crypto_major avg `0.1897` n `8`; equity avg `-0.0043` n `92`; fx avg `0.0074` n `6`; index avg `0.0122` n `25`; metal avg `0.0634` n `20`; unknown avg `0.1255` n `766`
- 1h: commodity avg `0.2203` n `12`; crypto_alt avg `-0.1844` n `230`; crypto_major avg `-0.1425` n `8`; equity avg `-0.1018` n `92`; fx avg `0.0025` n `6`; index avg `-0.0309` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.0739` n `766`
- 4h: commodity avg `0.7463` n `12`; crypto_alt avg `-1.2261` n `230`; crypto_major avg `-0.8978` n `8`; equity avg `-1.191` n `92`; fx avg `-0.0219` n `6`; index avg `-0.1971` n `25`; metal avg `-0.1075` n `20`; unknown avg `-0.2509` n `766`
- 24h: commodity avg `0.6152` n `12`; crypto_alt avg `-2.4395` n `230`; crypto_major avg `-3.2883` n `8`; equity avg `-3.278` n `92`; fx avg `-0.069` n `6`; index avg `-0.5951` n `25`; metal avg `-0.5476` n `20`; unknown avg `-0.2943` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
