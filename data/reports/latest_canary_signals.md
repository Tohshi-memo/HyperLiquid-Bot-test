# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T14:07:25.788881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0612` n `13`; crypto_alt avg `0.3614` n `238`; crypto_major avg `0.3286` n `8`; equity avg `0.2477` n `156`; fx avg `-0.007` n `6`; index avg `0.0084` n `27`; metal avg `-0.0081` n `20`; unknown avg `0.2762` n `1243`
- 1h: commodity avg `0.2137` n `13`; crypto_alt avg `-0.3346` n `238`; crypto_major avg `-0.4527` n `8`; equity avg `0.2458` n `156`; fx avg `-0.0752` n `6`; index avg `0.0183` n `27`; metal avg `-0.0533` n `20`; unknown avg `2.2649` n `1239`
- 4h: commodity avg `0.0066` n `13`; crypto_alt avg `-0.0461` n `238`; crypto_major avg `-0.4981` n `8`; equity avg `-0.4877` n `156`; fx avg `-0.1689` n `6`; index avg `-0.032` n `27`; metal avg `-0.401` n `20`; unknown avg `2.5403` n `1233`
- 24h: commodity avg `0.55` n `13`; crypto_alt avg `-4.8221` n `238`; crypto_major avg `-3.7382` n `8`; equity avg `-4.59` n `156`; fx avg `-0.0389` n `6`; index avg `-0.4107` n `27`; metal avg `-0.8825` n `20`; unknown avg `23.6582` n `1010`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
