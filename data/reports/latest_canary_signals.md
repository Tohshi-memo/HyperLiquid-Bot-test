# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T05:00:31.784311+00:00`
- Correlation status: `ready`
- Asset price records: `235`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.6257` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.3863` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.9212` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.052` n `7`; crypto_alt avg `-0.0846` n `223`; crypto_major avg `-0.1461` n `7`; equity avg `-0.0906` n `42`; fx avg `0.0072` n `4`; index avg `0.0104` n `9`; metal avg `-0.0729` n `7`; unknown avg `-0.0054` n `314`
- 1h: commodity avg `0.1494` n `7`; crypto_alt avg `0.1254` n `223`; crypto_major avg `0.3664` n `7`; equity avg `-0.2508` n `42`; fx avg `0.0016` n `4`; index avg `0.0025` n `9`; metal avg `-0.0881` n `7`; unknown avg `-0.3316` n `314`
- 4h: commodity avg `0.2398` n `7`; crypto_alt avg `2.0751` n `223`; crypto_major avg `2.6261` n `7`; equity avg `0.7049` n `42`; fx avg `-0.0265` n `4`; index avg `0.6467` n `9`; metal avg `0.0004` n `7`; unknown avg `0.1056` n `314`
- 24h: commodity avg `0.1008` n `7`; crypto_alt avg `2.9103` n `223`; crypto_major avg `3.2728` n `7`; equity avg `1.1501` n `42`; fx avg `-0.0482` n `4`; index avg `0.8578` n `9`; metal avg `0.2227` n `7`; unknown avg `0.5328` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3963`, n `227`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3861`, n `227`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3662`, n `231`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3507`, n `231`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2031`, n `231`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1927`, n `227`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1907`, n `227`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1787`, n `231`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1738`, n `231`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1678`, n `227`, weak_sample_signal
