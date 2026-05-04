# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T22:30:29.928300+00:00`
- Correlation status: `ready`
- Asset price records: `304`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `7`; crypto_alt avg `-0.0156` n `223`; crypto_major avg `-0.0268` n `7`; equity avg `-0.0111` n `47`; fx avg `0.0` n `4`; index avg `-0.0046` n `6`; metal avg `0.0044` n `7`; unknown avg `-0.0025` n `312`
- 1h: commodity avg `-0.0682` n `7`; crypto_alt avg `0.0429` n `223`; crypto_major avg `0.0501` n `7`; equity avg `0.1269` n `47`; fx avg `0.0007` n `4`; index avg `-0.1392` n `6`; metal avg `-0.0247` n `7`; unknown avg `0.0576` n `312`
- 4h: commodity avg `-0.3591` n `7`; crypto_alt avg `0.061` n `223`; crypto_major avg `-0.0763` n `7`; equity avg `-0.2493` n `47`; fx avg `-0.0038` n `4`; index avg `-0.1265` n `6`; metal avg `0.1247` n `7`; unknown avg `-0.2529` n `312`
- 24h: commodity avg `1.6753` n `7`; crypto_alt avg `1.7529` n `223`; crypto_major avg `0.761` n `7`; equity avg `-0.2445` n `47`; fx avg `-0.03` n `4`; index avg `-0.1351` n `6`; metal avg `-2.2794` n `7`; unknown avg `-1.2813` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2357`, n `300`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2298`, n `300`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1649`, n `296`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1638`, n `296`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `300`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `300`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1409`, n `300`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `300`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `296`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1198`, n `300`, weak_sample_signal
