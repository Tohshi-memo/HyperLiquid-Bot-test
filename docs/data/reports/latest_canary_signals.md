# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T13:22:26.945370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.114` n `12`; crypto_alt avg `0.1009` n `232`; crypto_major avg `0.1155` n `8`; equity avg `0.0585` n `134`; fx avg `-0.0036` n `6`; index avg `0.0146` n `26`; metal avg `0.0129` n `20`; unknown avg `-0.0144` n `796`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.6642` n `232`; crypto_major avg `0.3754` n `8`; equity avg `0.0829` n `134`; fx avg `-0.0189` n `6`; index avg `0.0435` n `26`; metal avg `0.0519` n `20`; unknown avg `0.0534` n `788`
- 4h: commodity avg `0.2187` n `12`; crypto_alt avg `1.0318` n `232`; crypto_major avg `0.5542` n `8`; equity avg `-0.0097` n `134`; fx avg `0.0411` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0644` n `20`; unknown avg `6683.7779` n `748`
- 24h: commodity avg `0.157` n `12`; crypto_alt avg `1.4137` n `232`; crypto_major avg `0.0341` n `8`; equity avg `0.3554` n `134`; fx avg `-0.0868` n `6`; index avg `0.0204` n `26`; metal avg `-0.1341` n `20`; unknown avg `178.0894` n `664`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
