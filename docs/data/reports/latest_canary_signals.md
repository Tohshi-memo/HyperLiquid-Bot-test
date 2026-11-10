# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T21:52:30.455086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `13`; crypto_alt avg `0.161` n `239`; crypto_major avg `-0.0198` n `8`; equity avg `0.0192` n `160`; fx avg `-0.0003` n `6`; index avg `-0.0021` n `27`; metal avg `0.0242` n `20`; unknown avg `0.7071` n `1262`
- 1h: commodity avg `-0.0169` n `13`; crypto_alt avg `0.1628` n `239`; crypto_major avg `0.1018` n `8`; equity avg `0.1036` n `160`; fx avg `-0.0005` n `6`; index avg `0.0079` n `27`; metal avg `-0.0273` n `20`; unknown avg `0.8329` n `1240`
- 4h: commodity avg `0.0915` n `13`; crypto_alt avg `0.5511` n `239`; crypto_major avg `1.0802` n `8`; equity avg `1.2507` n `160`; fx avg `0.02` n `6`; index avg `0.1255` n `27`; metal avg `0.1147` n `20`; unknown avg `1.0913` n `1232`
- 24h: commodity avg `0.1542` n `13`; crypto_alt avg `-1.4068` n `239`; crypto_major avg `-2.4767` n `8`; equity avg `-1.3789` n `160`; fx avg `-0.0876` n `6`; index avg `-0.2003` n `27`; metal avg `-0.6777` n `20`; unknown avg `20.3957` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2578`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1985`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
