# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T15:52:41.006023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0249` n `12`; crypto_alt avg `-0.091` n `230`; crypto_major avg `-0.1226` n `8`; equity avg `-0.181` n `94`; fx avg `-0.0063` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0275` n `20`; unknown avg `-0.1033` n `768`
- 1h: commodity avg `-0.0551` n `12`; crypto_alt avg `0.0221` n `230`; crypto_major avg `-0.0838` n `8`; equity avg `-0.2147` n `94`; fx avg `-0.0104` n `6`; index avg `0.0347` n `25`; metal avg `0.0873` n `20`; unknown avg `-0.0492` n `768`
- 4h: commodity avg `-0.2486` n `12`; crypto_alt avg `0.6879` n `230`; crypto_major avg `0.3234` n `8`; equity avg `-1.1479` n `94`; fx avg `-0.0041` n `6`; index avg `0.0547` n `25`; metal avg `-0.1073` n `20`; unknown avg `0.2926` n `768`
- 24h: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.6993` n `230`; crypto_major avg `-1.5922` n `8`; equity avg `-2.5557` n `94`; fx avg `-0.0612` n `6`; index avg `-0.1959` n `25`; metal avg `-0.2108` n `20`; unknown avg `-0.2571` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
