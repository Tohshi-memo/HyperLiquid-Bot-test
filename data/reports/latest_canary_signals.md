# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T00:37:32.524207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `0.1153` n `228`; crypto_major avg `0.081` n `8`; equity avg `-0.1184` n `86`; fx avg `0.0079` n `6`; index avg `-0.0187` n `23`; metal avg `0.0952` n `20`; unknown avg `0.5761` n `716`
- 1h: commodity avg `-0.0175` n `12`; crypto_alt avg `0.015` n `228`; crypto_major avg `-0.0962` n `8`; equity avg `-0.6729` n `86`; fx avg `0.0069` n `6`; index avg `-0.1955` n `23`; metal avg `-0.1449` n `20`; unknown avg `-0.0558` n `716`
- 4h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.9277` n `228`; crypto_major avg `-0.7163` n `8`; equity avg `-0.9383` n `86`; fx avg `0.0235` n `6`; index avg `-0.2291` n `23`; metal avg `-0.1251` n `20`; unknown avg `-0.4064` n `716`
- 24h: commodity avg `-0.8349` n `12`; crypto_alt avg `-1.0048` n `228`; crypto_major avg `-0.6337` n `8`; equity avg `-0.8356` n `85`; fx avg `0.1046` n `6`; index avg `-0.079` n `23`; metal avg `-0.0207` n `18`; unknown avg `0.1109` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
