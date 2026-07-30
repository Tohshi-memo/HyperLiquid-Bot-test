# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T17:37:32.190097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `12`; crypto_alt avg `0.0773` n `230`; crypto_major avg `-0.0415` n `8`; equity avg `-0.0501` n `102`; fx avg `-0.0833` n `6`; index avg `-0.0273` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0029` n `779`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0269` n `230`; crypto_major avg `0.0435` n `8`; equity avg `0.214` n `102`; fx avg `-0.0266` n `6`; index avg `-0.0021` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.077` n `779`
- 4h: commodity avg `0.2486` n `12`; crypto_alt avg `0.2586` n `230`; crypto_major avg `0.9049` n `8`; equity avg `2.3626` n `102`; fx avg `-0.0749` n `6`; index avg `0.2303` n `25`; metal avg `0.2414` n `20`; unknown avg `0.1318` n `779`
- 24h: commodity avg `0.0098` n `12`; crypto_alt avg `0.6602` n `230`; crypto_major avg `1.4222` n `8`; equity avg `4.426` n `102`; fx avg `-0.3583` n `6`; index avg `0.3934` n `25`; metal avg `0.7477` n `20`; unknown avg `-0.0524` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
