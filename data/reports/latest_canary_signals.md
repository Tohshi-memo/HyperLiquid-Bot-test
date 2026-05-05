# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T10:54:43.274356+00:00`
- Correlation status: `ready`
- Asset price records: `353`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `7`; crypto_alt avg `-0.0362` n `223`; crypto_major avg `0.1526` n `7`; equity avg `0.0162` n `47`; fx avg `0.0028` n `4`; index avg `-0.0136` n `6`; metal avg `-0.1647` n `7`; unknown avg `1.3044` n `312`
- 1h: commodity avg `0.128` n `7`; crypto_alt avg `0.2422` n `223`; crypto_major avg `0.4091` n `7`; equity avg `-0.0618` n `47`; fx avg `0.0119` n `4`; index avg `0.0314` n `6`; metal avg `-0.2887` n `7`; unknown avg `1.2757` n `312`
- 4h: commodity avg `-0.1142` n `7`; crypto_alt avg `0.574` n `223`; crypto_major avg `0.263` n `7`; equity avg `0.1037` n `47`; fx avg `0.0722` n `4`; index avg `0.0628` n `6`; metal avg `0.1695` n `7`; unknown avg `0.5402` n `312`
- 24h: commodity avg `0.1946` n `7`; crypto_alt avg `2.146` n `223`; crypto_major avg `1.6511` n `7`; equity avg `0.6878` n `47`; fx avg `0.0457` n `4`; index avg `0.3694` n `6`; metal avg `0.3691` n `7`; unknown avg `0.8061` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2171`, n `349`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2099`, n `349`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `349`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `349`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `349`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `349`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `349`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `349`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `345`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0986`, n `345`, weak_sample_signal
