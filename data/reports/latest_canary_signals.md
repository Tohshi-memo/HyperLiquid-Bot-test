# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T10:37:21.243664+00:00`
- Correlation status: `ready`
- Asset price records: `446`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7722` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.2492` n `7`; crypto_alt avg `0.0402` n `223`; crypto_major avg `0.0685` n `7`; equity avg `0.1941` n `47`; fx avg `-0.0704` n `4`; index avg `0.2519` n `6`; metal avg `0.1282` n `7`; unknown avg `-0.2117` n `313`
- 1h: commodity avg `-0.3371` n `7`; crypto_alt avg `0.2763` n `223`; crypto_major avg `0.218` n `7`; equity avg `0.1657` n `47`; fx avg `-0.0649` n `4`; index avg `0.2462` n `6`; metal avg `0.3583` n `7`; unknown avg `0.1272` n `313`
- 4h: commodity avg `-2.2575` n `7`; crypto_alt avg `1.9159` n `223`; crypto_major avg `1.5147` n `7`; equity avg `1.0471` n `47`; fx avg `-0.1666` n `4`; index avg `0.9263` n `6`; metal avg `1.2728` n `7`; unknown avg `0.7741` n `313`
- 24h: commodity avg `-3.6169` n `7`; crypto_alt avg `3.9361` n `223`; crypto_major avg `3.1704` n `7`; equity avg `3.629` n `47`; fx avg `-0.6343` n `4`; index avg `3.0842` n `6`; metal avg `3.1424` n `7`; unknown avg `2.3184` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1692`, n `442`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1631`, n `442`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `442`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1383`, n `442`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `442`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `442`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1141`, n `438`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `438`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0966`, n `438`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `438`, weak_sample_signal
