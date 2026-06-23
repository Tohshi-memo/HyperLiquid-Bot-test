# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T23:44:15.125033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `-0.1232` n `228`; crypto_major avg `-0.0505` n `8`; equity avg `-0.0337` n `86`; fx avg `0.0041` n `6`; index avg `-0.0094` n `23`; metal avg `-0.1894` n `20`; unknown avg `0.1502` n `764`
- 1h: commodity avg `-0.0775` n `12`; crypto_alt avg `-0.2721` n `228`; crypto_major avg `-0.0163` n `8`; equity avg `-0.1234` n `86`; fx avg `0.0059` n `6`; index avg `-0.0015` n `23`; metal avg `-0.2276` n `20`; unknown avg `0.4546` n `756`
- 4h: commodity avg `-0.1351` n `12`; crypto_alt avg `0.1765` n `228`; crypto_major avg `0.3588` n `8`; equity avg `-0.1328` n `86`; fx avg `-0.0102` n `6`; index avg `0.0548` n `23`; metal avg `-0.3679` n `20`; unknown avg `0.2378` n `756`
- 24h: commodity avg `-0.4964` n `12`; crypto_alt avg `-2.1442` n `228`; crypto_major avg `-3.0931` n `8`; equity avg `-3.2729` n `86`; fx avg `-0.2188` n `6`; index avg `-0.8758` n `23`; metal avg `-1.5089` n `20`; unknown avg `0.725` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
