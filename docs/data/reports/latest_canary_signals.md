# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T22:07:25.821157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.2788` n `232`; crypto_major avg `-0.2579` n `8`; equity avg `-0.0537` n `133`; fx avg `0.0083` n `6`; index avg `-0.0081` n `26`; metal avg `0.0225` n `20`; unknown avg `0.9355` n `790`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.1616` n `232`; crypto_major avg `-0.0897` n `8`; equity avg `-0.0128` n `133`; fx avg `0.0052` n `6`; index avg `0.0024` n `26`; metal avg `0.0258` n `20`; unknown avg `2.0387` n `784`
- 4h: commodity avg `0.1212` n `12`; crypto_alt avg `-0.1914` n `232`; crypto_major avg `0.0314` n `8`; equity avg `-0.1219` n `133`; fx avg `0.0192` n `6`; index avg `-0.0371` n `26`; metal avg `-0.0528` n `20`; unknown avg `3.224` n `772`
- 24h: commodity avg `-0.0811` n `12`; crypto_alt avg `4.4393` n `232`; crypto_major avg `5.5011` n `8`; equity avg `1.3212` n `133`; fx avg `-0.2156` n `6`; index avg `0.183` n `26`; metal avg `0.8107` n `20`; unknown avg `221.1555` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
