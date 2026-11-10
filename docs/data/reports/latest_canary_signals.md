# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T03:37:25.550478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `-0.0187` n `239`; crypto_major avg `-0.0522` n `8`; equity avg `-0.2152` n `160`; fx avg `0.0001` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0396` n `20`; unknown avg `0.0539` n `1261`
- 1h: commodity avg `-0.118` n `13`; crypto_alt avg `-0.0004` n `239`; crypto_major avg `-0.1926` n `8`; equity avg `-0.4903` n `160`; fx avg `-0.0247` n `6`; index avg `-0.0605` n `27`; metal avg `-0.0057` n `20`; unknown avg `-0.1218` n `1251`
- 4h: commodity avg `-0.1848` n `13`; crypto_alt avg `-0.2599` n `239`; crypto_major avg `-0.7029` n `8`; equity avg `-0.7043` n `160`; fx avg `0.0487` n `6`; index avg `-0.1423` n `27`; metal avg `-0.0933` n `20`; unknown avg `0.2513` n `1243`
- 24h: commodity avg `-0.7572` n `13`; crypto_alt avg `0.3216` n `239`; crypto_major avg `-0.8954` n `8`; equity avg `2.7823` n `160`; fx avg `0.0253` n `6`; index avg `0.2533` n `27`; metal avg `0.0516` n `20`; unknown avg `184.3847` n `1071`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
