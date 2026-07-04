# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T16:52:27.206241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0662` n `229`; crypto_major avg `0.0094` n `8`; equity avg `-0.0055` n `88`; fx avg `0.0012` n `6`; index avg `-0.0134` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0721` n `765`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.1289` n `229`; crypto_major avg `0.0249` n `8`; equity avg `-0.0331` n `88`; fx avg `-0.0058` n `6`; index avg `-0.0175` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0418` n `765`
- 4h: commodity avg `-0.0666` n `12`; crypto_alt avg `0.7755` n `229`; crypto_major avg `0.9257` n `8`; equity avg `0.0239` n `88`; fx avg `0.0178` n `6`; index avg `0.0005` n `25`; metal avg `0.029` n `20`; unknown avg `0.2478` n `759`
- 24h: commodity avg `0.0087` n `12`; crypto_alt avg `1.4278` n `229`; crypto_major avg `2.0623` n `8`; equity avg `0.2618` n `88`; fx avg `-0.0072` n `6`; index avg `-0.0549` n `25`; metal avg `0.0301` n `20`; unknown avg `1.8507` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
