# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T23:52:30.568102+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `0.1469` n `239`; crypto_major avg `0.1514` n `8`; equity avg `0.1647` n `168`; fx avg `-0.0013` n `6`; index avg `0.0207` n `27`; metal avg `0.0105` n `20`; unknown avg `2.0515` n `1267`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.2275` n `239`; crypto_major avg `0.1188` n `8`; equity avg `0.2182` n `168`; fx avg `0.0075` n `6`; index avg `0.0338` n `27`; metal avg `-0.0074` n `20`; unknown avg `1.5609` n `1207`
- 4h: commodity avg `0.1054` n `13`; crypto_alt avg `0.379` n `239`; crypto_major avg `0.2474` n `8`; equity avg `0.673` n `168`; fx avg `-0.0174` n `6`; index avg `0.0454` n `27`; metal avg `0.3182` n `20`; unknown avg `180.9354` n `1143`
- 24h: commodity avg `0.3917` n `13`; crypto_alt avg `2.5493` n `239`; crypto_major avg `1.2136` n `8`; equity avg `0.1795` n `168`; fx avg `0.0237` n `6`; index avg `-0.0166` n `27`; metal avg `0.3004` n `20`; unknown avg `770.3955` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
