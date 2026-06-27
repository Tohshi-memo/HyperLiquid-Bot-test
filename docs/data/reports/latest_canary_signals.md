# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T15:22:25.737543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `0.0639` n `228`; crypto_major avg `0.1548` n `8`; equity avg `-0.0056` n `88`; fx avg `-0.007` n `6`; index avg `0.0028` n `23`; metal avg `0.0112` n `20`; unknown avg `0.0591` n `764`
- 1h: commodity avg `-0.0342` n `12`; crypto_alt avg `0.1662` n `228`; crypto_major avg `0.3405` n `8`; equity avg `-0.0096` n `88`; fx avg `0.0019` n `6`; index avg `0.0021` n `23`; metal avg `0.0014` n `20`; unknown avg `-0.0123` n `764`
- 4h: commodity avg `0.0674` n `12`; crypto_alt avg `0.9989` n `228`; crypto_major avg `1.1495` n `8`; equity avg `0.1522` n `88`; fx avg `0.0003` n `6`; index avg `0.0328` n `23`; metal avg `0.0178` n `20`; unknown avg `4.3711` n `764`
- 24h: commodity avg `0.4463` n `12`; crypto_alt avg `1.4565` n `228`; crypto_major avg `1.458` n `8`; equity avg `0.9962` n `87`; fx avg `0.0664` n `6`; index avg `-0.0074` n `23`; metal avg `0.0375` n `20`; unknown avg `0.3553` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
