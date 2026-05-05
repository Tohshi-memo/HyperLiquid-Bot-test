# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T20:15:28.634701+00:00`
- Correlation status: `ready`
- Asset price records: `389`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0696` n `7`; crypto_alt avg `0.1613` n `223`; crypto_major avg `0.0852` n `7`; equity avg `-0.019` n `47`; fx avg `-0.0013` n `4`; index avg `0.0` n `6`; metal avg `0.0428` n `7`; unknown avg `-0.2544` n `313`
- 1h: commodity avg `-0.0404` n `7`; crypto_alt avg `0.4531` n `223`; crypto_major avg `0.3183` n `7`; equity avg `-0.082` n `47`; fx avg `0.0034` n `4`; index avg `-0.0435` n `6`; metal avg `-0.0817` n `7`; unknown avg `-0.1944` n `313`
- 4h: commodity avg `-0.0559` n `7`; crypto_alt avg `0.6467` n `223`; crypto_major avg `0.4517` n `7`; equity avg `0.0443` n `47`; fx avg `0.0116` n `4`; index avg `0.1188` n `6`; metal avg `-0.3779` n `7`; unknown avg `-0.2931` n `313`
- 24h: commodity avg `-1.1861` n `7`; crypto_alt avg `2.0092` n `223`; crypto_major avg `2.4362` n `7`; equity avg `1.9049` n `47`; fx avg `-0.0352` n `4`; index avg `1.3625` n `6`; metal avg `0.7358` n `7`; unknown avg `1.0545` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `385`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2001`, n `385`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `385`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `385`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1141`, n `381`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `385`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `385`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `381`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `385`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `385`, weak_sample_signal
