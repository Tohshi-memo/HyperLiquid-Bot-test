# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T13:22:24.330813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `13`; crypto_alt avg `-0.0195` n `237`; crypto_major avg `-0.0479` n `8`; equity avg `0.1293` n `152`; fx avg `0.0011` n `6`; index avg `0.0149` n `26`; metal avg `0.0035` n `20`; unknown avg `4.1275` n `1231`
- 1h: commodity avg `-0.0029` n `13`; crypto_alt avg `0.0239` n `237`; crypto_major avg `-0.0716` n `8`; equity avg `0.1484` n `152`; fx avg `-0.0032` n `6`; index avg `0.0194` n `26`; metal avg `0.0072` n `20`; unknown avg `2.9899` n `1231`
- 4h: commodity avg `-0.0453` n `13`; crypto_alt avg `0.6466` n `237`; crypto_major avg `0.4412` n `8`; equity avg `0.4395` n `152`; fx avg `0.004` n `6`; index avg `0.0604` n `26`; metal avg `0.0551` n `20`; unknown avg `17.9812` n `1195`
- 24h: commodity avg `-0.1762` n `13`; crypto_alt avg `-1.2378` n `237`; crypto_major avg `-0.0672` n `8`; equity avg `0.2284` n `152`; fx avg `0.0038` n `6`; index avg `0.0543` n `26`; metal avg `-0.0241` n `20`; unknown avg `22.2232` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2242`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
