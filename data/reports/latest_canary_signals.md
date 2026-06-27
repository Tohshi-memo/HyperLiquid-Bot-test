# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T01:52:29.762961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `12`; crypto_alt avg `-0.096` n `228`; crypto_major avg `-0.019` n `8`; equity avg `-0.0477` n `88`; fx avg `0.0007` n `6`; index avg `0.0026` n `23`; metal avg `-0.0023` n `20`; unknown avg `-0.0261` n `764`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.1948` n `228`; crypto_major avg `-0.1621` n `8`; equity avg `0.111` n `88`; fx avg `0.0057` n `6`; index avg `0.0103` n `23`; metal avg `0.014` n `20`; unknown avg `-0.5123` n `764`
- 4h: commodity avg `0.0304` n `12`; crypto_alt avg `-0.1803` n `228`; crypto_major avg `-0.2468` n `8`; equity avg `0.1963` n `88`; fx avg `-0.026` n `6`; index avg `0.0331` n `23`; metal avg `0.0596` n `20`; unknown avg `-0.2127` n `748`
- 24h: commodity avg `-0.2146` n `12`; crypto_alt avg `1.865` n `228`; crypto_major avg `1.6594` n `8`; equity avg `0.6538` n `87`; fx avg `-0.0256` n `6`; index avg `-0.1016` n `23`; metal avg `1.0617` n `20`; unknown avg `0.0267` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
