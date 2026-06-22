# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T15:37:30.458646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.1494` n `228`; crypto_major avg `0.0769` n `8`; equity avg `0.0706` n `85`; fx avg `0.0034` n `6`; index avg `-0.016` n `23`; metal avg `-0.0195` n `20`; unknown avg `-0.0213` n `716`
- 1h: commodity avg `-0.1476` n `12`; crypto_alt avg `0.2328` n `228`; crypto_major avg `0.0893` n `8`; equity avg `-0.2697` n `85`; fx avg `-0.0234` n `6`; index avg `-0.065` n `23`; metal avg `-0.0384` n `20`; unknown avg `-0.0935` n `716`
- 4h: commodity avg `-0.3916` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.1556` n `8`; equity avg `-0.5867` n `85`; fx avg `-0.0397` n `6`; index avg `-0.0483` n `23`; metal avg `-0.207` n `20`; unknown avg `0.137` n `716`
- 24h: commodity avg `-0.8065` n `12`; crypto_alt avg `0.1609` n `228`; crypto_major avg `0.3787` n `8`; equity avg `-0.4781` n `85`; fx avg `-0.0262` n `6`; index avg `0.093` n `23`; metal avg `0.2609` n `18`; unknown avg `0.7709` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
