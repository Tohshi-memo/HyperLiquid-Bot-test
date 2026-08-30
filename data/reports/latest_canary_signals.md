# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T01:52:31.548331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.0192` n `231`; crypto_major avg `0.0544` n `8`; equity avg `-0.0099` n `128`; fx avg `0.0` n `6`; index avg `-0.0215` n `26`; metal avg `-0.0039` n `20`; unknown avg `-0.0821` n `793`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `-0.2486` n `231`; crypto_major avg `-0.1605` n `8`; equity avg `0.0092` n `128`; fx avg `-0.001` n `6`; index avg `-0.0058` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.0938` n `793`
- 4h: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.2897` n `231`; crypto_major avg `-0.0131` n `8`; equity avg `0.02` n `128`; fx avg `0.0188` n `6`; index avg `0.016` n `26`; metal avg `-0.0059` n `20`; unknown avg `4.0042` n `774`
- 24h: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.0388` n `231`; crypto_major avg `0.622` n `8`; equity avg `0.3715` n `128`; fx avg `-0.0124` n `6`; index avg `0.0915` n `26`; metal avg `0.1127` n `20`; unknown avg `0.0093` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2251`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
