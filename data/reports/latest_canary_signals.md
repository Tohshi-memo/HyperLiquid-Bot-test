# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T01:07:26.454696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `0.0828` n `239`; crypto_major avg `0.2843` n `8`; equity avg `-0.0564` n `160`; fx avg `0.0049` n `6`; index avg `-0.0102` n `27`; metal avg `0.1464` n `20`; unknown avg `1.7939` n `1257`
- 1h: commodity avg `0.0481` n `13`; crypto_alt avg `-0.1551` n `239`; crypto_major avg `-0.1229` n `8`; equity avg `-0.6323` n `160`; fx avg `-0.0041` n `6`; index avg `-0.0888` n `27`; metal avg `0.061` n `20`; unknown avg `2.6363` n `1255`
- 4h: commodity avg `-0.0623` n `13`; crypto_alt avg `-0.4048` n `239`; crypto_major avg `0.2209` n `8`; equity avg `-0.0525` n `160`; fx avg `0.0613` n `6`; index avg `-0.111` n `27`; metal avg `0.0399` n `20`; unknown avg `1.8729` n `1235`
- 24h: commodity avg `-0.3011` n `13`; crypto_alt avg `0.5665` n `239`; crypto_major avg `-0.5446` n `8`; equity avg `4.2414` n `160`; fx avg `-0.0245` n `6`; index avg `0.4041` n `27`; metal avg `0.2861` n `20`; unknown avg `5.9549` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
