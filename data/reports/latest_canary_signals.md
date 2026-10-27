# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T22:22:31.945482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0481` n `13`; crypto_alt avg `0.0394` n `238`; crypto_major avg `0.0318` n `8`; equity avg `0.0354` n `154`; fx avg `0.0005` n `6`; index avg `0.0119` n `27`; metal avg `0.0146` n `20`; unknown avg `0.0835` n `1236`
- 1h: commodity avg `-0.0687` n `13`; crypto_alt avg `0.4148` n `238`; crypto_major avg `0.314` n `8`; equity avg `0.0841` n `154`; fx avg `-0.0011` n `6`; index avg `0.0094` n `27`; metal avg `0.0181` n `20`; unknown avg `0.5994` n `1234`
- 4h: commodity avg `0.0546` n `13`; crypto_alt avg `0.2089` n `238`; crypto_major avg `0.2075` n `8`; equity avg `-0.0048` n `154`; fx avg `-0.0005` n `6`; index avg `0.023` n `27`; metal avg `0.1242` n `20`; unknown avg `2.0737` n `1152`
- 24h: commodity avg `-0.2719` n `13`; crypto_alt avg `1.4032` n `237`; crypto_major avg `1.6351` n `8`; equity avg `1.3075` n `154`; fx avg `-0.0579` n `6`; index avg `0.3844` n `27`; metal avg `0.23` n `20`; unknown avg `34.6889` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
