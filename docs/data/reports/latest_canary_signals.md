# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T18:22:29.918882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `0.1233` n `239`; crypto_major avg `0.1263` n `8`; equity avg `0.0484` n `168`; fx avg `-0.001` n `6`; index avg `0.0008` n `27`; metal avg `0.0023` n `20`; unknown avg `13.4885` n `1268`
- 1h: commodity avg `-0.0234` n `13`; crypto_alt avg `-0.0523` n `239`; crypto_major avg `-0.2524` n `8`; equity avg `-0.0128` n `168`; fx avg `-0.0022` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0159` n `20`; unknown avg `37808.4366` n `1238`
- 4h: commodity avg `-0.0714` n `13`; crypto_alt avg `-0.7821` n `239`; crypto_major avg `-0.1249` n `8`; equity avg `0.0289` n `168`; fx avg `-0.0008` n `6`; index avg `0.0032` n `27`; metal avg `-0.025` n `20`; unknown avg `50.0089` n `1207`
- 24h: commodity avg `-0.1237` n `13`; crypto_alt avg `-3.2884` n `239`; crypto_major avg `-1.4071` n `8`; equity avg `-0.4783` n `168`; fx avg `-0.0107` n `6`; index avg `-0.0429` n `27`; metal avg `0.1133` n `20`; unknown avg `196.5046` n `1052`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
