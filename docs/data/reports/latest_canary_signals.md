# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T10:22:30.123931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0489` n `12`; crypto_alt avg `0.0423` n `232`; crypto_major avg `0.1417` n `8`; equity avg `0.1703` n `134`; fx avg `0.0105` n `6`; index avg `0.0378` n `26`; metal avg `0.0153` n `20`; unknown avg `1.5323` n `797`
- 1h: commodity avg `-0.1022` n `12`; crypto_alt avg `0.7269` n `232`; crypto_major avg `0.699` n `8`; equity avg `0.4969` n `134`; fx avg `-0.0189` n `6`; index avg `0.0922` n `26`; metal avg `0.0969` n `20`; unknown avg `0.7761` n `795`
- 4h: commodity avg `0.015` n `12`; crypto_alt avg `1.0883` n `232`; crypto_major avg `0.9037` n `8`; equity avg `0.4643` n `134`; fx avg `-0.0126` n `6`; index avg `0.0614` n `26`; metal avg `0.0602` n `20`; unknown avg `1.0375` n `785`
- 24h: commodity avg `0.3838` n `12`; crypto_alt avg `1.232` n `232`; crypto_major avg `-0.2704` n `8`; equity avg `-0.0034` n `134`; fx avg `-0.1132` n `6`; index avg `-0.0334` n `26`; metal avg `0.1528` n `20`; unknown avg `7463.2781` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
