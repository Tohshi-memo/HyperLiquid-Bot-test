# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T04:37:31.086977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.032` n `12`; crypto_alt avg `-0.3503` n `228`; crypto_major avg `-0.2834` n `8`; equity avg `0.0186` n `74`; fx avg `0.0064` n `6`; index avg `-0.0974` n `23`; metal avg `0.1041` n `18`; unknown avg `-0.048` n `645`
- 1h: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.0761` n `228`; crypto_major avg `-0.1339` n `8`; equity avg `0.0042` n `74`; fx avg `0.0208` n `6`; index avg `-0.146` n `23`; metal avg `0.0675` n `18`; unknown avg `0.7268` n `645`
- 4h: commodity avg `-0.1003` n `12`; crypto_alt avg `0.46` n `228`; crypto_major avg `0.115` n `8`; equity avg `0.2301` n `74`; fx avg `0.0686` n `6`; index avg `-0.0475` n `23`; metal avg `0.0904` n `18`; unknown avg `-0.2402` n `629`
- 24h: commodity avg `-0.9309` n `12`; crypto_alt avg `2.5123` n `228`; crypto_major avg `2.5687` n `8`; equity avg `1.8544` n `74`; fx avg `0.0379` n `6`; index avg `0.7345` n `23`; metal avg `2.0664` n `18`; unknown avg `3.3104` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
