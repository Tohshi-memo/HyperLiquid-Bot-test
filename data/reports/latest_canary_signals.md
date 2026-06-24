# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T12:07:34.149971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.1024` n `228`; crypto_major avg `-0.2657` n `8`; equity avg `-0.0861` n `86`; fx avg `0.0003` n `6`; index avg `0.0004` n `23`; metal avg `-0.2658` n `20`; unknown avg `-0.0166` n `764`
- 1h: commodity avg `-0.139` n `12`; crypto_alt avg `0.6829` n `228`; crypto_major avg `0.6947` n `8`; equity avg `0.1438` n `86`; fx avg `-0.0084` n `6`; index avg `0.0479` n `23`; metal avg `-0.3497` n `20`; unknown avg `0.2385` n `764`
- 4h: commodity avg `-0.1012` n `12`; crypto_alt avg `0.1874` n `228`; crypto_major avg `0.2193` n `8`; equity avg `-0.0841` n `86`; fx avg `-0.031` n `6`; index avg `0.0457` n `23`; metal avg `-0.8003` n `20`; unknown avg `-0.1145` n `764`
- 24h: commodity avg `-0.5553` n `12`; crypto_alt avg `-0.0774` n `228`; crypto_major avg `-0.0947` n `8`; equity avg `4.3102` n `86`; fx avg `-0.0221` n `6`; index avg `0.1201` n `23`; metal avg `-1.129` n `20`; unknown avg `-0.1685` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
