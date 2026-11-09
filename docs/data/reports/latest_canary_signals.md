# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T08:22:37.479511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0851` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0647` n `13`; crypto_alt avg `0.7501` n `239`; crypto_major avg `0.6338` n `8`; equity avg `0.3986` n `158`; fx avg `0.0296` n `6`; index avg `0.0505` n `27`; metal avg `0.0204` n `20`; unknown avg `0.3052` n `1241`
- 1h: commodity avg `-0.0218` n `13`; crypto_alt avg `0.3599` n `239`; crypto_major avg `0.1949` n `8`; equity avg `0.0318` n `158`; fx avg `0.0629` n `6`; index avg `-0.0121` n `27`; metal avg `-0.0157` n `20`; unknown avg `-0.0214` n `1153`
- 4h: commodity avg `-0.4887` n `13`; crypto_alt avg `-0.9754` n `239`; crypto_major avg `-1.2434` n `8`; equity avg `-1.1657` n `158`; fx avg `-0.0171` n `6`; index avg `-0.1583` n `27`; metal avg `-0.284` n `20`; unknown avg `0.2064` n `1131`
- 24h: commodity avg `-0.3203` n `13`; crypto_alt avg `-2.7571` n `239`; crypto_major avg `-3.59` n `8`; equity avg `-0.953` n `158`; fx avg `-0.122` n `6`; index avg `-0.1544` n `27`; metal avg `0.2013` n `20`; unknown avg `0.9724` n `954`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
