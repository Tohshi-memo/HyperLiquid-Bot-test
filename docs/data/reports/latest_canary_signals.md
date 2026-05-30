# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T01:37:24.498013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1139` n `12`; crypto_alt avg `0.2999` n `228`; crypto_major avg `0.2025` n `8`; equity avg `0.0562` n `69`; fx avg `0.0078` n `6`; index avg `-0.0118` n `23`; metal avg `0.0115` n `18`; unknown avg `0.0315` n `419`
- 1h: commodity avg `0.008` n `12`; crypto_alt avg `0.8809` n `228`; crypto_major avg `0.7068` n `8`; equity avg `0.2259` n `69`; fx avg `0.0049` n `6`; index avg `0.0009` n `23`; metal avg `0.0188` n `18`; unknown avg `-0.0688` n `419`
- 4h: commodity avg `0.3585` n `12`; crypto_alt avg `1.3952` n `228`; crypto_major avg `1.0041` n `8`; equity avg `0.191` n `69`; fx avg `-0.0019` n `6`; index avg `0.0889` n `23`; metal avg `0.0992` n `18`; unknown avg `-0.3208` n `419`
- 24h: commodity avg `-0.216` n `12`; crypto_alt avg `1.7585` n `228`; crypto_major avg `1.9401` n `8`; equity avg `1.2097` n `69`; fx avg `0.0919` n `6`; index avg `0.2552` n `23`; metal avg `-0.23` n `18`; unknown avg `0.5143` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
