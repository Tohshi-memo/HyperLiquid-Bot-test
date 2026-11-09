# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T22:22:33.135327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0558` n `13`; crypto_alt avg `0.002` n `239`; crypto_major avg `0.0282` n `8`; equity avg `-0.103` n `160`; fx avg `-0.0106` n `6`; index avg `-0.0068` n `27`; metal avg `-0.0151` n `20`; unknown avg `-0.0368` n `1261`
- 1h: commodity avg `-0.0431` n `13`; crypto_alt avg `-0.1018` n `239`; crypto_major avg `-0.0343` n `8`; equity avg `0.2679` n `160`; fx avg `-0.0009` n `6`; index avg `0.0291` n `27`; metal avg `0.0227` n `20`; unknown avg `18.9859` n `1247`
- 4h: commodity avg `-0.2373` n `13`; crypto_alt avg `-0.508` n `239`; crypto_major avg `-0.0197` n `8`; equity avg `0.4759` n `160`; fx avg `-0.0036` n `6`; index avg `0.0963` n `27`; metal avg `0.2886` n `20`; unknown avg `-0.1904` n `1205`
- 24h: commodity avg `-0.5063` n `13`; crypto_alt avg `2.2354` n `239`; crypto_major avg `0.0685` n `8`; equity avg `5.0854` n `160`; fx avg `-0.1064` n `6`; index avg `0.6428` n `27`; metal avg `0.7506` n `20`; unknown avg `4.9799` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
