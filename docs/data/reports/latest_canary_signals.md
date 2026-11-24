# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T08:07:46.345126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0204` n `13`; crypto_alt avg `-0.2052` n `239`; crypto_major avg `-0.3096` n `8`; equity avg `-0.249` n `166`; fx avg `-0.0` n `6`; index avg `-0.0375` n `27`; metal avg `-0.0705` n `20`; unknown avg `0.7312` n `1244`
- 1h: commodity avg `0.169` n `13`; crypto_alt avg `-0.5097` n `239`; crypto_major avg `-0.6348` n `8`; equity avg `-0.5877` n `166`; fx avg `0.0141` n `6`; index avg `-0.0907` n `27`; metal avg `-0.0383` n `20`; unknown avg `0.6552` n `1244`
- 4h: commodity avg `0.2104` n `13`; crypto_alt avg `0.5194` n `239`; crypto_major avg `-0.1435` n `8`; equity avg `-0.4293` n `166`; fx avg `0.0274` n `6`; index avg `-0.0711` n `27`; metal avg `-0.1142` n `20`; unknown avg `-0.2536` n `1206`
- 24h: commodity avg `-0.8091` n `13`; crypto_alt avg `-0.0395` n `239`; crypto_major avg `-0.6897` n `8`; equity avg `3.5087` n `166`; fx avg `-0.2427` n `6`; index avg `0.56` n `27`; metal avg `-0.1388` n `20`; unknown avg `1072.6984` n `1036`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
