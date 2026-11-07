# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T03:52:37.329320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0199` n `13`; crypto_alt avg `0.0306` n `239`; crypto_major avg `0.0442` n `8`; equity avg `0.0507` n `158`; fx avg `0.0089` n `6`; index avg `0.0102` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.136` n `1261`
- 1h: commodity avg `-0.0896` n `13`; crypto_alt avg `-0.3511` n `239`; crypto_major avg `-0.2878` n `8`; equity avg `0.1729` n `158`; fx avg `0.0065` n `6`; index avg `0.0114` n `27`; metal avg `0.0009` n `20`; unknown avg `11.2047` n `1249`
- 4h: commodity avg `-0.1322` n `13`; crypto_alt avg `-0.4105` n `239`; crypto_major avg `-0.2589` n `8`; equity avg `0.1124` n `158`; fx avg `-0.0121` n `6`; index avg `0.017` n `27`; metal avg `0.0119` n `20`; unknown avg `3.8287` n `1243`
- 24h: commodity avg `-0.372` n `13`; crypto_alt avg `0.1942` n `239`; crypto_major avg `-0.1138` n `8`; equity avg `1.2465` n `158`; fx avg `-0.065` n `6`; index avg `0.174` n `27`; metal avg `0.2474` n `20`; unknown avg `8.0299` n `1016`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
