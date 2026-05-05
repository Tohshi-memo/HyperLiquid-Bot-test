# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T17:00:42.265683+00:00`
- Correlation status: `ready`
- Asset price records: `376`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0889` n `7`; crypto_alt avg `0.1352` n `223`; crypto_major avg `0.1276` n `7`; equity avg `0.1601` n `47`; fx avg `-0.0072` n `4`; index avg `0.0548` n `6`; metal avg `0.0366` n `7`; unknown avg `0.0141` n `313`
- 1h: commodity avg `0.1295` n `7`; crypto_alt avg `-0.1664` n `223`; crypto_major avg `-0.3338` n `7`; equity avg `-0.0676` n `47`; fx avg `-0.0214` n `4`; index avg `0.014` n `6`; metal avg `-0.1096` n `7`; unknown avg `-0.2933` n `313`
- 4h: commodity avg `-0.4516` n `7`; crypto_alt avg `-0.4535` n `223`; crypto_major avg `-0.1645` n `7`; equity avg `0.332` n `47`; fx avg `-0.1463` n `4`; index avg `0.5686` n `6`; metal avg `-0.2303` n `7`; unknown avg `0.3451` n `312`
- 24h: commodity avg `-1.4631` n `7`; crypto_alt avg `1.5303` n `223`; crypto_major avg `1.7565` n `7`; equity avg `1.4743` n `47`; fx avg `-0.047` n `4`; index avg `1.3397` n `6`; metal avg `1.1122` n `7`; unknown avg `0.8306` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2071`, n `372`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2003`, n `372`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `372`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `372`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `372`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1076`, n `368`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `372`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `372`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `372`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `368`, weak_sample_signal
