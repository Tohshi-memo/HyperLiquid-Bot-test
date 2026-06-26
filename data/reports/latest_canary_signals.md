# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T21:22:29.066544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0441` n `12`; crypto_alt avg `0.1561` n `228`; crypto_major avg `0.2291` n `8`; equity avg `0.0629` n `88`; fx avg `0.054` n `6`; index avg `0.0127` n `23`; metal avg `-0.0065` n `20`; unknown avg `0.2795` n `764`
- 1h: commodity avg `0.2192` n `12`; crypto_alt avg `-0.4222` n `228`; crypto_major avg `-0.3655` n `8`; equity avg `-0.1058` n `88`; fx avg `0.0941` n `6`; index avg `-0.0073` n `23`; metal avg `0.0999` n `20`; unknown avg `-0.6209` n `764`
- 4h: commodity avg `0.1908` n `12`; crypto_alt avg `-0.4997` n `228`; crypto_major avg `-0.5743` n `8`; equity avg `-0.2959` n `87`; fx avg `0.0832` n `6`; index avg `-0.1676` n `23`; metal avg `-0.0818` n `20`; unknown avg `-0.4146` n `764`
- 24h: commodity avg `-0.1679` n `12`; crypto_alt avg `1.7949` n `228`; crypto_major avg `1.816` n `8`; equity avg `-0.6064` n `87`; fx avg `0.0204` n `6`; index avg `-0.367` n `23`; metal avg `0.6369` n `20`; unknown avg `-0.6957` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2207`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2149`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
