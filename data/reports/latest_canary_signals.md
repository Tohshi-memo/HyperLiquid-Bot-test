# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T06:52:31.393232+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.079` n `13`; crypto_alt avg `-0.1282` n `239`; crypto_major avg `-0.047` n `8`; equity avg `-0.3295` n `168`; fx avg `-0.0031` n `6`; index avg `-0.0164` n `27`; metal avg `-0.0168` n `20`; unknown avg `0.4362` n `1263`
- 1h: commodity avg `-0.0915` n `13`; crypto_alt avg `-0.0145` n `239`; crypto_major avg `-0.0731` n `8`; equity avg `-0.2308` n `168`; fx avg `-0.0129` n `6`; index avg `-0.0229` n `27`; metal avg `0.0821` n `20`; unknown avg `1.2248` n `1237`
- 4h: commodity avg `0.0144` n `13`; crypto_alt avg `0.3997` n `239`; crypto_major avg `0.8229` n `8`; equity avg `1.3634` n `168`; fx avg `-0.0509` n `6`; index avg `0.0878` n `27`; metal avg `0.3583` n `20`; unknown avg `57.1201` n `1219`
- 24h: commodity avg `0.5269` n `13`; crypto_alt avg `2.4082` n `239`; crypto_major avg `2.9446` n `8`; equity avg `3.9058` n `168`; fx avg `0.0054` n `6`; index avg `0.3468` n `27`; metal avg `1.2516` n `20`; unknown avg `218.7893` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
