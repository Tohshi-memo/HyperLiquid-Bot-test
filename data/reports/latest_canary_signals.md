# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T00:22:28.387316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.1733` n `228`; crypto_major avg `-0.2904` n `8`; equity avg `-0.0519` n `88`; fx avg `0.0072` n `6`; index avg `-0.0003` n `23`; metal avg `-0.018` n `20`; unknown avg `-0.0364` n `764`
- 1h: commodity avg `0.0604` n `12`; crypto_alt avg `0.074` n `228`; crypto_major avg `-0.0211` n `8`; equity avg `0.0258` n `88`; fx avg `-0.0427` n `6`; index avg `0.02` n `23`; metal avg `0.0122` n `20`; unknown avg `-0.1103` n `764`
- 4h: commodity avg `0.2345` n `12`; crypto_alt avg `-0.2092` n `228`; crypto_major avg `-0.1341` n `8`; equity avg `0.1636` n `88`; fx avg `0.0649` n `6`; index avg `0.0248` n `23`; metal avg `0.1805` n `20`; unknown avg `-0.0224` n `748`
- 24h: commodity avg `-0.2275` n `12`; crypto_alt avg `1.2629` n `228`; crypto_major avg `1.0771` n `8`; equity avg `0.0167` n `87`; fx avg `-0.0347` n `6`; index avg `-0.2466` n `23`; metal avg `0.8386` n `20`; unknown avg `0.184` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2135`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
