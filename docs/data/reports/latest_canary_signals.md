# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T16:07:31.104969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `12`; crypto_alt avg `-0.006` n `230`; crypto_major avg `-0.0065` n `8`; equity avg `0.3946` n `98`; fx avg `-0.005` n `6`; index avg `0.0696` n `25`; metal avg `0.0572` n `20`; unknown avg `0.0257` n `770`
- 1h: commodity avg `-0.068` n `12`; crypto_alt avg `0.7451` n `230`; crypto_major avg `0.9744` n `8`; equity avg `0.8306` n `98`; fx avg `-0.018` n `6`; index avg `0.1543` n `25`; metal avg `0.1341` n `20`; unknown avg `0.1108` n `770`
- 4h: commodity avg `-0.1322` n `12`; crypto_alt avg `0.603` n `230`; crypto_major avg `0.7811` n `8`; equity avg `0.032` n `98`; fx avg `-0.097` n `6`; index avg `0.0548` n `25`; metal avg `0.1129` n `20`; unknown avg `-0.0513` n `770`
- 24h: commodity avg `-0.683` n `12`; crypto_alt avg `1.4166` n `230`; crypto_major avg `1.3135` n `8`; equity avg `1.0742` n `97`; fx avg `-0.1467` n `6`; index avg `0.2741` n `25`; metal avg `0.3184` n `20`; unknown avg `0.1355` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0941`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0823`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
