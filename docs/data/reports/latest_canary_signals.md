# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T03:52:26.252871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0377` n `12`; crypto_alt avg `0.0052` n `228`; crypto_major avg `-0.0067` n `8`; equity avg `-0.0014` n `88`; fx avg `-0.0009` n `6`; index avg `-0.0002` n `23`; metal avg `-0.0062` n `20`; unknown avg `0.7217` n `764`
- 1h: commodity avg `-0.1811` n `12`; crypto_alt avg `0.2748` n `228`; crypto_major avg `0.1036` n `8`; equity avg `0.0465` n `88`; fx avg `-0.002` n `6`; index avg `0.0114` n `23`; metal avg `0.0242` n `20`; unknown avg `0.6865` n `764`
- 4h: commodity avg `0.0344` n `12`; crypto_alt avg `0.3437` n `228`; crypto_major avg `0.1244` n `8`; equity avg `-0.0275` n `88`; fx avg `-0.0303` n `6`; index avg `-0.0268` n `23`; metal avg `0.058` n `20`; unknown avg `15.7747` n `722`
- 24h: commodity avg `0.2164` n `12`; crypto_alt avg `-0.5355` n `228`; crypto_major avg `-1.2059` n `8`; equity avg `0.0844` n `88`; fx avg `-0.0189` n `6`; index avg `-0.1121` n `23`; metal avg `-0.027` n `20`; unknown avg `9.8141` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2183`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
