# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T13:52:30.556171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `0.1876` n `228`; crypto_major avg `0.1016` n `8`; equity avg `0.0595` n `88`; fx avg `-0.0006` n `6`; index avg `-0.0216` n `23`; metal avg `0.0086` n `20`; unknown avg `0.0447` n `764`
- 1h: commodity avg `0.0442` n `12`; crypto_alt avg `0.3038` n `228`; crypto_major avg `0.3659` n `8`; equity avg `0.1226` n `88`; fx avg `-0.0013` n `6`; index avg `-0.0088` n `23`; metal avg `0.0102` n `20`; unknown avg `0.0166` n `764`
- 4h: commodity avg `0.1332` n `12`; crypto_alt avg `0.4947` n `228`; crypto_major avg `0.5806` n `8`; equity avg `0.1291` n `88`; fx avg `0.0096` n `6`; index avg `-0.0136` n `23`; metal avg `0.0167` n `20`; unknown avg `0.2593` n `764`
- 24h: commodity avg `0.334` n `12`; crypto_alt avg `2.0918` n `228`; crypto_major avg `2.0417` n `8`; equity avg `1.8832` n `87`; fx avg `0.024` n `6`; index avg `0.1311` n `23`; metal avg `0.3008` n `20`; unknown avg `0.4546` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
