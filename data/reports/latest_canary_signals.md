# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T00:22:27.493541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0297` n `13`; crypto_alt avg `-0.2943` n `239`; crypto_major avg `-0.3018` n `8`; equity avg `-0.0629` n `160`; fx avg `0.0014` n `6`; index avg `-0.0136` n `27`; metal avg `-0.038` n `20`; unknown avg `0.2604` n `1261`
- 1h: commodity avg `0.0696` n `13`; crypto_alt avg `-0.0919` n `239`; crypto_major avg `-0.0925` n `8`; equity avg `0.2063` n `160`; fx avg `0.0294` n `6`; index avg `-0.0472` n `27`; metal avg `-0.1174` n `20`; unknown avg `-0.0558` n `1249`
- 4h: commodity avg `0.0859` n `13`; crypto_alt avg `-1.052` n `239`; crypto_major avg `-0.1535` n `8`; equity avg `-0.0664` n `160`; fx avg `0.0836` n `6`; index avg `-0.0547` n `27`; metal avg `-0.1155` n `20`; unknown avg `-0.2768` n `1209`
- 24h: commodity avg `-0.3261` n `13`; crypto_alt avg `1.2971` n `239`; crypto_major avg `-0.0168` n `8`; equity avg `5.4916` n `160`; fx avg `0.0191` n `6`; index avg `0.6074` n `27`; metal avg `0.445` n `20`; unknown avg `5.0083` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
