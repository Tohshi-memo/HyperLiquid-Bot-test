# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T21:52:29.484645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `-0.141` n `228`; crypto_major avg `-0.1145` n `8`; equity avg `-0.0139` n `85`; fx avg `-0.0018` n `6`; index avg `0.0007` n `23`; metal avg `-0.0046` n `20`; unknown avg `-0.0147` n `717`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `-0.2702` n `228`; crypto_major avg `-0.2066` n `8`; equity avg `0.0194` n `85`; fx avg `-0.0465` n `6`; index avg `0.0116` n `23`; metal avg `0.0107` n `20`; unknown avg `-0.2905` n `717`
- 4h: commodity avg `0.0384` n `12`; crypto_alt avg `-0.8326` n `228`; crypto_major avg `-0.6253` n `8`; equity avg `-0.2049` n `85`; fx avg `-0.021` n `6`; index avg `-0.039` n `23`; metal avg `0.1143` n `20`; unknown avg `-0.3574` n `709`
- 24h: commodity avg `-1.1051` n `12`; crypto_alt avg `-0.1822` n `228`; crypto_major avg `-0.0396` n `8`; equity avg `-0.5741` n `85`; fx avg `0.0639` n `6`; index avg `0.1351` n `23`; metal avg `0.4002` n `18`; unknown avg `0.4171` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
