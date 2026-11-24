# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T20:07:34.746690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0574` n `13`; crypto_alt avg `-0.3501` n `239`; crypto_major avg `-0.2006` n `8`; equity avg `-0.3379` n `168`; fx avg `0.0019` n `6`; index avg `-0.042` n `27`; metal avg `-0.0534` n `20`; unknown avg `22.0516` n `1249`
- 1h: commodity avg `-0.1142` n `13`; crypto_alt avg `-0.541` n `239`; crypto_major avg `-0.4048` n `8`; equity avg `-0.3798` n `168`; fx avg `-0.0246` n `6`; index avg `-0.0491` n `27`; metal avg `-0.0507` n `20`; unknown avg `17.4919` n `1247`
- 4h: commodity avg `0.2576` n `13`; crypto_alt avg `-0.0866` n `239`; crypto_major avg `0.0541` n `8`; equity avg `0.7259` n `168`; fx avg `0.0029` n `6`; index avg `0.1201` n `27`; metal avg `0.0344` n `20`; unknown avg `20.0544` n `1223`
- 24h: commodity avg `0.6784` n `13`; crypto_alt avg `-3.5198` n `239`; crypto_major avg `-3.207` n `8`; equity avg `-3.8319` n `167`; fx avg `0.2369` n `6`; index avg `-0.2399` n `27`; metal avg `-1.1218` n `20`; unknown avg `21.5235` n `1109`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
