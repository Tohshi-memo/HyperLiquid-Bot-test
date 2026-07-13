# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T15:07:27.863585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0856` n `12`; crypto_alt avg `0.1725` n `230`; crypto_major avg `0.1635` n `8`; equity avg `0.255` n `92`; fx avg `-0.0022` n `6`; index avg `0.0368` n `25`; metal avg `0.0435` n `20`; unknown avg `-0.0252` n `766`
- 1h: commodity avg `0.2638` n `12`; crypto_alt avg `0.5102` n `230`; crypto_major avg `0.528` n `8`; equity avg `0.764` n `92`; fx avg `-0.0249` n `6`; index avg `0.0724` n `25`; metal avg `-0.0242` n `20`; unknown avg `0.1681` n `766`
- 4h: commodity avg `0.1752` n `12`; crypto_alt avg `0.0302` n `230`; crypto_major avg `-0.3406` n `8`; equity avg `-0.1515` n `92`; fx avg `-0.0391` n `6`; index avg `0.0226` n `25`; metal avg `-0.1864` n `20`; unknown avg `-0.0073` n `766`
- 24h: commodity avg `0.0836` n `12`; crypto_alt avg `-1.2332` n `230`; crypto_major avg `-2.1488` n `8`; equity avg `-2.0603` n `92`; fx avg `-0.0838` n `6`; index avg `-0.4061` n `25`; metal avg `-0.3771` n `20`; unknown avg `-0.1333` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
