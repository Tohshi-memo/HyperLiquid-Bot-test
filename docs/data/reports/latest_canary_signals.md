# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T02:22:13.746008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `-0.1126` n `228`; crypto_major avg `-0.1867` n `8`; equity avg `-0.0843` n `67`; fx avg `-0.0167` n `6`; index avg `-0.0073` n `23`; metal avg `-0.0708` n `18`; unknown avg `0.0079` n `396`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.0549` n `228`; crypto_major avg `-0.1451` n `8`; equity avg `0.0274` n `67`; fx avg `-0.0109` n `6`; index avg `0.0313` n `23`; metal avg `-0.0983` n `18`; unknown avg `0.7152` n `396`
- 4h: commodity avg `-0.0378` n `12`; crypto_alt avg `0.5651` n `228`; crypto_major avg `0.0405` n `8`; equity avg `0.2785` n `67`; fx avg `-0.1409` n `6`; index avg `0.1675` n `23`; metal avg `0.1773` n `18`; unknown avg `0.2865` n `396`
- 24h: commodity avg `0.3872` n `12`; crypto_alt avg `-1.1369` n `228`; crypto_major avg `0.0052` n `8`; equity avg `0.2393` n `67`; fx avg `-0.0453` n `6`; index avg `-0.1796` n `23`; metal avg `0.5622` n `18`; unknown avg `-0.5033` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
