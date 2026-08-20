# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T19:17:16.076320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.1274` n `230`; crypto_major avg `0.0324` n `8`; equity avg `-0.0102` n `121`; fx avg `0.0019` n `6`; index avg `-0.0015` n `25`; metal avg `0.0508` n `20`; unknown avg `-0.0363` n `792`
- 1h: commodity avg `0.1209` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.7336` n `8`; equity avg `0.153` n `121`; fx avg `-0.0013` n `6`; index avg `0.0327` n `25`; metal avg `0.0808` n `20`; unknown avg `0.0058` n `792`
- 4h: commodity avg `0.169` n `12`; crypto_alt avg `0.1246` n `230`; crypto_major avg `0.2191` n `8`; equity avg `-0.251` n `121`; fx avg `0.0448` n `6`; index avg `-0.0488` n `25`; metal avg `-0.0029` n `20`; unknown avg `1.5435` n `792`
- 24h: commodity avg `0.4507` n `12`; crypto_alt avg `5.4993` n `230`; crypto_major avg `7.1338` n `8`; equity avg `-0.4351` n `121`; fx avg `0.2069` n `6`; index avg `-0.0468` n `25`; metal avg `0.2084` n `20`; unknown avg `3.3871` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
