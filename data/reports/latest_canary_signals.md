# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T23:52:35.720921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `13`; crypto_alt avg `0.1447` n `239`; crypto_major avg `0.0325` n `8`; equity avg `0.0373` n `160`; fx avg `-0.0159` n `6`; index avg `0.0018` n `27`; metal avg `0.0143` n `20`; unknown avg `0.1224` n `1262`
- 1h: commodity avg `-0.0167` n `13`; crypto_alt avg `0.1483` n `239`; crypto_major avg `0.0261` n `8`; equity avg `0.4248` n `160`; fx avg `-0.0008` n `6`; index avg `0.04` n `27`; metal avg `0.0441` n `20`; unknown avg `18.9284` n `1256`
- 4h: commodity avg `-0.0013` n `13`; crypto_alt avg `0.541` n `239`; crypto_major avg `0.1739` n `8`; equity avg `1.0338` n `160`; fx avg `0.0004` n `6`; index avg `0.0807` n `27`; metal avg `0.0462` n `20`; unknown avg `20.79` n `1226`
- 24h: commodity avg `0.0891` n `13`; crypto_alt avg `-0.5973` n `239`; crypto_major avg `-2.7189` n `8`; equity avg `-1.1312` n `160`; fx avg `-0.1235` n `6`; index avg `-0.1398` n `27`; metal avg `-0.6028` n `20`; unknown avg `20.9586` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2584`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
