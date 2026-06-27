# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T09:22:25.090592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.3063` n `228`; crypto_major avg `-0.3428` n `8`; equity avg `-0.0113` n `88`; fx avg `-0.0174` n `6`; index avg `-0.0015` n `23`; metal avg `-0.0097` n `20`; unknown avg `-0.0627` n `764`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `-0.3307` n `228`; crypto_major avg `-0.3451` n `8`; equity avg `-0.0192` n `88`; fx avg `-0.0477` n `6`; index avg `-0.0045` n `23`; metal avg `-0.0079` n `20`; unknown avg `-0.1359` n `764`
- 4h: commodity avg `0.0662` n `12`; crypto_alt avg `-0.3576` n `228`; crypto_major avg `-0.344` n `8`; equity avg `0.1753` n `88`; fx avg `-0.0298` n `6`; index avg `0.0106` n `23`; metal avg `-0.0163` n `20`; unknown avg `-0.0929` n `716`
- 24h: commodity avg `0.165` n `12`; crypto_alt avg `0.7804` n `228`; crypto_major avg `0.6982` n `8`; equity avg `1.7993` n `87`; fx avg `0.0073` n `6`; index avg `0.0898` n `23`; metal avg `0.4752` n `20`; unknown avg `-0.2721` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
