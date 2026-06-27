# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T11:37:27.973100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `-0.0604` n `228`; crypto_major avg `-0.0898` n `8`; equity avg `0.0044` n `88`; fx avg `0.0` n `6`; index avg `0.0024` n `23`; metal avg `-0.009` n `20`; unknown avg `3.2398` n `764`
- 1h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.2624` n `228`; crypto_major avg `-0.2981` n `8`; equity avg `-0.0306` n `88`; fx avg `0.0105` n `6`; index avg `-0.0233` n `23`; metal avg `-0.0117` n `20`; unknown avg `0.195` n `764`
- 4h: commodity avg `0.1003` n `12`; crypto_alt avg `-0.4703` n `228`; crypto_major avg `-0.4169` n `8`; equity avg `0.0452` n `88`; fx avg `-0.0212` n `6`; index avg `-0.0276` n `23`; metal avg `-0.0261` n `20`; unknown avg `0.0089` n `764`
- 24h: commodity avg `0.0472` n `12`; crypto_alt avg `1.6908` n `228`; crypto_major avg `1.6529` n `8`; equity avg `1.8155` n `87`; fx avg `0.0343` n `6`; index avg `0.052` n `23`; metal avg `0.3166` n `20`; unknown avg `0.1339` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
