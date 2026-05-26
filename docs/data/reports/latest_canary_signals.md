# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T23:37:16.368433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `-0.062` n `228`; crypto_major avg `0.044` n `8`; equity avg `0.0352` n `67`; fx avg `-0.0018` n `6`; index avg `0.0038` n `23`; metal avg `0.1092` n `18`; unknown avg `0.0545` n `418`
- 1h: commodity avg `-0.0577` n `12`; crypto_alt avg `0.2216` n `228`; crypto_major avg `0.2301` n `8`; equity avg `-0.0119` n `67`; fx avg `-0.0127` n `6`; index avg `0.0558` n `23`; metal avg `0.1972` n `18`; unknown avg `-0.2928` n `418`
- 4h: commodity avg `-0.076` n `12`; crypto_alt avg `0.1184` n `228`; crypto_major avg `-0.1741` n `8`; equity avg `0.1627` n `67`; fx avg `0.0125` n `6`; index avg `0.0847` n `23`; metal avg `0.3435` n `18`; unknown avg `-0.6599` n `418`
- 24h: commodity avg `0.5921` n `12`; crypto_alt avg `-1.4058` n `228`; crypto_major avg `-1.3539` n `8`; equity avg `-0.0385` n `67`; fx avg `-0.0815` n `6`; index avg `0.6964` n `23`; metal avg `-0.3223` n `18`; unknown avg `0.0741` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
