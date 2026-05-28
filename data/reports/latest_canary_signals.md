# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T01:37:17.147246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.1445` n `228`; crypto_major avg `-0.0539` n `8`; equity avg `-0.0981` n `67`; fx avg `0.0179` n `6`; index avg `-0.006` n `23`; metal avg `-0.1116` n `18`; unknown avg `0.2614` n `419`
- 1h: commodity avg `-0.153` n `12`; crypto_alt avg `-0.5763` n `228`; crypto_major avg `-0.2563` n `8`; equity avg `0.1062` n `67`; fx avg `-0.0016` n `6`; index avg `0.0891` n `23`; metal avg `-0.6737` n `18`; unknown avg `1.3135` n `419`
- 4h: commodity avg `0.2502` n `12`; crypto_alt avg `-1.8649` n `228`; crypto_major avg `-1.1453` n `8`; equity avg `-0.3987` n `67`; fx avg `0.0116` n `6`; index avg `-0.2036` n `23`; metal avg `-0.6729` n `18`; unknown avg `1.9356` n `419`
- 24h: commodity avg `-0.6092` n `12`; crypto_alt avg `-2.8394` n `228`; crypto_major avg `-1.8154` n `8`; equity avg `-0.8265` n `67`; fx avg `-0.0465` n `6`; index avg `-0.8083` n `23`; metal avg `-2.0879` n `18`; unknown avg `-0.5969` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
