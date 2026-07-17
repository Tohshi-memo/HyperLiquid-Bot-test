# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T04:31:00.063460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `12`; crypto_alt avg `0.0685` n `230`; crypto_major avg `0.0747` n `8`; equity avg `-0.2099` n `96`; fx avg `-0.0023` n `6`; index avg `-0.0457` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.0516` n `768`
- 1h: commodity avg `0.0702` n `12`; crypto_alt avg `-0.3781` n `230`; crypto_major avg `-0.4406` n `8`; equity avg `-0.6401` n `96`; fx avg `-0.0052` n `6`; index avg `-0.1428` n `25`; metal avg `-0.1016` n `20`; unknown avg `-0.0462` n `768`
- 4h: commodity avg `0.0106` n `12`; crypto_alt avg `0.0742` n `230`; crypto_major avg `-0.2738` n `8`; equity avg `-1.0773` n `94`; fx avg `-0.0208` n `6`; index avg `-0.2104` n `25`; metal avg `-0.0776` n `20`; unknown avg `0.1118` n `768`
- 24h: commodity avg `-0.0341` n `12`; crypto_alt avg `-1.9401` n `230`; crypto_major avg `-3.0151` n `8`; equity avg `-5.5284` n `94`; fx avg `-0.1302` n `6`; index avg `-0.7593` n `25`; metal avg `-0.8356` n `20`; unknown avg `-0.4663` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
