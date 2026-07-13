# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T09:07:30.706560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `-0.0583` n `230`; crypto_major avg `-0.1699` n `8`; equity avg `-0.0098` n `92`; fx avg `-0.0027` n `6`; index avg `-0.0362` n `25`; metal avg `-0.0125` n `20`; unknown avg `-0.0017` n `766`
- 1h: commodity avg `-0.1484` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `0.0545` n `8`; equity avg `0.2643` n `92`; fx avg `-0.0092` n `6`; index avg `0.0336` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.0282` n `766`
- 4h: commodity avg `-0.407` n `12`; crypto_alt avg `0.5742` n `230`; crypto_major avg `0.255` n `8`; equity avg `0.2328` n `92`; fx avg `-0.0498` n `6`; index avg `0.0706` n `25`; metal avg `0.2531` n `20`; unknown avg `0.0525` n `750`
- 24h: commodity avg `-0.3366` n `12`; crypto_alt avg `-1.0205` n `230`; crypto_major avg `-0.9419` n `8`; equity avg `-2.0303` n `92`; fx avg `-0.0294` n `6`; index avg `-0.4396` n `25`; metal avg `-0.1476` n `20`; unknown avg `-0.1015` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
