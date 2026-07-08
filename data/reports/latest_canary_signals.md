# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T23:07:25.983072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.1015` n `229`; crypto_major avg `0.1049` n `8`; equity avg `-0.0229` n `91`; fx avg `-0.0044` n `6`; index avg `-0.0219` n `25`; metal avg `-0.0312` n `20`; unknown avg `0.0252` n `764`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `0.0651` n `229`; crypto_major avg `0.0244` n `8`; equity avg `0.051` n `91`; fx avg `-0.0262` n `6`; index avg `0.0074` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0736` n `764`
- 4h: commodity avg `0.1596` n `12`; crypto_alt avg `0.2477` n `229`; crypto_major avg `0.3392` n `8`; equity avg `0.5001` n `91`; fx avg `0.006` n `6`; index avg `0.0229` n `25`; metal avg `-0.1031` n `20`; unknown avg `1.0004` n `764`
- 24h: commodity avg `0.3509` n `12`; crypto_alt avg `-1.4936` n `229`; crypto_major avg `-2.317` n `8`; equity avg `1.62` n `91`; fx avg `0.002` n `6`; index avg `0.0278` n `25`; metal avg `-0.7222` n `20`; unknown avg `-0.0915` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
