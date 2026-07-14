# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T00:37:24.899156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0833` n `12`; crypto_alt avg `0.1096` n `230`; crypto_major avg `0.0269` n `8`; equity avg `0.237` n `92`; fx avg `0.0112` n `6`; index avg `0.0461` n `25`; metal avg `0.0994` n `20`; unknown avg `-0.021` n `766`
- 1h: commodity avg `0.1545` n `12`; crypto_alt avg `0.5193` n `230`; crypto_major avg `0.3635` n `8`; equity avg `0.6731` n `92`; fx avg `0.0093` n `6`; index avg `0.0489` n `25`; metal avg `0.0343` n `20`; unknown avg `0.1992` n `766`
- 4h: commodity avg `0.3373` n `12`; crypto_alt avg `0.2877` n `230`; crypto_major avg `0.3592` n `8`; equity avg `0.131` n `92`; fx avg `0.0086` n `6`; index avg `-0.0252` n `25`; metal avg `0.0041` n `20`; unknown avg `-0.0542` n `766`
- 24h: commodity avg `1.1577` n `12`; crypto_alt avg `-1.8674` n `230`; crypto_major avg `-2.4493` n `8`; equity avg `-2.6645` n `92`; fx avg `-0.0987` n `6`; index avg `-0.5758` n `25`; metal avg `-0.3196` n `20`; unknown avg `-0.3654` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
