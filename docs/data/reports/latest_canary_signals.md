# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T19:07:37.207253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `0.1316` n `230`; crypto_major avg `0.2003` n `8`; equity avg `0.2196` n `102`; fx avg `-0.0079` n `6`; index avg `0.0381` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.0171` n `775`
- 1h: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.0165` n `230`; crypto_major avg `0.1161` n `8`; equity avg `0.3028` n `102`; fx avg `0.0236` n `6`; index avg `0.0331` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0248` n `775`
- 4h: commodity avg `-0.4685` n `12`; crypto_alt avg `0.4005` n `230`; crypto_major avg `0.7822` n `8`; equity avg `1.102` n `102`; fx avg `-0.0026` n `6`; index avg `0.122` n `25`; metal avg `0.0673` n `20`; unknown avg `-0.215` n `774`
- 24h: commodity avg `-0.9499` n `12`; crypto_alt avg `-1.9848` n `230`; crypto_major avg `-1.7698` n `8`; equity avg `-3.2052` n `102`; fx avg `-0.0929` n `6`; index avg `-0.357` n `25`; metal avg `-0.4194` n `20`; unknown avg `-0.4553` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
