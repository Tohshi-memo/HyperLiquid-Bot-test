# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T23:37:28.354604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.0156` n `230`; crypto_major avg `0.0109` n `8`; equity avg `-0.2188` n `92`; fx avg `-0.0018` n `6`; index avg `-0.0216` n `25`; metal avg `-0.0316` n `20`; unknown avg `-0.0293` n `766`
- 1h: commodity avg `0.1575` n `12`; crypto_alt avg `0.1744` n `230`; crypto_major avg `0.217` n `8`; equity avg `-0.5462` n `92`; fx avg `0.0155` n `6`; index avg `-0.1026` n `25`; metal avg `-0.0749` n `20`; unknown avg `0.1135` n `766`
- 4h: commodity avg `0.2487` n `12`; crypto_alt avg `-0.365` n `230`; crypto_major avg `-0.1082` n `8`; equity avg `-0.3805` n `92`; fx avg `-0.0165` n `6`; index avg `-0.0835` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.3239` n `766`
- 24h: commodity avg `1.0677` n `12`; crypto_alt avg `-1.7276` n `230`; crypto_major avg `-2.194` n `8`; equity avg `-3.4205` n `92`; fx avg `-0.0515` n `6`; index avg `-0.6735` n `25`; metal avg `-0.34` n `20`; unknown avg `-0.3703` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
