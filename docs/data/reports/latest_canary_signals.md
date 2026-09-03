# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T21:53:17.610176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `-0.1403` n `232`; crypto_major avg `-0.0821` n `8`; equity avg `-0.0056` n `133`; fx avg `0.0007` n `6`; index avg `0.0051` n `26`; metal avg `-0.0052` n `20`; unknown avg `0.5634` n `792`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `0.1473` n `232`; crypto_major avg `0.0794` n `8`; equity avg `0.0284` n `133`; fx avg `-0.0032` n `6`; index avg `0.0028` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.984` n `784`
- 4h: commodity avg `0.0555` n `12`; crypto_alt avg `0.2366` n `232`; crypto_major avg `0.3361` n `8`; equity avg `-0.0223` n `133`; fx avg `0.0099` n `6`; index avg `-0.012` n `26`; metal avg `-0.0974` n `20`; unknown avg `0.6521` n `772`
- 24h: commodity avg `-0.0433` n `12`; crypto_alt avg `4.6064` n `232`; crypto_major avg `5.5542` n `8`; equity avg `1.282` n `133`; fx avg `-0.2128` n `6`; index avg `0.1674` n `26`; metal avg `0.7923` n `20`; unknown avg `220.1557` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
