# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T05:47:40.735171+00:00`
- Correlation status: `ready`
- Asset price records: `523`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.35` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.0169` n `228`; crypto_major avg `-0.082` n `8`; equity avg `0.0524` n `65`; fx avg `0.0225` n `4`; index avg `0.0267` n `23`; metal avg `0.0122` n `18`; unknown avg `-0.1163` n `358`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.6233` n `228`; crypto_major avg `0.2391` n `8`; equity avg `0.3055` n `65`; fx avg `-0.0038` n `4`; index avg `0.0993` n `23`; metal avg `0.183` n `18`; unknown avg `0.0074` n `358`
- 4h: commodity avg `0.0401` n `12`; crypto_alt avg `1.1171` n `228`; crypto_major avg `0.0782` n `8`; equity avg `0.4849` n `65`; fx avg `0.0519` n `4`; index avg `0.1287` n `23`; metal avg `-0.3301` n `18`; unknown avg `-0.0805` n `358`
- 24h: commodity avg `-1.8911` n `7`; crypto_alt avg `1.5245` n `223`; crypto_major avg `-0.6844` n `7`; equity avg `1.5363` n `47`; fx avg `-0.0525` n `4`; index avg `1.207` n `6`; metal avg `1.6094` n `7`; unknown avg `1.8952` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `519`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `519`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `515`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `519`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `515`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0736`, n `515`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0716`, n `515`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `519`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0679`, n `515`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `515`, weak_sample_signal
