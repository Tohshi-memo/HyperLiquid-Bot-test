# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T06:07:26.444055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.037` n `13`; crypto_alt avg `-0.1514` n `239`; crypto_major avg `-0.0186` n `8`; equity avg `-0.0794` n `161`; fx avg `0.0029` n `6`; index avg `-0.0217` n `27`; metal avg `-0.021` n `20`; unknown avg `-0.2114` n `1229`
- 1h: commodity avg `0.0826` n `13`; crypto_alt avg `-0.1936` n `239`; crypto_major avg `0.2402` n `8`; equity avg `0.2901` n `161`; fx avg `-0.004` n `6`; index avg `0.0073` n `27`; metal avg `0.0729` n `20`; unknown avg `-0.2482` n `1223`
- 4h: commodity avg `0.0612` n `13`; crypto_alt avg `0.063` n `239`; crypto_major avg `0.4045` n `8`; equity avg `1.3666` n `161`; fx avg `-0.0556` n `6`; index avg `0.1618` n `27`; metal avg `0.2166` n `20`; unknown avg `3.3252` n `1217`
- 24h: commodity avg `0.3211` n `13`; crypto_alt avg `-0.7094` n `239`; crypto_major avg `-2.1357` n `8`; equity avg `1.4913` n `161`; fx avg `-0.1756` n `6`; index avg `0.1822` n `27`; metal avg `-0.1551` n `20`; unknown avg `2.4931` n `1162`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2594`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2343`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
