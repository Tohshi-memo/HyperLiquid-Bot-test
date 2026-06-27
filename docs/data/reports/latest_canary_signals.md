# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T18:52:32.447452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.0003` n `228`; crypto_major avg `-0.0938` n `8`; equity avg `-0.0183` n `88`; fx avg `-0.0006` n `6`; index avg `0.0079` n `23`; metal avg `0.0008` n `20`; unknown avg `-0.0626` n `764`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `-0.165` n `228`; crypto_major avg `-0.3305` n `8`; equity avg `0.0029` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0075` n `23`; metal avg `0.0019` n `20`; unknown avg `-0.1526` n `764`
- 4h: commodity avg `-0.1453` n `12`; crypto_alt avg `-0.3752` n `228`; crypto_major avg `-0.605` n `8`; equity avg `-0.1344` n `88`; fx avg `0.0058` n `6`; index avg `-0.0359` n `23`; metal avg `-0.0439` n `20`; unknown avg `-0.035` n `764`
- 24h: commodity avg `0.2681` n `12`; crypto_alt avg `0.1272` n `228`; crypto_major avg `0.1578` n `8`; equity avg `0.9351` n `88`; fx avg `0.0771` n `6`; index avg `-0.044` n `23`; metal avg `0.0948` n `20`; unknown avg `-0.0535` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
