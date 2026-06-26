# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T20:22:33.180007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.1561` n `228`; crypto_major avg `-0.2854` n `8`; equity avg `0.0929` n `88`; fx avg `0.0019` n `6`; index avg `0.0312` n `23`; metal avg `-0.0032` n `20`; unknown avg `0.4092` n `764`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `-0.0616` n `228`; crypto_major avg `-0.1185` n `8`; equity avg `0.174` n `88`; fx avg `-0.0068` n `6`; index avg `-0.0611` n `23`; metal avg `-0.0146` n `20`; unknown avg `0.2718` n `764`
- 4h: commodity avg `-0.0906` n `12`; crypto_alt avg `0.5535` n `228`; crypto_major avg `0.4054` n `8`; equity avg `0.1743` n `87`; fx avg `-0.0068` n `6`; index avg `-0.1019` n `23`; metal avg `-0.1818` n `20`; unknown avg `-0.3348` n `764`
- 24h: commodity avg `-0.5062` n `12`; crypto_alt avg `2.289` n `228`; crypto_major avg `1.9438` n `8`; equity avg `-0.7241` n `87`; fx avg `-0.0827` n `6`; index avg `-0.4083` n `23`; metal avg `0.488` n `20`; unknown avg `-0.3785` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2157`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
