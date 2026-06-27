# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T02:37:28.353543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0981` n `12`; crypto_alt avg `-0.0202` n `228`; crypto_major avg `-0.0761` n `8`; equity avg `0.0107` n `88`; fx avg `-0.0047` n `6`; index avg `0.0003` n `23`; metal avg `0.0008` n `20`; unknown avg `0.0658` n `764`
- 1h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.4549` n `228`; crypto_major avg `0.6009` n `8`; equity avg `0.0936` n `88`; fx avg `0.0022` n `6`; index avg `0.0172` n `23`; metal avg `0.0016` n `20`; unknown avg `3.0316` n `764`
- 4h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.66` n `228`; crypto_major avg `0.4802` n `8`; equity avg `0.2813` n `88`; fx avg `-0.0031` n `6`; index avg `0.049` n `23`; metal avg `0.0624` n `20`; unknown avg `1.1697` n `764`
- 24h: commodity avg `-0.2182` n `12`; crypto_alt avg `3.7239` n `228`; crypto_major avg `3.5705` n `8`; equity avg `1.7808` n `87`; fx avg `-0.0135` n `6`; index avg `0.0886` n `23`; metal avg `1.4042` n `20`; unknown avg `0.4143` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
