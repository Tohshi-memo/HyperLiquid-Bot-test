# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T02:07:30.270036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.447` n `228`; crypto_major avg `0.3161` n `8`; equity avg `-0.3129` n `86`; fx avg `-0.008` n `6`; index avg `-0.0629` n `23`; metal avg `-0.0691` n `20`; unknown avg `-0.2175` n `716`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.0542` n `228`; crypto_major avg `-0.1916` n `8`; equity avg `-0.981` n `86`; fx avg `-0.0277` n `6`; index avg `-0.2147` n `23`; metal avg `-0.4074` n `20`; unknown avg `-0.2727` n `716`
- 4h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.3056` n `228`; crypto_major avg `-0.44` n `8`; equity avg `-1.868` n `86`; fx avg `0.0083` n `6`; index avg `-0.3987` n `23`; metal avg `-0.5513` n `20`; unknown avg `-0.7008` n `716`
- 24h: commodity avg `-0.5119` n `12`; crypto_alt avg `-1.3224` n `228`; crypto_major avg `-1.2536` n `8`; equity avg `-2.2998` n `85`; fx avg `-0.0452` n `6`; index avg `-0.3636` n `23`; metal avg `-0.6756` n `18`; unknown avg `0.074` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
