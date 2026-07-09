# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T22:37:38.997203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.0876` n `229`; crypto_major avg `-0.0656` n `8`; equity avg `0.0181` n `91`; fx avg `-0.0048` n `6`; index avg `-0.0021` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0236` n `765`
- 1h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.065` n `229`; crypto_major avg `-0.0201` n `8`; equity avg `0.062` n `91`; fx avg `-0.0138` n `6`; index avg `0.006` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.2129` n `765`
- 4h: commodity avg `-0.019` n `12`; crypto_alt avg `-0.3295` n `229`; crypto_major avg `-0.1744` n `8`; equity avg `-0.2351` n `91`; fx avg `-0.0094` n `6`; index avg `-0.0115` n `25`; metal avg `-0.1329` n `20`; unknown avg `-0.3978` n `765`
- 24h: commodity avg `-1.1491` n `12`; crypto_alt avg `1.012` n `229`; crypto_major avg `0.6425` n `8`; equity avg `1.5794` n `91`; fx avg `0.0255` n `6`; index avg `0.3335` n `25`; metal avg `0.6256` n `20`; unknown avg `-0.1388` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
