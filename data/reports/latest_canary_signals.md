# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T17:52:16.887950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `12`; crypto_alt avg `0.1083` n `228`; crypto_major avg `0.1139` n `8`; equity avg `-0.0003` n `69`; fx avg `0.0` n `6`; index avg `0.0402` n `23`; metal avg `0.0009` n `18`; unknown avg `-0.2119` n `421`
- 1h: commodity avg `0.137` n `12`; crypto_alt avg `0.6761` n `228`; crypto_major avg `0.5593` n `8`; equity avg `0.1114` n `69`; fx avg `0.0015` n `6`; index avg `0.2038` n `23`; metal avg `-0.0367` n `18`; unknown avg `0.0786` n `421`
- 4h: commodity avg `0.1618` n `12`; crypto_alt avg `-0.8127` n `228`; crypto_major avg `-0.523` n `8`; equity avg `0.0114` n `69`; fx avg `-0.0084` n `6`; index avg `0.3377` n `23`; metal avg `-0.0624` n `18`; unknown avg `0.0832` n `421`
- 24h: commodity avg `0.7392` n `12`; crypto_alt avg `-0.9923` n `228`; crypto_major avg `-0.447` n `8`; equity avg `0.9544` n `69`; fx avg `-0.0116` n `6`; index avg `0.1936` n `23`; metal avg `-0.157` n `18`; unknown avg `0.428` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
