# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T16:52:30.153097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `12`; crypto_alt avg `0.0296` n `230`; crypto_major avg `-0.0404` n `8`; equity avg `-0.1233` n `98`; fx avg `-0.0024` n `6`; index avg `-0.0219` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0085` n `773`
- 1h: commodity avg `0.0499` n `12`; crypto_alt avg `0.2312` n `230`; crypto_major avg `0.2252` n `8`; equity avg `-0.1554` n `98`; fx avg `-0.0067` n `6`; index avg `-0.011` n `25`; metal avg `-0.1285` n `20`; unknown avg `-0.1049` n `773`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `0.8076` n `230`; crypto_major avg `0.8676` n `8`; equity avg `1.2806` n `98`; fx avg `-0.0272` n `6`; index avg `0.2665` n `25`; metal avg `0.0609` n `20`; unknown avg `9.8906` n `773`
- 24h: commodity avg `0.4546` n `12`; crypto_alt avg `0.1367` n `230`; crypto_major avg `-0.5405` n `8`; equity avg `-0.1878` n `98`; fx avg `-0.0332` n `6`; index avg `-0.0915` n `25`; metal avg `0.3404` n `20`; unknown avg `0.8504` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1051`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
