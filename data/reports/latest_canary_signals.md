# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T01:37:27.884912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.2429` n `232`; crypto_major avg `-0.2511` n `8`; equity avg `-0.0256` n `133`; fx avg `-0.0035` n `6`; index avg `0.0029` n `26`; metal avg `-0.012` n `20`; unknown avg `-0.0477` n `793`
- 1h: commodity avg `0.0535` n `12`; crypto_alt avg `-0.8387` n `232`; crypto_major avg `-0.8003` n `8`; equity avg `-0.015` n `133`; fx avg `0.0169` n `6`; index avg `0.0008` n `26`; metal avg `-0.0395` n `20`; unknown avg `0.0861` n `791`
- 4h: commodity avg `0.0362` n `12`; crypto_alt avg `-1.1366` n `232`; crypto_major avg `-0.9399` n `8`; equity avg `0.2112` n `133`; fx avg `0.0458` n `6`; index avg `0.0159` n `26`; metal avg `-0.0413` n `20`; unknown avg `1.568` n `784`
- 24h: commodity avg `-0.1375` n `12`; crypto_alt avg `2.8767` n `232`; crypto_major avg `4.2657` n `8`; equity avg `1.4514` n `133`; fx avg `-0.1356` n `6`; index avg `0.1914` n `26`; metal avg `0.637` n `20`; unknown avg `1.1551` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
