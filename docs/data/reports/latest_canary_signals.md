# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T16:22:29.036572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2708` n `12`; crypto_alt avg `-0.4499` n `232`; crypto_major avg `-0.4806` n `8`; equity avg `-0.4031` n `131`; fx avg `0.0175` n `6`; index avg `-0.0826` n `26`; metal avg `-0.12` n `20`; unknown avg `2.8568` n `793`
- 1h: commodity avg `0.2632` n `12`; crypto_alt avg `-0.2996` n `232`; crypto_major avg `-0.4092` n `8`; equity avg `-0.0575` n `131`; fx avg `0.0028` n `6`; index avg `-0.032` n `26`; metal avg `-0.0142` n `20`; unknown avg `-0.107` n `790`
- 4h: commodity avg `0.3875` n `12`; crypto_alt avg `-0.4058` n `232`; crypto_major avg `-0.8384` n `8`; equity avg `-0.2407` n `130`; fx avg `-0.0275` n `6`; index avg `0.0122` n `26`; metal avg `-0.0483` n `20`; unknown avg `0.3335` n `790`
- 24h: commodity avg `0.5941` n `12`; crypto_alt avg `0.7226` n `232`; crypto_major avg `-0.7492` n `8`; equity avg `-1.1272` n `130`; fx avg `0.0406` n `6`; index avg `-0.1666` n `26`; metal avg `-0.5535` n `20`; unknown avg `-0.0954` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0394`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0336`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0322`, n `668`, weak_sample_signal
