# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T21:22:30.239810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `0.1448` n `232`; crypto_major avg `0.0828` n `8`; equity avg `0.023` n `134`; fx avg `0.0016` n `6`; index avg `0.0023` n `26`; metal avg `0.0058` n `20`; unknown avg `1.0519` n `796`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.3521` n `232`; crypto_major avg `0.1262` n `8`; equity avg `0.066` n `134`; fx avg `0.0019` n `6`; index avg `0.0019` n `26`; metal avg `0.004` n `20`; unknown avg `7.8268` n `780`
- 4h: commodity avg `-0.0037` n `12`; crypto_alt avg `0.4344` n `232`; crypto_major avg `0.0784` n `8`; equity avg `0.1477` n `134`; fx avg `-0.0146` n `6`; index avg `0.016` n `26`; metal avg `0.0208` n `20`; unknown avg `-0.2029` n `734`
- 24h: commodity avg `0.1785` n `12`; crypto_alt avg `0.1847` n `232`; crypto_major avg `-1.2437` n `8`; equity avg `0.4965` n `134`; fx avg `-0.1468` n `6`; index avg `0.0818` n `26`; metal avg `0.006` n `20`; unknown avg `7800.4369` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
