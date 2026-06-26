# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T20:59:47.824519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0561` n `12`; crypto_alt avg `-0.0124` n `228`; crypto_major avg `-0.0857` n `8`; equity avg `0.0065` n `88`; fx avg `0.0019` n `6`; index avg `-0.0165` n `23`; metal avg `0.1778` n `20`; unknown avg `-0.2809` n `764`
- 1h: commodity avg `0.1632` n `12`; crypto_alt avg `-0.4682` n `228`; crypto_major avg `-0.7307` n `8`; equity avg `-0.0872` n `88`; fx avg `0.0072` n `6`; index avg `-0.0721` n `23`; metal avg `0.0554` n `20`; unknown avg `-0.7406` n `764`
- 4h: commodity avg `0.077` n `12`; crypto_alt avg `-0.1539` n `228`; crypto_major avg `-0.4184` n `8`; equity avg `-0.2482` n `87`; fx avg `-0.0056` n `6`; index avg `-0.1977` n `23`; metal avg `-0.0353` n `20`; unknown avg `-0.4001` n `764`
- 24h: commodity avg `-0.2334` n `12`; crypto_alt avg `2.283` n `228`; crypto_major avg `2.0995` n `8`; equity avg `-0.6533` n `87`; fx avg `-0.0776` n `6`; index avg `-0.3836` n `23`; metal avg `0.6966` n `20`; unknown avg `-0.4055` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2224`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2159`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
