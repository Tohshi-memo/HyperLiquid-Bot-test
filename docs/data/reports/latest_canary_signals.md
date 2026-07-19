# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T02:52:28.979451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.1153` n `230`; crypto_major avg `-0.153` n `8`; equity avg `0.0219` n `96`; fx avg `0.001` n `6`; index avg `0.003` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.2514` n `770`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.181` n `230`; crypto_major avg `0.2431` n `8`; equity avg `0.0048` n `96`; fx avg `0.0058` n `6`; index avg `0.0067` n `25`; metal avg `0.0059` n `20`; unknown avg `0.1039` n `770`
- 4h: commodity avg `-0.0851` n `12`; crypto_alt avg `0.0926` n `230`; crypto_major avg `0.2891` n `8`; equity avg `0.2155` n `96`; fx avg `0.0456` n `6`; index avg `-0.0072` n `25`; metal avg `0.052` n `20`; unknown avg `-0.6861` n `770`
- 24h: commodity avg `0.2281` n `12`; crypto_alt avg `-0.0629` n `230`; crypto_major avg `0.9374` n `8`; equity avg `-0.2166` n `96`; fx avg `-0.0159` n `6`; index avg `-0.0044` n `25`; metal avg `-0.0214` n `20`; unknown avg `0.0555` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
