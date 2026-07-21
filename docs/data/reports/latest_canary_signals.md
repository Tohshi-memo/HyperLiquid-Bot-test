# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T00:22:38.050497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.1392` n `230`; crypto_major avg `0.1907` n `8`; equity avg `0.2986` n `98`; fx avg `0.0052` n `6`; index avg `0.0981` n `25`; metal avg `0.0741` n `20`; unknown avg `0.7286` n `771`
- 1h: commodity avg `0.0111` n `12`; crypto_alt avg `0.1056` n `230`; crypto_major avg `0.0932` n `8`; equity avg `-0.1382` n `98`; fx avg `0.0342` n `6`; index avg `-0.0845` n `25`; metal avg `0.0385` n `20`; unknown avg `-0.2943` n `770`
- 4h: commodity avg `0.0414` n `12`; crypto_alt avg `0.1068` n `230`; crypto_major avg `0.1154` n `8`; equity avg `0.1173` n `98`; fx avg `0.0198` n `6`; index avg `-0.0355` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.3739` n `770`
- 24h: commodity avg `-0.3007` n `12`; crypto_alt avg `1.1451` n `230`; crypto_major avg `0.854` n `8`; equity avg `-1.0602` n `98`; fx avg `-0.1599` n `6`; index avg `-0.2327` n `25`; metal avg `0.083` n `20`; unknown avg `-0.121` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1095`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `666`, weak_sample_signal
