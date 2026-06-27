# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T12:07:31.701975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `0.0733` n `228`; crypto_major avg `-0.1217` n `8`; equity avg `0.0097` n `88`; fx avg `-0.001` n `6`; index avg `0.0018` n `23`; metal avg `0.0021` n `20`; unknown avg `0.0043` n `764`
- 1h: commodity avg `0.0829` n `12`; crypto_alt avg `0.1701` n `228`; crypto_major avg `-0.0853` n `8`; equity avg `-0.0448` n `88`; fx avg `-0.0017` n `6`; index avg `-0.0047` n `23`; metal avg `-0.0047` n `20`; unknown avg `0.1832` n `764`
- 4h: commodity avg `0.1154` n `12`; crypto_alt avg `-0.1128` n `228`; crypto_major avg `-0.5247` n `8`; equity avg `-0.0239` n `88`; fx avg `0.0111` n `6`; index avg `-0.0215` n `23`; metal avg `-0.0146` n `20`; unknown avg `0.0337` n `764`
- 24h: commodity avg `0.1274` n `12`; crypto_alt avg `2.0823` n `228`; crypto_major avg `1.9282` n `8`; equity avg `1.8368` n `87`; fx avg `0.0369` n `6`; index avg `0.0669` n `23`; metal avg `0.3753` n `20`; unknown avg `0.1742` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
