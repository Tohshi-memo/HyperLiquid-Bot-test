# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T09:39:02.679721+00:00`
- Correlation status: `ready`
- Asset price records: `442`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4355` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.1851` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.4609` n `7`; crypto_alt avg `0.082` n `223`; crypto_major avg `0.3566` n `7`; equity avg `0.1657` n `47`; fx avg `-0.0013` n `4`; index avg `0.0908` n `6`; metal avg `0.2024` n `7`; unknown avg `-0.115` n `313`
- 1h: commodity avg `-1.581` n `7`; crypto_alt avg `0.4968` n `223`; crypto_major avg `0.6041` n `7`; equity avg `0.5763` n `47`; fx avg `-0.0517` n `4`; index avg `0.5937` n `6`; metal avg `0.7276` n `7`; unknown avg `0.0658` n `313`
- 4h: commodity avg `-2.1005` n `7`; crypto_alt avg `1.6774` n `223`; crypto_major avg `1.335` n `7`; equity avg `0.8481` n `47`; fx avg `-0.1221` n `4`; index avg `0.7545` n `6`; metal avg `1.0855` n `7`; unknown avg `1.1034` n `311`
- 24h: commodity avg `-3.2489` n `7`; crypto_alt avg `3.7277` n `223`; crypto_major avg `3.0426` n `7`; equity avg `3.322` n `47`; fx avg `-0.5508` n `4`; index avg `2.9104` n `6`; metal avg `2.7602` n `7`; unknown avg `1.9165` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1731`, n `438`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.167`, n `438`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1425`, n `438`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1284`, n `438`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `438`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `438`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `434`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0962`, n `434`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `434`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `438`, weak_sample_signal
