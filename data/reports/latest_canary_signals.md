# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T01:30:28.906205+00:00`
- Correlation status: `ready`
- Asset price records: `410`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.086` n `7`; crypto_alt avg `0.082` n `223`; crypto_major avg `0.1059` n `7`; equity avg `0.0284` n `47`; fx avg `0.0149` n `4`; index avg `-0.0461` n `6`; metal avg `0.2438` n `7`; unknown avg `0.0161` n `313`
- 1h: commodity avg `-0.1014` n `7`; crypto_alt avg `0.6621` n `223`; crypto_major avg `0.4868` n `7`; equity avg `0.1656` n `47`; fx avg `-0.0323` n `4`; index avg `0.4695` n `6`; metal avg `0.5354` n `7`; unknown avg `0.1027` n `313`
- 4h: commodity avg `-0.5268` n `7`; crypto_alt avg `0.1314` n `223`; crypto_major avg `0.0049` n `7`; equity avg `0.5304` n `47`; fx avg `-0.214` n `4`; index avg `0.6293` n `6`; metal avg `1.2723` n `7`; unknown avg `-0.0803` n `313`
- 24h: commodity avg `-1.5435` n `7`; crypto_alt avg `2.2471` n `223`; crypto_major avg `2.1338` n `7`; equity avg `2.7183` n `47`; fx avg `-0.182` n `4`; index avg `2.333` n `6`; metal avg `1.7504` n `7`; unknown avg `1.5893` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1887`, n `406`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1824`, n `406`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `406`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1254`, n `406`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `406`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1018`, n `406`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1018`, n `402`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `406`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `406`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.096`, n `402`, weak_sample_signal
