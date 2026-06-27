# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T01:37:31.081610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0996` n `228`; crypto_major avg `-0.1199` n `8`; equity avg `0.0727` n `88`; fx avg `0.0006` n `6`; index avg `-0.0058` n `23`; metal avg `0.006` n `20`; unknown avg `-0.0881` n `764`
- 1h: commodity avg `0.0167` n `12`; crypto_alt avg `0.1317` n `228`; crypto_major avg `0.0785` n `8`; equity avg `0.1275` n `88`; fx avg `0.0116` n `6`; index avg `0.0068` n `23`; metal avg `0.0167` n `20`; unknown avg `-0.0565` n `764`
- 4h: commodity avg `0.0369` n `12`; crypto_alt avg `-0.0812` n `228`; crypto_major avg `-0.1667` n `8`; equity avg `0.3054` n `88`; fx avg `-0.0519` n `6`; index avg `0.0359` n `23`; metal avg `0.0841` n `20`; unknown avg `0.124` n `748`
- 24h: commodity avg `-0.2215` n `12`; crypto_alt avg `2.0423` n `228`; crypto_major avg `1.8697` n `8`; equity avg `0.6548` n `87`; fx avg `-0.0408` n `6`; index avg `-0.1468` n `23`; metal avg `0.9451` n `20`; unknown avg `0.2246` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
