# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T08:37:25.426288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.0234` n `232`; crypto_major avg `-0.0235` n `8`; equity avg `0.0007` n `134`; fx avg `0.0048` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0141` n `20`; unknown avg `1.1853` n `790`
- 1h: commodity avg `-0.1797` n `12`; crypto_alt avg `0.4108` n `232`; crypto_major avg `0.2602` n `8`; equity avg `0.0907` n `134`; fx avg `-0.1158` n `6`; index avg `-0.0014` n `26`; metal avg `0.152` n `20`; unknown avg `1.2742` n `788`
- 4h: commodity avg `-0.209` n `12`; crypto_alt avg `0.0366` n `232`; crypto_major avg `-0.1026` n `8`; equity avg `0.0573` n `134`; fx avg `-0.1755` n `6`; index avg `0.0551` n `26`; metal avg `0.2274` n `20`; unknown avg `1.4793` n `758`
- 24h: commodity avg `-0.1538` n `12`; crypto_alt avg `0.3135` n `232`; crypto_major avg `-0.5975` n `8`; equity avg `0.4651` n `134`; fx avg `-0.1419` n `6`; index avg `0.058` n `26`; metal avg `0.0131` n `20`; unknown avg `383.4229` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
