# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T12:45:24.449929+00:00`
- Correlation status: `ready`
- Asset price records: `361`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0901` n `7`; crypto_alt avg `0.0622` n `223`; crypto_major avg `0.0029` n `7`; equity avg `0.0551` n `47`; fx avg `0.0026` n `4`; index avg `0.2383` n `6`; metal avg `-0.1765` n `7`; unknown avg `-0.1002` n `312`
- 1h: commodity avg `-0.2023` n `7`; crypto_alt avg `0.2471` n `223`; crypto_major avg `0.2458` n `7`; equity avg `0.3156` n `47`; fx avg `0.0201` n `4`; index avg `0.4596` n `6`; metal avg `0.1344` n `7`; unknown avg `0.0143` n `312`
- 4h: commodity avg `-0.0937` n `7`; crypto_alt avg `0.5501` n `223`; crypto_major avg `0.7178` n `7`; equity avg `0.3948` n `47`; fx avg `0.087` n `4`; index avg `0.3017` n `6`; metal avg `0.3673` n `7`; unknown avg `0.2947` n `312`
- 24h: commodity avg `0.5475` n `7`; crypto_alt avg `2.5355` n `223`; crypto_major avg `2.2442` n `7`; equity avg `0.8721` n `47`; fx avg `0.0746` n `4`; index avg `0.6797` n `6`; metal avg `0.4526` n `7`; unknown avg `-0.3918` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2086`, n `357`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2014`, n `357`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `357`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.131`, n `357`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1048`, n `357`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `357`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `357`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `357`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `353`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `357`, weak_sample_signal
