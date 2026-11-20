# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T22:52:26.556990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `0.0385` n `239`; crypto_major avg `-0.1944` n `8`; equity avg `-0.0124` n `166`; fx avg `-0.0244` n `6`; index avg `0.0116` n `27`; metal avg `-0.0009` n `20`; unknown avg `1.8395` n `1258`
- 1h: commodity avg `0.0036` n `13`; crypto_alt avg `0.3281` n `239`; crypto_major avg `0.0606` n `8`; equity avg `0.3` n `166`; fx avg `-0.0334` n `6`; index avg `0.0379` n `27`; metal avg `0.0081` n `20`; unknown avg `161.0263` n `1238`
- 4h: commodity avg `0.3195` n `13`; crypto_alt avg `0.5724` n `239`; crypto_major avg `0.2416` n `8`; equity avg `-0.394` n `166`; fx avg `-0.0596` n `6`; index avg `-0.1191` n `27`; metal avg `0.0716` n `20`; unknown avg `2.3111` n `1204`
- 24h: commodity avg `0.2728` n `13`; crypto_alt avg `-4.9025` n `239`; crypto_major avg `-5.7295` n `8`; equity avg `-6.3438` n `166`; fx avg `-0.0116` n `6`; index avg `-0.713` n `27`; metal avg `-0.8387` n `20`; unknown avg `31.9868` n `1127`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
