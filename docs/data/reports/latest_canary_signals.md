# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T18:30:31.696220+00:00`
- Correlation status: `ready`
- Asset price records: `382`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0575` n `7`; crypto_alt avg `-0.002` n `223`; crypto_major avg `-0.1275` n `7`; equity avg `-0.0276` n `47`; fx avg `0.0` n `4`; index avg `-0.108` n `6`; metal avg `-0.0109` n `7`; unknown avg `-0.2981` n `313`
- 1h: commodity avg `0.0299` n `7`; crypto_alt avg `0.1343` n `223`; crypto_major avg `0.1143` n `7`; equity avg `0.0476` n `47`; fx avg `-0.0025` n `4`; index avg `-0.1272` n `6`; metal avg `0.0148` n `7`; unknown avg `-0.0472` n `313`
- 4h: commodity avg `-0.275` n `7`; crypto_alt avg `-0.0427` n `223`; crypto_major avg `0.245` n `7`; equity avg `0.1107` n `47`; fx avg `-0.15` n `4`; index avg `0.3173` n `6`; metal avg `-0.487` n `7`; unknown avg `-0.0596` n `313`
- 24h: commodity avg `-1.5063` n `7`; crypto_alt avg `1.2634` n `223`; crypto_major avg `1.8601` n `7`; equity avg `1.5222` n `47`; fx avg `-0.0512` n `4`; index avg `1.3063` n `6`; metal avg `1.0149` n `7`; unknown avg `0.7207` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2069`, n `378`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `378`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `378`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1277`, n `378`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1141`, n `374`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1084`, n `378`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `374`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `378`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.105`, n `378`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `378`, weak_sample_signal
