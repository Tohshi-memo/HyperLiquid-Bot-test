# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T23:58:45.177312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.1538` n `228`; crypto_major avg `0.2411` n `8`; equity avg `0.0065` n `69`; fx avg `-0.0078` n `6`; index avg `-0.0241` n `23`; metal avg `0.0188` n `18`; unknown avg `0.7982` n `419`
- 1h: commodity avg `0.1416` n `12`; crypto_alt avg `0.2081` n `228`; crypto_major avg `0.1736` n `8`; equity avg `0.0127` n `69`; fx avg `-0.0133` n `6`; index avg `0.0613` n `23`; metal avg `0.0159` n `18`; unknown avg `0.5546` n `419`
- 4h: commodity avg `0.199` n `12`; crypto_alt avg `-0.0261` n `228`; crypto_major avg `-0.3084` n `8`; equity avg `0.1039` n `69`; fx avg `-0.046` n `6`; index avg `0.0607` n `23`; metal avg `-0.074` n `18`; unknown avg `-0.447` n `419`
- 24h: commodity avg `-0.3047` n `12`; crypto_alt avg `0.7097` n `228`; crypto_major avg `0.8652` n `8`; equity avg `0.7992` n `69`; fx avg `0.152` n `6`; index avg `0.1604` n `23`; metal avg `0.1059` n `18`; unknown avg `1.3686` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
