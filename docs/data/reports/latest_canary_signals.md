# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T12:07:27.419944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.052` n `12`; crypto_alt avg `-0.5231` n `228`; crypto_major avg `-0.6763` n `8`; equity avg `-0.2149` n `88`; fx avg `0.0004` n `6`; index avg `-0.0348` n `23`; metal avg `-0.0539` n `20`; unknown avg `-0.0773` n `765`
- 1h: commodity avg `0.1637` n `12`; crypto_alt avg `-1.0498` n `228`; crypto_major avg `-0.8288` n `8`; equity avg `-0.2186` n `88`; fx avg `-0.0096` n `6`; index avg `-0.0117` n `23`; metal avg `-0.0548` n `20`; unknown avg `-0.1325` n `765`
- 4h: commodity avg `0.3264` n `12`; crypto_alt avg `-1.3742` n `228`; crypto_major avg `-0.9961` n `8`; equity avg `-0.1797` n `88`; fx avg `-0.0363` n `6`; index avg `-0.0025` n `23`; metal avg `0.04` n `20`; unknown avg `-0.284` n `765`
- 24h: commodity avg `0.3178` n `12`; crypto_alt avg `-2.4157` n `228`; crypto_major avg `-1.1807` n `8`; equity avg `1.0312` n `88`; fx avg `0.1067` n `6`; index avg `0.1519` n `23`; metal avg `0.1295` n `20`; unknown avg `9.0434` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
