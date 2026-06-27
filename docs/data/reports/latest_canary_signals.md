# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T00:07:27.609647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0592` n `12`; crypto_alt avg `0.2124` n `228`; crypto_major avg `0.1847` n `8`; equity avg `0.0658` n `88`; fx avg `0.01` n `6`; index avg `0.0079` n `23`; metal avg `0.0169` n `20`; unknown avg `-0.1231` n `764`
- 1h: commodity avg `0.1128` n `12`; crypto_alt avg `0.1936` n `228`; crypto_major avg `0.1444` n `8`; equity avg `0.1166` n `88`; fx avg `0.0071` n `6`; index avg `0.0264` n `23`; metal avg `0.0442` n `20`; unknown avg `-0.0271` n `764`
- 4h: commodity avg `0.2907` n `12`; crypto_alt avg `-0.1909` n `228`; crypto_major avg `-0.1288` n `8`; equity avg `0.3076` n `88`; fx avg `0.0597` n `6`; index avg `0.0563` n `23`; metal avg `0.1953` n `20`; unknown avg `0.0023` n `748`
- 24h: commodity avg `-0.1433` n `12`; crypto_alt avg `1.5631` n `228`; crypto_major avg `1.3975` n `8`; equity avg `-0.1591` n `87`; fx avg `-0.0047` n `6`; index avg `-0.3215` n `23`; metal avg `0.9032` n `20`; unknown avg `0.2705` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
