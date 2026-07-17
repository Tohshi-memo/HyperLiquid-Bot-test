# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T04:37:25.992634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.0377` n `230`; crypto_major avg `0.0261` n `8`; equity avg `-0.2206` n `96`; fx avg `-0.0068` n `6`; index avg `-0.0746` n `25`; metal avg `-0.0354` n `20`; unknown avg `-0.0728` n `768`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `-0.4085` n `230`; crypto_major avg `-0.4888` n `8`; equity avg `-0.6504` n `96`; fx avg `-0.0097` n `6`; index avg `-0.1715` n `25`; metal avg `-0.1341` n `20`; unknown avg `-0.0482` n `768`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `0.0426` n `230`; crypto_major avg `-0.3221` n `8`; equity avg `-1.0898` n `94`; fx avg `-0.0253` n `6`; index avg `-0.239` n `25`; metal avg `-0.11` n `20`; unknown avg `0.1083` n `768`
- 24h: commodity avg `-0.0526` n `12`; crypto_alt avg `-1.9659` n `230`; crypto_major avg `-3.0614` n `8`; equity avg `-5.5405` n `94`; fx avg `-0.1346` n `6`; index avg `-0.7869` n `25`; metal avg `-0.8672` n `20`; unknown avg `-0.4716` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
