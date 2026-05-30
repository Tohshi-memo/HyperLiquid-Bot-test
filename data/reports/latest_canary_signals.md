# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T01:22:19.361764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0441` n `12`; crypto_alt avg `0.2371` n `228`; crypto_major avg `0.2463` n `8`; equity avg `0.0422` n `69`; fx avg `-0.0014` n `6`; index avg `0.0458` n `23`; metal avg `0.0083` n `18`; unknown avg `-0.0133` n `419`
- 1h: commodity avg `-0.1165` n `12`; crypto_alt avg `0.729` n `228`; crypto_major avg `0.5975` n `8`; equity avg `0.2117` n `69`; fx avg `-0.0011` n `6`; index avg `-0.006` n `23`; metal avg `-0.0119` n `18`; unknown avg `0.0486` n `419`
- 4h: commodity avg `0.1146` n `12`; crypto_alt avg `0.7726` n `228`; crypto_major avg `0.5632` n `8`; equity avg `0.1919` n `69`; fx avg `-0.0172` n `6`; index avg `0.0584` n `23`; metal avg `0.0799` n `18`; unknown avg `-0.4707` n `419`
- 24h: commodity avg `-0.2352` n `12`; crypto_alt avg `1.4277` n `228`; crypto_major avg `1.5968` n `8`; equity avg `1.1259` n `69`; fx avg `0.0827` n `6`; index avg `0.2034` n `23`; metal avg `-0.4535` n `18`; unknown avg `0.384` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
