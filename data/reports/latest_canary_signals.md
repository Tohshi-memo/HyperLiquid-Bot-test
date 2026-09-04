# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T03:37:27.686492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.1148` n `232`; crypto_major avg `-0.0185` n `8`; equity avg `-0.0032` n `133`; fx avg `0.0078` n `6`; index avg `-0.0089` n `26`; metal avg `0.0027` n `20`; unknown avg `0.1288` n `793`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `0.0064` n `232`; crypto_major avg `0.2949` n `8`; equity avg `0.0747` n `133`; fx avg `0.0169` n `6`; index avg `0.0153` n `26`; metal avg `-0.006` n `20`; unknown avg `0.5891` n `791`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `-0.4312` n `232`; crypto_major avg `-0.21` n `8`; equity avg `0.3563` n `133`; fx avg `0.0321` n `6`; index avg `0.029` n `26`; metal avg `-0.1039` n `20`; unknown avg `2.192` n `784`
- 24h: commodity avg `-0.1139` n `12`; crypto_alt avg `2.8793` n `232`; crypto_major avg `4.3228` n `8`; equity avg `1.3364` n `133`; fx avg `-0.1235` n `6`; index avg `0.1735` n `26`; metal avg `0.4688` n `20`; unknown avg `23.491` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
