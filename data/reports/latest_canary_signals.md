# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T01:52:19.327916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `0.0356` n `228`; crypto_major avg `-0.0645` n `8`; equity avg `-0.0483` n `67`; fx avg `-0.0066` n `6`; index avg `-0.0131` n `23`; metal avg `-0.2193` n `18`; unknown avg `-0.494` n `419`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `-0.5689` n `228`; crypto_major avg `-0.2406` n `8`; equity avg `-0.1287` n `67`; fx avg `0.0189` n `6`; index avg `-0.0308` n `23`; metal avg `-0.9557` n `18`; unknown avg `-0.2447` n `419`
- 4h: commodity avg `0.2091` n `12`; crypto_alt avg `-0.5135` n `228`; crypto_major avg `-0.4546` n `8`; equity avg `-0.4068` n `67`; fx avg `0.0077` n `6`; index avg `-0.1807` n `23`; metal avg `-0.8509` n `18`; unknown avg `-0.2502` n `419`
- 24h: commodity avg `-0.7082` n `12`; crypto_alt avg `-2.8906` n `228`; crypto_major avg `-1.9679` n `8`; equity avg `-0.7759` n `67`; fx avg `-0.0503` n `6`; index avg `-0.7717` n `23`; metal avg `-2.0521` n `18`; unknown avg `-1.1237` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
