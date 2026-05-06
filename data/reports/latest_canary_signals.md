# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T11:31:40.600447+00:00`
- Correlation status: `ready`
- Asset price records: `450`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.4647` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0237` n `7`; crypto_alt avg `-0.0541` n `223`; crypto_major avg `-0.0911` n `7`; equity avg `-0.0554` n `47`; fx avg `0.0047` n `4`; index avg `-0.0196` n `6`; metal avg `-0.0785` n `7`; unknown avg `-0.0031` n `313`
- 1h: commodity avg `-0.8293` n `7`; crypto_alt avg `0.0668` n `223`; crypto_major avg `0.3835` n `7`; equity avg `0.3822` n `47`; fx avg `-0.013` n `4`; index avg `0.1335` n `6`; metal avg `-0.0148` n `7`; unknown avg `0.0626` n `313`
- 4h: commodity avg `-3.0495` n `7`; crypto_alt avg `1.3303` n `223`; crypto_major avg `1.4152` n `7`; equity avg `1.4529` n `47`; fx avg `-0.2263` n `4`; index avg `1.2075` n `6`; metal avg `1.3643` n `7`; unknown avg `0.2299` n `313`
- 24h: commodity avg `-4.4999` n `7`; crypto_alt avg `3.9893` n `223`; crypto_major avg `3.2147` n `7`; equity avg `3.9107` n `47`; fx avg `-0.6582` n `4`; index avg `3.3325` n `6`; metal avg `3.0669` n `7`; unknown avg `2.1778` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1676`, n `446`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1615`, n `446`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1513`, n `446`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `446`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1199`, n `446`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `446`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1159`, n `442`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `442`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `442`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `442`, weak_sample_signal
