# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T19:52:31.521667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `13`; crypto_alt avg `0.0537` n `235`; crypto_major avg `0.0367` n `8`; equity avg `0.0094` n `143`; fx avg `0.0062` n `6`; index avg `0.0015` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.3629` n `1078`
- 1h: commodity avg `0.0294` n `13`; crypto_alt avg `0.206` n `235`; crypto_major avg `-0.0462` n `8`; equity avg `0.0293` n `143`; fx avg `0.0086` n `6`; index avg `0.0072` n `26`; metal avg `0.0093` n `20`; unknown avg `0.3193` n `1068`
- 4h: commodity avg `-0.108` n `13`; crypto_alt avg `0.224` n `235`; crypto_major avg `0.1671` n `8`; equity avg `0.094` n `143`; fx avg `0.0018` n `6`; index avg `0.0239` n `26`; metal avg `0.0058` n `20`; unknown avg `1.0402` n `1062`
- 24h: commodity avg `0.0184` n `13`; crypto_alt avg `2.8546` n `235`; crypto_major avg `1.4891` n `8`; equity avg `0.1917` n `143`; fx avg `-0.0445` n `6`; index avg `0.0485` n `26`; metal avg `-0.0286` n `20`; unknown avg `-0.1818` n `862`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1996`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
