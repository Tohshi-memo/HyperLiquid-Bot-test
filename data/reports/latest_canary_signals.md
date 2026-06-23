# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T15:42:05.116850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `-0.1337` n `228`; crypto_major avg `-0.0725` n `8`; equity avg `-0.0574` n `86`; fx avg `-0.0143` n `6`; index avg `-0.0556` n `23`; metal avg `0.1209` n `20`; unknown avg `-0.1845` n `764`
- 1h: commodity avg `0.063` n `12`; crypto_alt avg `-0.927` n `228`; crypto_major avg `-1.0012` n `8`; equity avg `-0.9464` n `86`; fx avg `-0.0292` n `6`; index avg `-0.1349` n `23`; metal avg `0.174` n `20`; unknown avg `-0.4731` n `764`
- 4h: commodity avg `-0.2235` n `12`; crypto_alt avg `-0.4433` n `228`; crypto_major avg `-0.703` n `8`; equity avg `0.3259` n `86`; fx avg `-0.0908` n `6`; index avg `-0.0468` n `23`; metal avg `0.1741` n `20`; unknown avg `-0.4236` n `764`
- 24h: commodity avg `-0.3354` n `12`; crypto_alt avg `-4.4649` n `228`; crypto_major avg `-4.9552` n `8`; equity avg `-3.4276` n `85`; fx avg `-0.1846` n `6`; index avg `-0.935` n `23`; metal avg `-0.978` n `20`; unknown avg `-0.3126` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
