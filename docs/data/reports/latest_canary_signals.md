# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T22:00:33.870479+00:00`
- Correlation status: `ready`
- Asset price records: `302`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0522` n `7`; crypto_alt avg `0.212` n `223`; crypto_major avg `0.1802` n `7`; equity avg `0.1281` n `47`; fx avg `0.0045` n `4`; index avg `0.0323` n `6`; metal avg `-0.055` n `7`; unknown avg `0.2305` n `312`
- 1h: commodity avg `0.0195` n `7`; crypto_alt avg `0.8293` n `223`; crypto_major avg `0.6482` n `7`; equity avg `0.1815` n `47`; fx avg `-0.0048` n `4`; index avg `-0.1356` n `6`; metal avg `0.0024` n `7`; unknown avg `0.0335` n `312`
- 4h: commodity avg `-0.0248` n `7`; crypto_alt avg `0.1597` n `223`; crypto_major avg `-0.0669` n `7`; equity avg `-0.2191` n `47`; fx avg `-0.0013` n `4`; index avg `-0.0548` n `6`; metal avg `-0.0941` n `7`; unknown avg `-0.2968` n `312`
- 24h: commodity avg `2.1713` n `7`; crypto_alt avg `2.2854` n `223`; crypto_major avg `1.349` n `7`; equity avg `-0.2869` n `47`; fx avg `-0.0272` n `4`; index avg `-0.5371` n `6`; metal avg `-2.2821` n `7`; unknown avg `-1.1429` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2357`, n `298`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2298`, n `298`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1735`, n `294`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1722`, n `294`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `298`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `298`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1413`, n `298`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `298`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1206`, n `294`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1197`, n `298`, weak_sample_signal
