# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T11:37:25.536757+00:00`
- Correlation status: `ready`
- Asset price records: `450`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.6355` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0873` n `7`; crypto_alt avg `-0.0216` n `223`; crypto_major avg `-0.0225` n `7`; equity avg `0.0308` n `47`; fx avg `0.0113` n `4`; index avg `0.0037` n `6`; metal avg `0.0452` n `7`; unknown avg `0.0082` n `313`
- 1h: commodity avg `-0.9379` n `7`; crypto_alt avg `0.0993` n `223`; crypto_major avg `0.4525` n `7`; equity avg `0.4687` n `47`; fx avg `-0.0064` n `4`; index avg `0.1569` n `6`; metal avg `0.109` n `7`; unknown avg `0.08` n `313`
- 4h: commodity avg `-3.1508` n `7`; crypto_alt avg `1.3632` n `223`; crypto_major avg `1.4847` n `7`; equity avg `1.5403` n `47`; fx avg `-0.2197` n `4`; index avg `1.2311` n `6`; metal avg `1.4902` n `7`; unknown avg `0.2537` n `313`
- 24h: commodity avg `-4.5971` n `7`; crypto_alt avg `4.0176` n `223`; crypto_major avg `3.2857` n `7`; equity avg `4.0019` n `47`; fx avg `-0.6516` n `4`; index avg `3.3565` n `6`; metal avg `3.1957` n `7`; unknown avg `2.2037` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1675`, n `446`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1614`, n `446`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `446`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `446`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `446`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `446`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1157`, n `442`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `442`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0996`, n `442`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `442`, weak_sample_signal
