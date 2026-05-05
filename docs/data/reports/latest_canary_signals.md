# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T08:45:40.055388+00:00`
- Correlation status: `ready`
- Asset price records: `345`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0457` n `7`; crypto_alt avg `-0.1604` n `223`; crypto_major avg `-0.1198` n `7`; equity avg `0.0176` n `47`; fx avg `-0.015` n `4`; index avg `0.047` n `6`; metal avg `0.0374` n `7`; unknown avg `-0.1368` n `312`
- 1h: commodity avg `-0.0674` n `7`; crypto_alt avg `-0.1389` n `223`; crypto_major avg `-0.2495` n `7`; equity avg `0.042` n `47`; fx avg `0.0009` n `4`; index avg `0.1891` n `6`; metal avg `-0.0203` n `7`; unknown avg `-0.1129` n `312`
- 4h: commodity avg `-0.1468` n `7`; crypto_alt avg `0.4316` n `223`; crypto_major avg `0.3225` n `7`; equity avg `0.736` n `47`; fx avg `0.0053` n `4`; index avg `0.3231` n `6`; metal avg `0.6315` n `7`; unknown avg `0.3778` n `310`
- 24h: commodity avg `0.3525` n `7`; crypto_alt avg `1.2449` n `223`; crypto_major avg `0.5708` n `7`; equity avg `0.1028` n `47`; fx avg `-0.0183` n `4`; index avg `0.0384` n `6`; metal avg `-0.1471` n `7`; unknown avg `-0.8427` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2185`, n `341`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2115`, n `341`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1387`, n `341`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `341`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `341`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `341`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `341`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `341`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `337`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0965`, n `337`, weak_sample_signal
