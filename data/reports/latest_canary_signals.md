# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T01:52:24.864792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `0.1622` n `232`; crypto_major avg `0.2145` n `8`; equity avg `-0.064` n `133`; fx avg `0.0129` n `6`; index avg `-0.0151` n `26`; metal avg `-0.0369` n `20`; unknown avg `-0.1611` n `793`
- 1h: commodity avg `0.0984` n `12`; crypto_alt avg `-0.3518` n `232`; crypto_major avg `-0.2254` n `8`; equity avg `-0.1576` n `133`; fx avg `0.0448` n `6`; index avg `-0.024` n `26`; metal avg `-0.0873` n `20`; unknown avg `-0.1397` n `791`
- 4h: commodity avg `0.048` n `12`; crypto_alt avg `-0.8391` n `232`; crypto_major avg `-0.6453` n `8`; equity avg `0.1525` n `133`; fx avg `0.058` n `6`; index avg `-0.0043` n `26`; metal avg `-0.073` n `20`; unknown avg `1.5453` n `784`
- 24h: commodity avg `-0.1443` n `12`; crypto_alt avg `3.0938` n `232`; crypto_major avg `4.5607` n `8`; equity avg `1.4177` n `133`; fx avg `-0.1427` n `6`; index avg `0.1923` n `26`; metal avg `0.5875` n `20`; unknown avg `1.173` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
