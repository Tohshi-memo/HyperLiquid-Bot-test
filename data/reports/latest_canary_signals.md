# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T23:30:32.432086+00:00`
- Correlation status: `ready`
- Asset price records: `308`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `7`; crypto_alt avg `0.0795` n `223`; crypto_major avg `0.0277` n `7`; equity avg `0.1339` n `47`; fx avg `0.0008` n `4`; index avg `-0.0087` n `6`; metal avg `0.0005` n `7`; unknown avg `-0.0371` n `312`
- 1h: commodity avg `0.0267` n `7`; crypto_alt avg `-0.3759` n `223`; crypto_major avg `-0.2809` n `7`; equity avg `-0.2549` n `47`; fx avg `0.0035` n `4`; index avg `-0.0261` n `6`; metal avg `-0.0587` n `7`; unknown avg `-0.0645` n `312`
- 4h: commodity avg `-0.0335` n `7`; crypto_alt avg `-0.1473` n `223`; crypto_major avg `-0.0133` n `7`; equity avg `-0.3496` n `47`; fx avg `0.0089` n `4`; index avg `-0.097` n `6`; metal avg `-0.1328` n `7`; unknown avg `-0.2392` n `312`
- 24h: commodity avg `1.4006` n `7`; crypto_alt avg `1.9478` n `223`; crypto_major avg `1.011` n `7`; equity avg `-0.219` n `47`; fx avg `-0.0199` n `4`; index avg `-0.3078` n `6`; metal avg `-2.3908` n `7`; unknown avg `-1.2648` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.236`, n `304`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2302`, n `304`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1846`, n `300`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1828`, n `300`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `304`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1469`, n `304`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1415`, n `304`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `304`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1207`, n `304`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `300`, weak_sample_signal
