# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T16:45:52.856451+00:00`
- Correlation status: `ready`
- Asset price records: `375`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0534` n `7`; crypto_alt avg `-0.2727` n `223`; crypto_major avg `-0.2848` n `7`; equity avg `-0.092` n `47`; fx avg `-0.0027` n `4`; index avg `-0.0227` n `6`; metal avg `0.0457` n `7`; unknown avg `-0.0462` n `313`
- 1h: commodity avg `0.1293` n `7`; crypto_alt avg `-0.2383` n `223`; crypto_major avg `-0.5433` n `7`; equity avg `-0.4213` n `47`; fx avg `-0.0158` n `4`; index avg `0.018` n `6`; metal avg `-0.3354` n `7`; unknown avg `0.0402` n `313`
- 4h: commodity avg `-0.557` n `7`; crypto_alt avg `-0.565` n `223`; crypto_major avg `-0.2133` n `7`; equity avg `0.0922` n `47`; fx avg `-0.1404` n `4`; index avg `0.458` n `6`; metal avg `-0.4431` n `7`; unknown avg `0.1883` n `312`
- 24h: commodity avg `-1.4973` n `7`; crypto_alt avg `1.283` n `223`; crypto_major avg `1.4145` n `7`; equity avg `1.2544` n `47`; fx avg `-0.0427` n `4`; index avg `1.2391` n `6`; metal avg `1.0539` n `7`; unknown avg `0.7358` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.207`, n `371`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `371`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `371`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1293`, n `371`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1077`, n `371`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1077`, n `367`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `371`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `371`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `371`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `367`, weak_sample_signal
