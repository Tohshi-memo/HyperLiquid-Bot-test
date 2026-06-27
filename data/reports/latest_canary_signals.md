# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T02:07:27.158351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1102` n `12`; crypto_alt avg `0.0829` n `228`; crypto_major avg `0.0781` n `8`; equity avg `0.049` n `88`; fx avg `-0.0037` n `6`; index avg `0.0083` n `23`; metal avg `-0.001` n `20`; unknown avg `-0.7293` n `764`
- 1h: commodity avg `-0.1584` n `12`; crypto_alt avg `-0.0864` n `228`; crypto_major avg `0.0248` n `8`; equity avg `0.1638` n `88`; fx avg `-0.0145` n `6`; index avg `0.0092` n `23`; metal avg `0.0113` n `20`; unknown avg `-0.4905` n `764`
- 4h: commodity avg `-0.0801` n `12`; crypto_alt avg `0.1869` n `228`; crypto_major avg `0.1101` n `8`; equity avg `0.2241` n `88`; fx avg `-0.0056` n `6`; index avg `0.0408` n `23`; metal avg `0.0664` n `20`; unknown avg `-0.2863` n `748`
- 24h: commodity avg `-0.3131` n `12`; crypto_alt avg `2.0623` n `228`; crypto_major avg `1.8686` n `8`; equity avg `0.9466` n `87`; fx avg `-0.0365` n `6`; index avg `-0.0536` n `23`; metal avg `1.056` n `20`; unknown avg `-0.0363` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2103`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
