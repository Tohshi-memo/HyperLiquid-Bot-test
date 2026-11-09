# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T23:52:28.206023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `13`; crypto_alt avg `0.0681` n `239`; crypto_major avg `0.0924` n `8`; equity avg `0.14` n `160`; fx avg `0.0128` n `6`; index avg `-0.0048` n `27`; metal avg `0.0091` n `20`; unknown avg `0.3404` n `1261`
- 1h: commodity avg `-0.0452` n `13`; crypto_alt avg `-0.4813` n `239`; crypto_major avg `-0.204` n `8`; equity avg `0.1318` n `160`; fx avg `0.021` n `6`; index avg `-0.028` n `27`; metal avg `-0.0177` n `20`; unknown avg `0.0218` n `1255`
- 4h: commodity avg `0.2381` n `13`; crypto_alt avg `-0.8408` n `239`; crypto_major avg `0.1518` n `8`; equity avg `0.4269` n `160`; fx avg `0.0624` n `6`; index avg `0.0301` n `27`; metal avg `0.0458` n `20`; unknown avg `-0.0032` n `1207`
- 24h: commodity avg `-0.436` n `13`; crypto_alt avg `1.9309` n `239`; crypto_major avg `0.4751` n `8`; equity avg `5.4682` n `160`; fx avg `-0.0668` n `6`; index avg `0.6766` n `27`; metal avg `0.652` n `20`; unknown avg `5.1154` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
