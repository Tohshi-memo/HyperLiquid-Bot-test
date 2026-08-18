# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T19:36:15.036163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `0.0607` n `8`; equity avg `0.1304` n `120`; fx avg `0.0033` n `6`; index avg `0.0083` n `25`; metal avg `-0.0153` n `20`; unknown avg `-0.0778` n `789`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.0823` n `230`; crypto_major avg `0.0408` n `8`; equity avg `-0.042` n `120`; fx avg `-0.0023` n `6`; index avg `-0.005` n `25`; metal avg `-0.0232` n `20`; unknown avg `-0.0002` n `789`
- 4h: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.2214` n `230`; crypto_major avg `-0.0834` n `8`; equity avg `-0.1437` n `120`; fx avg `0.0052` n `6`; index avg `0.0056` n `25`; metal avg `-0.0215` n `20`; unknown avg `0.1346` n `789`
- 24h: commodity avg `0.2908` n `12`; crypto_alt avg `-0.5454` n `230`; crypto_major avg `0.3667` n `8`; equity avg `-4.3727` n `120`; fx avg `-0.0354` n `6`; index avg `-0.6677` n `25`; metal avg `-0.6794` n `20`; unknown avg `-0.2934` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
