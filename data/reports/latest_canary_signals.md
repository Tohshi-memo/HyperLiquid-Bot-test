# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T20:37:31.477605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `12`; crypto_alt avg `0.0296` n `228`; crypto_major avg `-0.0196` n `8`; equity avg `0.0809` n `86`; fx avg `0.0025` n `6`; index avg `0.006` n `23`; metal avg `0.0118` n `20`; unknown avg `0.0794` n `764`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.4691` n `228`; crypto_major avg `0.3323` n `8`; equity avg `0.1604` n `86`; fx avg `0.0115` n `6`; index avg `0.0269` n `23`; metal avg `-0.0761` n `20`; unknown avg `0.3461` n `764`
- 4h: commodity avg `0.0975` n `12`; crypto_alt avg `0.2939` n `228`; crypto_major avg `0.0043` n `8`; equity avg `-0.608` n `86`; fx avg `0.0111` n `6`; index avg `-0.1088` n `23`; metal avg `-0.2765` n `20`; unknown avg `-0.0555` n `756`
- 24h: commodity avg `-0.3579` n `12`; crypto_alt avg `-2.7822` n `228`; crypto_major avg `-3.7176` n `8`; equity avg `-3.2269` n `86`; fx avg `-0.1806` n `6`; index avg `-0.9311` n `23`; metal avg `-1.2065` n `20`; unknown avg `0.3834` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
