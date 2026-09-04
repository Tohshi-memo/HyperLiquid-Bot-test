# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T03:07:24.298551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.1917` n `232`; crypto_major avg `0.3488` n `8`; equity avg `0.0231` n `133`; fx avg `0.0147` n `6`; index avg `0.0088` n `26`; metal avg `-0.0302` n `20`; unknown avg `-0.2148` n `791`
- 1h: commodity avg `-0.0369` n `12`; crypto_alt avg `0.4632` n `232`; crypto_major avg `0.3954` n `8`; equity avg `0.0335` n `133`; fx avg `-0.0035` n `6`; index avg `0.0285` n `26`; metal avg `-0.0892` n `20`; unknown avg `0.4243` n `791`
- 4h: commodity avg `-0.0305` n `12`; crypto_alt avg `0.1668` n `232`; crypto_major avg `0.1507` n `8`; equity avg `0.3702` n `133`; fx avg `0.0178` n `6`; index avg `0.0293` n `26`; metal avg `-0.0915` n `20`; unknown avg `0.645` n `784`
- 24h: commodity avg `-0.1715` n `12`; crypto_alt avg `3.0398` n `232`; crypto_major avg `4.2357` n `8`; equity avg `1.4994` n `133`; fx avg `-0.1138` n `6`; index avg `0.2095` n `26`; metal avg `0.4968` n `20`; unknown avg `1.1811` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
