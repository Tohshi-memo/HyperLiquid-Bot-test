# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T23:45:44.867283+00:00`
- Correlation status: `ready`
- Asset price records: `403`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `7`; crypto_alt avg `0.0304` n `223`; crypto_major avg `-0.0294` n `7`; equity avg `-0.0221` n `47`; fx avg `0.0032` n `4`; index avg `0.0083` n `6`; metal avg `0.1225` n `7`; unknown avg `-0.0522` n `313`
- 1h: commodity avg `-0.6919` n `7`; crypto_alt avg `-0.0409` n `223`; crypto_major avg `-0.2515` n `7`; equity avg `0.112` n `47`; fx avg `0.022` n `4`; index avg `0.1513` n `6`; metal avg `0.8604` n `7`; unknown avg `-0.4572` n `313`
- 4h: commodity avg `-0.7041` n `7`; crypto_alt avg `0.1802` n `223`; crypto_major avg `-0.2199` n `7`; equity avg `0.7508` n `47`; fx avg `0.1433` n `4`; index avg `0.3107` n `6`; metal avg `0.7369` n `7`; unknown avg `-0.2565` n `313`
- 24h: commodity avg `-1.876` n `7`; crypto_alt avg `2.2531` n `223`; crypto_major avg `2.3321` n `7`; equity avg `2.973` n `47`; fx avg `0.0935` n `4`; index avg `1.8723` n `6`; metal avg `1.4942` n `7`; unknown avg `1.2037` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1934`, n `399`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1871`, n `399`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `399`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `399`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `399`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1072`, n `395`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `399`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `399`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `399`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `395`, weak_sample_signal
