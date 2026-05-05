# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T04:45:26.670579+00:00`
- Correlation status: `ready`
- Asset price records: `329`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.071` n `7`; crypto_alt avg `-0.0732` n `223`; crypto_major avg `-0.0965` n `7`; equity avg `-0.0422` n `47`; fx avg `-0.0016` n `4`; index avg `0.0122` n `6`; metal avg `-0.0111` n `7`; unknown avg `0.0976` n `312`
- 1h: commodity avg `-0.1256` n `7`; crypto_alt avg `-0.1032` n `223`; crypto_major avg `-0.2624` n `7`; equity avg `-0.01` n `47`; fx avg `0.0016` n `4`; index avg `0.1153` n `6`; metal avg `-0.0378` n `7`; unknown avg `0.1184` n `312`
- 4h: commodity avg `-0.2808` n `7`; crypto_alt avg `0.6223` n `223`; crypto_major avg `0.6804` n `7`; equity avg `0.3027` n `47`; fx avg `-0.0035` n `4`; index avg `0.293` n `6`; metal avg `0.2536` n `7`; unknown avg `0.3424` n `312`
- 24h: commodity avg `0.9593` n `7`; crypto_alt avg `0.1886` n `223`; crypto_major avg `-0.9262` n `7`; equity avg `-0.8779` n `47`; fx avg `0.0012` n `4`; index avg `-0.1065` n `6`; metal avg `-1.8969` n `7`; unknown avg `-1.2626` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.227`, n `325`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2206`, n `325`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1531`, n `325`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.141`, n `321`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `325`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1383`, n `321`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `325`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `325`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `325`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.121`, n `321`, weak_sample_signal
