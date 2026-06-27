# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T15:37:29.053896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.2382` n `228`; crypto_major avg `0.1271` n `8`; equity avg `0.02` n `88`; fx avg `0.0081` n `6`; index avg `0.0005` n `23`; metal avg `0.0066` n `20`; unknown avg `0.0226` n `764`
- 1h: commodity avg `-0.0451` n `12`; crypto_alt avg `0.5529` n `228`; crypto_major avg `0.5467` n `8`; equity avg `0.0296` n `88`; fx avg `0.0094` n `6`; index avg `0.0111` n `23`; metal avg `0.0038` n `20`; unknown avg `0.0839` n `764`
- 4h: commodity avg `0.0222` n `12`; crypto_alt avg `1.302` n `228`; crypto_major avg `1.3694` n `8`; equity avg `0.1678` n `88`; fx avg `0.0083` n `6`; index avg `0.031` n `23`; metal avg `0.0334` n `20`; unknown avg `0.3696` n `764`
- 24h: commodity avg `0.3402` n `12`; crypto_alt avg `1.1254` n `228`; crypto_major avg `0.8975` n `8`; equity avg `0.4959` n `87`; fx avg `0.0822` n `6`; index avg `-0.1088` n `23`; metal avg `-0.0641` n `20`; unknown avg `0.3368` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
