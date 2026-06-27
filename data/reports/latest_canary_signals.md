# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T02:22:30.883658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0321` n `12`; crypto_alt avg `0.4887` n `228`; crypto_major avg `0.6181` n `8`; equity avg `0.0818` n `88`; fx avg `0.0099` n `6`; index avg `0.006` n `23`; metal avg `0.0041` n `20`; unknown avg `5.0659` n `764`
- 1h: commodity avg `-0.1903` n `12`; crypto_alt avg `0.3747` n `228`; crypto_major avg `0.5568` n `8`; equity avg `0.1549` n `88`; fx avg `0.0075` n `6`; index avg `0.0111` n `23`; metal avg `0.0068` n `20`; unknown avg `5.0419` n `764`
- 4h: commodity avg `-0.1203` n `12`; crypto_alt avg `0.6429` n `228`; crypto_major avg `0.6082` n `8`; equity avg `0.2644` n `88`; fx avg `0.0129` n `6`; index avg `0.0501` n `23`; metal avg `0.0778` n `20`; unknown avg `1.075` n `764`
- 24h: commodity avg `-0.3518` n `12`; crypto_alt avg `4.3334` n `228`; crypto_major avg `4.0558` n `8`; equity avg `1.6249` n `87`; fx avg `-0.0211` n `6`; index avg `0.0346` n `23`; metal avg `1.185` n `20`; unknown avg `0.3962` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
