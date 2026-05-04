# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T19:00:31.865867+00:00`
- Correlation status: `ready`
- Asset price records: `290`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0652` n `7`; crypto_alt avg `0.0359` n `223`; crypto_major avg `0.0586` n `7`; equity avg `0.1064` n `42`; fx avg `-0.0195` n `4`; index avg `0.0295` n `9`; metal avg `0.0877` n `7`; unknown avg `-0.0569` n `314`
- 1h: commodity avg `0.1093` n `7`; crypto_alt avg `-0.0514` n `223`; crypto_major avg `-0.302` n `7`; equity avg `-0.1083` n `42`; fx avg `-0.0246` n `4`; index avg `-0.0165` n `9`; metal avg `-0.1151` n `7`; unknown avg `-0.1223` n `314`
- 4h: commodity avg `0.5254` n `7`; crypto_alt avg `0.1912` n `223`; crypto_major avg `-0.4096` n `7`; equity avg `-1.0803` n `42`; fx avg `-0.0338` n `4`; index avg `-0.5599` n `9`; metal avg `-0.755` n `7`; unknown avg `-0.3909` n `314`
- 24h: commodity avg `1.6591` n `7`; crypto_alt avg `2.0328` n `223`; crypto_major avg `1.1889` n `7`; equity avg `-0.2564` n `42`; fx avg `-0.0719` n `4`; index avg `0.4872` n `9`; metal avg `-2.3455` n `7`; unknown avg `-0.9741` n `312`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2378`, n `286`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2322`, n `286`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.166`, n `282`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.165`, n `282`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1495`, n `286`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `286`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `286`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.134`, n `282`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1339`, n `282`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `286`, weak_sample_signal
