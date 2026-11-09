# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T22:52:36.399947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `-0.0821` n `239`; crypto_major avg `0.0474` n `8`; equity avg `0.0573` n `160`; fx avg `0.0178` n `6`; index avg `0.011` n `27`; metal avg `0.0064` n `20`; unknown avg `0.232` n `1261`
- 1h: commodity avg `0.0757` n `13`; crypto_alt avg `-0.0245` n `239`; crypto_major avg `0.3296` n `8`; equity avg `-0.0361` n `160`; fx avg `0.0127` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0203` n `20`; unknown avg `18.9362` n `1247`
- 4h: commodity avg `-0.2733` n `13`; crypto_alt avg `-0.1483` n `239`; crypto_major avg `0.6282` n `8`; equity avg `0.3842` n `160`; fx avg `0.003` n `6`; index avg `0.084` n `27`; metal avg `0.2441` n `20`; unknown avg `-0.0369` n `1205`
- 24h: commodity avg `-0.494` n `13`; crypto_alt avg `2.4989` n `239`; crypto_major avg `0.6531` n `8`; equity avg `5.258` n `160`; fx avg `-0.098` n `6`; index avg `0.6972` n `27`; metal avg `0.7631` n `20`; unknown avg `5.4318` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
