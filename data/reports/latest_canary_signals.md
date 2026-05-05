# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T21:15:22.531652+00:00`
- Correlation status: `ready`
- Asset price records: `393`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0823` n `7`; crypto_alt avg `0.1411` n `223`; crypto_major avg `0.067` n `7`; equity avg `0.1848` n `47`; fx avg `0.0022` n `4`; index avg `0.0484` n `6`; metal avg `0.0589` n `7`; unknown avg `-0.0439` n `313`
- 1h: commodity avg `0.1453` n `7`; crypto_alt avg `0.7296` n `223`; crypto_major avg `0.2407` n `7`; equity avg `0.4106` n `47`; fx avg `-0.0058` n `4`; index avg `0.1554` n `6`; metal avg `0.0738` n `7`; unknown avg `0.1903` n `313`
- 4h: commodity avg `0.0116` n `7`; crypto_alt avg `1.4466` n `223`; crypto_major avg `0.9387` n `7`; equity avg `0.3693` n `47`; fx avg `0.0061` n `4`; index avg `0.2507` n `6`; metal avg `-0.0902` n `7`; unknown avg `0.2274` n `313`
- 24h: commodity avg `-1.1308` n `7`; crypto_alt avg `2.7555` n `223`; crypto_major avg `2.6754` n `7`; equity avg `2.2626` n `47`; fx avg `-0.0399` n `4`; index avg `1.5301` n `6`; metal avg `0.6889` n `7`; unknown avg `1.5568` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2067`, n `389`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1999`, n `389`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `389`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `389`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1115`, n `385`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `389`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.107`, n `389`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1035`, n `385`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `389`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `389`, weak_sample_signal
