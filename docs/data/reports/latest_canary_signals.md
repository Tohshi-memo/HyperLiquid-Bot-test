# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T18:45:49.726468+00:00`
- Correlation status: `ready`
- Asset price records: `383`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0124` n `7`; crypto_alt avg `0.0802` n `223`; crypto_major avg `0.025` n `7`; equity avg `-0.0481` n `47`; fx avg `0.0029` n `4`; index avg `0.111` n `6`; metal avg `-0.0252` n `7`; unknown avg `-0.0036` n `313`
- 1h: commodity avg `-0.0352` n `7`; crypto_alt avg `0.2459` n `223`; crypto_major avg `0.1468` n `7`; equity avg `-0.0264` n `47`; fx avg `0.0046` n `4`; index avg `0.0273` n `6`; metal avg `0.0137` n `7`; unknown avg `0.0179` n `313`
- 4h: commodity avg `-0.2626` n `7`; crypto_alt avg `0.0401` n `223`; crypto_major avg `0.2698` n `7`; equity avg `0.0622` n `47`; fx avg `-0.147` n `4`; index avg `0.4297` n `6`; metal avg `-0.5119` n `7`; unknown avg `-0.0646` n `313`
- 24h: commodity avg `-1.4176` n `7`; crypto_alt avg `1.3137` n `223`; crypto_major avg `2.0632` n `7`; equity avg `1.7107` n `47`; fx avg `-0.0408` n `4`; index avg `1.4741` n `6`; metal avg `0.9896` n `7`; unknown avg `0.7223` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `379`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2001`, n `379`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `379`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `379`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1141`, n `375`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `379`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `375`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `379`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `379`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `379`, weak_sample_signal
