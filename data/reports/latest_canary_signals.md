# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T22:07:34.814534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2612` n `12`; crypto_alt avg `-0.0441` n `230`; crypto_major avg `0.0097` n `8`; equity avg `-0.0207` n `102`; fx avg `-0.0124` n `6`; index avg `0.016` n `25`; metal avg `-0.0024` n `20`; unknown avg `1.2415` n `781`
- 1h: commodity avg `0.0409` n `12`; crypto_alt avg `-0.1162` n `230`; crypto_major avg `-0.0953` n `8`; equity avg `-0.2295` n `102`; fx avg `0.0196` n `6`; index avg `0.0056` n `25`; metal avg `0.0106` n `20`; unknown avg `1.9238` n `781`
- 4h: commodity avg `0.5084` n `12`; crypto_alt avg `-0.6462` n `230`; crypto_major avg `-0.6398` n `8`; equity avg `-1.0433` n `102`; fx avg `-0.0737` n `6`; index avg `-0.1384` n `25`; metal avg `-0.0604` n `20`; unknown avg `1.6483` n `780`
- 24h: commodity avg `0.6513` n `12`; crypto_alt avg `-0.8359` n `230`; crypto_major avg `-2.3641` n `8`; equity avg `-1.5656` n `102`; fx avg `0.0964` n `6`; index avg `0.0313` n `25`; metal avg `-0.4264` n `20`; unknown avg `2.5002` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
