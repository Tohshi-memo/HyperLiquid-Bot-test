# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T03:07:29.072382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0516` n `12`; crypto_alt avg `-0.3326` n `228`; crypto_major avg `-0.3919` n `8`; equity avg `0.0034` n `88`; fx avg `0.0002` n `6`; index avg `-0.0027` n `23`; metal avg `0.0062` n `20`; unknown avg `0.0313` n `764`
- 1h: commodity avg `0.1157` n `12`; crypto_alt avg `0.3194` n `228`; crypto_major avg `0.318` n `8`; equity avg `0.0853` n `88`; fx avg `0.0086` n `6`; index avg `0.0053` n `23`; metal avg `0.0143` n `20`; unknown avg `8.5454` n `764`
- 4h: commodity avg `0.0265` n `12`; crypto_alt avg `0.2143` n `228`; crypto_major avg `-0.0285` n `8`; equity avg `0.2163` n `88`; fx avg `0.02` n `6`; index avg `0.0465` n `23`; metal avg `0.0422` n `20`; unknown avg `0.4507` n `764`
- 24h: commodity avg `-0.0904` n `12`; crypto_alt avg `3.9311` n `228`; crypto_major avg `3.4933` n `8`; equity avg `2.2315` n `87`; fx avg `-0.0081` n `6`; index avg `0.2082` n `23`; metal avg `1.4111` n `20`; unknown avg `0.4758` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2089`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
