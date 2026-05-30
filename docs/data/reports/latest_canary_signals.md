# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T06:22:20.121425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.0477` n `228`; crypto_major avg `0.0535` n `8`; equity avg `-0.0102` n `69`; fx avg `0.0006` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0121` n `18`; unknown avg `-0.0035` n `421`
- 1h: commodity avg `-0.0433` n `12`; crypto_alt avg `0.0383` n `228`; crypto_major avg `0.1295` n `8`; equity avg `0.0063` n `69`; fx avg `0.0062` n `6`; index avg `0.046` n `23`; metal avg `0.0123` n `18`; unknown avg `0.0137` n `401`
- 4h: commodity avg `-0.0786` n `12`; crypto_alt avg `-0.2016` n `228`; crypto_major avg `0.0031` n `8`; equity avg `0.1627` n `69`; fx avg `0.0062` n `6`; index avg `0.0856` n `23`; metal avg `-0.01` n `18`; unknown avg `0.9326` n `401`
- 24h: commodity avg `-0.1372` n `12`; crypto_alt avg `1.3364` n `228`; crypto_major avg `1.6868` n `8`; equity avg `0.7978` n `69`; fx avg `0.0573` n `6`; index avg `-0.0015` n `23`; metal avg `-0.1097` n `18`; unknown avg `1.5144` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
