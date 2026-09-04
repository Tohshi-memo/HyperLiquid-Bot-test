# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T03:52:24.021212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `0.0476` n `232`; crypto_major avg `-0.0131` n `8`; equity avg `-0.0101` n `133`; fx avg `0.0116` n `6`; index avg `0.011` n `26`; metal avg `-0.0391` n `20`; unknown avg `-0.0037` n `793`
- 1h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.114` n `232`; crypto_major avg `0.2134` n `8`; equity avg `0.0235` n `133`; fx avg `0.0258` n `6`; index avg `0.0112` n `26`; metal avg `-0.0679` n `20`; unknown avg `-0.1459` n `791`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `-0.3717` n `232`; crypto_major avg `-0.247` n `8`; equity avg `0.3295` n `133`; fx avg `0.0557` n `6`; index avg `0.038` n `26`; metal avg `-0.1379` n `20`; unknown avg `3.1671` n `784`
- 24h: commodity avg `-0.1175` n `12`; crypto_alt avg `2.9034` n `232`; crypto_major avg `4.2278` n `8`; equity avg `1.3057` n `133`; fx avg `-0.0869` n `6`; index avg `0.1857` n `26`; metal avg `0.426` n `20`; unknown avg `1.1517` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
