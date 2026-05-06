# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T00:45:24.723605+00:00`
- Correlation status: `ready`
- Asset price records: `407`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1231` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0504` n `7`; crypto_alt avg `-0.0286` n `223`; crypto_major avg `0.0677` n `7`; equity avg `0.0944` n `47`; fx avg `-0.0437` n `4`; index avg `0.3399` n `6`; metal avg `0.1187` n `7`; unknown avg `-0.0004` n `313`
- 1h: commodity avg `0.3294` n `7`; crypto_alt avg `0.0354` n `223`; crypto_major avg `-0.0325` n `7`; equity avg `0.0032` n `47`; fx avg `-0.3018` n `4`; index avg `0.3529` n `6`; metal avg `0.1717` n `7`; unknown avg `0.2405` n `313`
- 4h: commodity avg `-0.4765` n `7`; crypto_alt avg `-0.4775` n `223`; crypto_major avg `-0.5591` n `7`; equity avg `0.6013` n `47`; fx avg `-0.1613` n `4`; index avg `0.564` n `6`; metal avg `0.9124` n `7`; unknown avg `0.1352` n `313`
- 24h: commodity avg `-1.4981` n `7`; crypto_alt avg `1.9546` n `223`; crypto_major avg `1.9631` n `7`; equity avg `2.6771` n `47`; fx avg `-0.2021` n `4`; index avg `2.2516` n `6`; metal avg `1.4775` n `7`; unknown avg `1.3494` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1921`, n `403`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1859`, n `403`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `403`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `403`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `403`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1051`, n `399`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `403`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `403`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `403`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0977`, n `399`, weak_sample_signal
