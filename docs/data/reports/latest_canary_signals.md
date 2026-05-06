# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T10:30:32.434571+00:00`
- Correlation status: `ready`
- Asset price records: `446`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6658` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0966` n `7`; crypto_alt avg `0.0686` n `223`; crypto_major avg `0.1057` n `7`; equity avg `0.1592` n `47`; fx avg `-0.052` n `4`; index avg `0.0676` n `6`; metal avg `0.151` n `7`; unknown avg `-0.0561` n `313`
- 1h: commodity avg `-0.1853` n `7`; crypto_alt avg `0.3046` n `223`; crypto_major avg `0.2553` n `7`; equity avg `0.1306` n `47`; fx avg `-0.0466` n `4`; index avg `0.0621` n `6`; metal avg `0.3812` n `7`; unknown avg `1.0782` n `313`
- 4h: commodity avg `-2.1137` n `7`; crypto_alt avg `1.9439` n `223`; crypto_major avg `1.5521` n `7`; equity avg `1.0123` n `47`; fx avg `-0.1484` n `4`; index avg `0.7392` n `6`; metal avg `1.2959` n `7`; unknown avg `1.7147` n `313`
- 24h: commodity avg `-3.4782` n `7`; crypto_alt avg `3.9597` n `223`; crypto_major avg `3.2084` n `7`; equity avg `3.592` n `47`; fx avg `-0.6163` n `4`; index avg `2.8824` n `6`; metal avg `3.1659` n `7`; unknown avg `3.2804` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1691`, n `442`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.163`, n `442`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `442`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1384`, n `442`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `442`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `442`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1136`, n `438`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `438`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0961`, n `438`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.094`, n `438`, weak_sample_signal
