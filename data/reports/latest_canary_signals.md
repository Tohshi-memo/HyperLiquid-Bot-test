# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T19:52:27.539047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `13`; crypto_alt avg `0.081` n `239`; crypto_major avg `0.0808` n `8`; equity avg `0.0323` n `168`; fx avg `-0.0083` n `6`; index avg `0.0022` n `27`; metal avg `0.0068` n `20`; unknown avg `0.068` n `1268`
- 1h: commodity avg `0.0205` n `13`; crypto_alt avg `-0.2169` n `239`; crypto_major avg `-0.1484` n `8`; equity avg `0.0104` n `168`; fx avg `0.0043` n `6`; index avg `0.012` n `27`; metal avg `0.0144` n `20`; unknown avg `1.0018` n `1258`
- 4h: commodity avg `0.0754` n `13`; crypto_alt avg `-0.4742` n `239`; crypto_major avg `-0.3046` n `8`; equity avg `0.0911` n `168`; fx avg `-0.0102` n `6`; index avg `0.0127` n `27`; metal avg `0.0206` n `20`; unknown avg `42.0128` n `1209`
- 24h: commodity avg `-0.031` n `13`; crypto_alt avg `-3.2262` n `239`; crypto_major avg `-1.3576` n `8`; equity avg `-0.0241` n `168`; fx avg `-0.0132` n `6`; index avg `-0.0013` n `27`; metal avg `0.0923` n `20`; unknown avg `0.193` n `1069`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
