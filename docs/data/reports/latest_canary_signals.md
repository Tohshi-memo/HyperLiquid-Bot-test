# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T06:30:27.373906+00:00`
- Correlation status: `ready`
- Asset price records: `430`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `7`; crypto_alt avg `0.2167` n `223`; crypto_major avg `0.0141` n `7`; equity avg `-0.1008` n `47`; fx avg `0.0365` n `4`; index avg `-0.0508` n `6`; metal avg `0.1645` n `7`; unknown avg `0.0804` n `313`
- 1h: commodity avg `-0.1649` n `7`; crypto_alt avg `0.0416` n `223`; crypto_major avg `0.0394` n `7`; equity avg `-0.0272` n `47`; fx avg `-0.0203` n `4`; index avg `0.0765` n `6`; metal avg `0.1732` n `7`; unknown avg `0.4339` n `311`
- 4h: commodity avg `0.0129` n `7`; crypto_alt avg `0.4497` n `223`; crypto_major avg `0.4503` n `7`; equity avg `0.6481` n `47`; fx avg `-0.2226` n `4`; index avg `0.34` n `6`; metal avg `0.7483` n `7`; unknown avg `0.9189` n `311`
- 24h: commodity avg `-1.6701` n `7`; crypto_alt avg `2.5189` n `223`; crypto_major avg `1.7164` n `7`; equity avg `2.7261` n `47`; fx avg `-0.4045` n `4`; index avg `2.2917` n `6`; metal avg `2.2594` n `7`; unknown avg `1.6409` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1806`, n `426`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1743`, n `426`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `426`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `426`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `426`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `426`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1021`, n `422`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0971`, n `422`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `426`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `426`, weak_sample_signal
