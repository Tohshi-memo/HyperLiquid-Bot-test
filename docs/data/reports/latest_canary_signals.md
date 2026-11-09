# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T11:22:26.565035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.305` n `13`; crypto_alt avg `0.6476` n `239`; crypto_major avg `0.7371` n `8`; equity avg `0.2913` n `158`; fx avg `-0.0443` n `6`; index avg `0.033` n `27`; metal avg `0.0181` n `20`; unknown avg `0.8245` n `1263`
- 1h: commodity avg `-0.4377` n `13`; crypto_alt avg `0.3941` n `239`; crypto_major avg `0.4995` n `8`; equity avg `-0.0644` n `158`; fx avg `-0.0547` n `6`; index avg `0.0143` n `27`; metal avg `-0.0205` n `20`; unknown avg `1.2512` n `1255`
- 4h: commodity avg `-0.2946` n `13`; crypto_alt avg `1.7992` n `239`; crypto_major avg `0.6587` n `8`; equity avg `0.9682` n `158`; fx avg `0.0331` n `6`; index avg `0.1153` n `27`; metal avg `0.0649` n `20`; unknown avg `249.3905` n `1129`
- 24h: commodity avg `-0.593` n `13`; crypto_alt avg `-1.5631` n `239`; crypto_major avg `-3.3771` n `8`; equity avg `-0.2305` n `158`; fx avg `-0.1526` n `6`; index avg `0.0017` n `27`; metal avg `0.2823` n `20`; unknown avg `0.7608` n `1028`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
