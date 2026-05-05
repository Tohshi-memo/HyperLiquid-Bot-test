# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T10:15:52.550959+00:00`
- Correlation status: `ready`
- Asset price records: `351`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `7`; crypto_alt avg `0.0881` n `223`; crypto_major avg `0.0746` n `7`; equity avg `-0.1055` n `47`; fx avg `0.0095` n `4`; index avg `-0.0011` n `6`; metal avg `-0.0237` n `7`; unknown avg `-0.2488` n `312`
- 1h: commodity avg `0.0156` n `7`; crypto_alt avg `0.0971` n `223`; crypto_major avg `-0.0848` n `7`; equity avg `-0.1746` n `47`; fx avg `0.0093` n `4`; index avg `0.0167` n `6`; metal avg `0.0043` n `7`; unknown avg `-0.0192` n `312`
- 4h: commodity avg `-0.2059` n `7`; crypto_alt avg `0.2766` n `223`; crypto_major avg `-0.0645` n `7`; equity avg `-0.0002` n `47`; fx avg `0.0547` n `4`; index avg `0.137` n `6`; metal avg `0.5331` n `7`; unknown avg `0.1141` n `312`
- 24h: commodity avg `-0.4449` n `7`; crypto_alt avg `2.4105` n `223`; crypto_major avg `1.8953` n `7`; equity avg `1.038` n `47`; fx avg `0.0492` n `4`; index avg `0.5553` n `6`; metal avg `1.2626` n `7`; unknown avg `-0.3251` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2172`, n `347`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.21`, n `347`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `347`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1349`, n `347`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `347`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `347`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `347`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `347`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `343`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0961`, n `343`, weak_sample_signal
