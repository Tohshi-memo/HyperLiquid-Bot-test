# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T00:37:21.322830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.69` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.1718` n `228`; crypto_major avg `0.2296` n `8`; equity avg `0.2142` n `69`; fx avg `-0.0052` n `6`; index avg `0.0155` n `23`; metal avg `0.0111` n `18`; unknown avg `-0.2701` n `422`
- 1h: commodity avg `-0.2686` n `12`; crypto_alt avg `-0.2465` n `228`; crypto_major avg `-0.0391` n `8`; equity avg `-0.517` n `69`; fx avg `0.013` n `6`; index avg `-0.2453` n `23`; metal avg `0.1025` n `18`; unknown avg `0.5517` n `422`
- 4h: commodity avg `-0.2184` n `12`; crypto_alt avg `-0.2512` n `228`; crypto_major avg `0.1512` n `8`; equity avg `-0.6144` n `69`; fx avg `-0.0025` n `6`; index avg `-0.4153` n `23`; metal avg `0.156` n `18`; unknown avg `0.6665` n `422`
- 24h: commodity avg `-0.281` n `12`; crypto_alt avg `-0.722` n `228`; crypto_major avg `-1.2033` n `8`; equity avg `-0.6902` n `69`; fx avg `0.0219` n `6`; index avg `-0.3587` n `23`; metal avg `-0.2202` n `18`; unknown avg `2.2552` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
