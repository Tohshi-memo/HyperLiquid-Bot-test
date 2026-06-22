# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T16:07:40.575239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `12`; crypto_alt avg `-0.2642` n `228`; crypto_major avg `-0.3259` n `8`; equity avg `-0.1958` n `85`; fx avg `0.0084` n `6`; index avg `-0.0163` n `23`; metal avg `-0.0012` n `20`; unknown avg `-0.0043` n `717`
- 1h: commodity avg `-0.0712` n `12`; crypto_alt avg `-0.6097` n `228`; crypto_major avg `-0.7077` n `8`; equity avg `-0.3094` n `85`; fx avg `0.025` n `6`; index avg `-0.0423` n `23`; metal avg `-0.2377` n `20`; unknown avg `0.0886` n `716`
- 4h: commodity avg `-0.3239` n `12`; crypto_alt avg `-0.9311` n `228`; crypto_major avg `-0.8998` n `8`; equity avg `-0.761` n `85`; fx avg `-0.0385` n `6`; index avg `-0.0482` n `23`; metal avg `-0.4151` n `20`; unknown avg `0.2341` n `716`
- 24h: commodity avg `-0.7377` n `12`; crypto_alt avg `-0.6907` n `228`; crypto_major avg `-0.3423` n `8`; equity avg `-0.6285` n `85`; fx avg `-0.0255` n `6`; index avg `0.0894` n `23`; metal avg `0.0973` n `18`; unknown avg `0.7291` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
