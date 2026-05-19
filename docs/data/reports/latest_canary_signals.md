# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T17:22:18.885215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `0.0791` n `228`; crypto_major avg `0.198` n `8`; equity avg `0.3174` n `66`; fx avg `-0.0022` n `6`; index avg `0.1664` n `23`; metal avg `0.1365` n `18`; unknown avg `0.0968` n `383`
- 1h: commodity avg `0.1557` n `12`; crypto_alt avg `0.7588` n `228`; crypto_major avg `0.6874` n `8`; equity avg `1.3518` n `66`; fx avg `0.0374` n `6`; index avg `0.684` n `23`; metal avg `0.3834` n `18`; unknown avg `0.2369` n `383`
- 4h: commodity avg `0.3203` n `12`; crypto_alt avg `0.1267` n `228`; crypto_major avg `0.4969` n `8`; equity avg `1.8206` n `66`; fx avg `-0.0556` n `6`; index avg `0.5303` n `23`; metal avg `-0.1591` n `18`; unknown avg `-0.1132` n `383`
- 24h: commodity avg `0.8009` n `12`; crypto_alt avg `0.9996` n `228`; crypto_major avg `1.2096` n `8`; equity avg `1.2454` n `66`; fx avg `-0.0116` n `6`; index avg `0.0782` n `23`; metal avg `-1.7548` n `18`; unknown avg `0.1293` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
