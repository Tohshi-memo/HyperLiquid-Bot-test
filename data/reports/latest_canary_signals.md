# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T01:30:27.279511+00:00`
- Correlation status: `ready`
- Asset price records: `316`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `7`; crypto_alt avg `0.0547` n `223`; crypto_major avg `0.0605` n `7`; equity avg `-0.1346` n `47`; fx avg `-0.0048` n `4`; index avg `-0.0043` n `6`; metal avg `-0.124` n `7`; unknown avg `-0.0112` n `312`
- 1h: commodity avg `0.0006` n `7`; crypto_alt avg `0.5895` n `223`; crypto_major avg `0.4666` n `7`; equity avg `0.1501` n `47`; fx avg `-0.007` n `4`; index avg `0.0531` n `6`; metal avg `0.2829` n `7`; unknown avg `-0.0221` n `312`
- 4h: commodity avg `-0.0984` n `7`; crypto_alt avg `0.173` n `223`; crypto_major avg `0.1291` n `7`; equity avg `0.0833` n `47`; fx avg `-0.0124` n `4`; index avg `-0.1176` n `6`; metal avg `0.2044` n `7`; unknown avg `-0.1264` n `312`
- 24h: commodity avg `1.2623` n `7`; crypto_alt avg `2.2378` n `223`; crypto_major avg `1.136` n `7`; equity avg `-0.4381` n `47`; fx avg `-0.0415` n `4`; index avg `-0.0847` n `6`; metal avg `-1.5764` n `7`; unknown avg `-1.4428` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2318`, n `312`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2255`, n `312`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.159`, n `308`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1571`, n `308`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1522`, n `312`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `312`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `312`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1306`, n `312`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `308`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `312`, weak_sample_signal
