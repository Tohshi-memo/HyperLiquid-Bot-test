# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T05:52:25.039306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `0.1443` n `228`; crypto_major avg `0.1496` n `8`; equity avg `0.0163` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0032` n `23`; metal avg `0.002` n `20`; unknown avg `-0.221` n `748`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `0.0046` n `228`; crypto_major avg `-0.1014` n `8`; equity avg `-0.029` n `88`; fx avg `0.0041` n `6`; index avg `-0.0112` n `23`; metal avg `-0.0069` n `20`; unknown avg `-0.1329` n `748`
- 4h: commodity avg `0.004` n `12`; crypto_alt avg `0.3069` n `228`; crypto_major avg `0.4136` n `8`; equity avg `0.1191` n `88`; fx avg `0.0033` n `6`; index avg `-0.0009` n `23`; metal avg `-0.0038` n `20`; unknown avg `-1.0922` n `748`
- 24h: commodity avg `-0.2568` n `12`; crypto_alt avg `2.1344` n `228`; crypto_major avg `1.9313` n `8`; equity avg `1.7599` n `87`; fx avg `0.0071` n `6`; index avg `0.1098` n `23`; metal avg `1.131` n `20`; unknown avg `-0.2597` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2058`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
