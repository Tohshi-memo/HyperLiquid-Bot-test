# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T07:22:31.489652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1429` n `13`; crypto_alt avg `-0.1598` n `239`; crypto_major avg `-0.0056` n `8`; equity avg `-0.1127` n `158`; fx avg `-0.0032` n `6`; index avg `-0.009` n `27`; metal avg `-0.045` n `20`; unknown avg `-0.0794` n `1263`
- 1h: commodity avg `-0.1268` n `13`; crypto_alt avg `-0.714` n `239`; crypto_major avg `-0.5725` n `8`; equity avg `-0.5689` n `158`; fx avg `-0.0111` n `6`; index avg `-0.0471` n `27`; metal avg `-0.1819` n `20`; unknown avg `3.2826` n `1255`
- 4h: commodity avg `-0.394` n `13`; crypto_alt avg `-1.2947` n `239`; crypto_major avg `-1.2586` n `8`; equity avg `-1.4373` n `158`; fx avg `-0.0981` n `6`; index avg `-0.1586` n `27`; metal avg `-0.2464` n `20`; unknown avg `8.0556` n `1210`
- 24h: commodity avg `-0.277` n `13`; crypto_alt avg `-3.152` n `239`; crypto_major avg `-3.7604` n `8`; equity avg `-0.9465` n `158`; fx avg `-0.1822` n `6`; index avg `-0.1091` n `27`; metal avg `0.2252` n `20`; unknown avg `1.2545` n `982`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
