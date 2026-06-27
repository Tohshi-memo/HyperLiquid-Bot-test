# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T13:22:29.145325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.0778` n `228`; crypto_major avg `0.1003` n `8`; equity avg `0.0169` n `88`; fx avg `-0.0013` n `6`; index avg `0.0065` n `23`; metal avg `-0.0051` n `20`; unknown avg `-0.0009` n `764`
- 1h: commodity avg `0.0015` n `12`; crypto_alt avg `0.0821` n `228`; crypto_major avg `0.3433` n `8`; equity avg `0.0789` n `88`; fx avg `-0.0013` n `6`; index avg `0.0114` n `23`; metal avg `0.0012` n `20`; unknown avg `0.043` n `764`
- 4h: commodity avg `0.0891` n `12`; crypto_alt avg `0.5123` n `228`; crypto_major avg `0.4576` n `8`; equity avg `0.0799` n `88`; fx avg `0.0385` n `6`; index avg `0.001` n `23`; metal avg `-0.0016` n `20`; unknown avg `0.2141` n `764`
- 24h: commodity avg `0.1501` n `12`; crypto_alt avg `2.9` n `228`; crypto_major avg `2.9735` n `8`; equity avg `2.5371` n `87`; fx avg `0.0077` n `6`; index avg `0.1721` n `23`; metal avg `0.3608` n `20`; unknown avg `0.4464` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
