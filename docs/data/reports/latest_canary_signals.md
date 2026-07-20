# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T11:07:25.119691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0426` n `12`; crypto_alt avg `0.0494` n `230`; crypto_major avg `0.1238` n `8`; equity avg `0.1433` n `98`; fx avg `-0.0085` n `6`; index avg `0.0374` n `25`; metal avg `0.033` n `20`; unknown avg `0.0622` n `770`
- 1h: commodity avg `0.0104` n `12`; crypto_alt avg `0.1747` n `230`; crypto_major avg `0.2897` n `8`; equity avg `0.3263` n `98`; fx avg `0.0058` n `6`; index avg `0.0581` n `25`; metal avg `0.0186` n `20`; unknown avg `0.1245` n `770`
- 4h: commodity avg `-0.5311` n `12`; crypto_alt avg `0.9387` n `230`; crypto_major avg `0.7998` n `8`; equity avg `0.8763` n `98`; fx avg `-0.0024` n `6`; index avg `0.1975` n `25`; metal avg `0.2444` n `20`; unknown avg `0.1954` n `763`
- 24h: commodity avg `-0.5567` n `12`; crypto_alt avg `0.2489` n `230`; crypto_major avg `-0.1876` n `8`; equity avg `0.7256` n `97`; fx avg `-0.0394` n `6`; index avg `0.1588` n `25`; metal avg `0.241` n `20`; unknown avg `-0.0055` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0867`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
