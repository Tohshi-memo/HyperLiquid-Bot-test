# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T02:15:36.813359+00:00`
- Correlation status: `ready`
- Asset price records: `413`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7501` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0117` n `7`; crypto_alt avg `-0.0597` n `223`; crypto_major avg `0.0082` n `7`; equity avg `-0.0512` n `47`; fx avg `0.0267` n `4`; index avg `-0.0337` n `6`; metal avg `0.0563` n `7`; unknown avg `0.1749` n `313`
- 1h: commodity avg `-0.2475` n `7`; crypto_alt avg `0.5573` n `223`; crypto_major avg `0.2568` n `7`; equity avg `0.1487` n `47`; fx avg `0.0095` n `4`; index avg `-0.0674` n `6`; metal avg `0.4687` n `7`; unknown avg `0.0226` n `313`
- 4h: commodity avg `-0.6194` n `7`; crypto_alt avg `0.6982` n `223`; crypto_major avg `-0.113` n `7`; equity avg `0.5426` n `47`; fx avg `-0.2678` n `4`; index avg `0.633` n `6`; metal avg `1.6371` n `7`; unknown avg `-0.0253` n `313`
- 24h: commodity avg `-1.5455` n `7`; crypto_alt avg `2.5047` n `223`; crypto_major avg `2.0933` n `7`; equity avg `2.7525` n `47`; fx avg `-0.1886` n `4`; index avg `2.2799` n `6`; metal avg `1.7603` n `7`; unknown avg `1.4142` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1852`, n `409`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1789`, n `409`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `409`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `409`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `409`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `409`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1016`, n `405`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `409`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `409`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0958`, n `405`, weak_sample_signal
