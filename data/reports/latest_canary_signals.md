# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T11:37:35.530885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `0.3561` n `228`; crypto_major avg `0.5122` n `8`; equity avg `0.2093` n `86`; fx avg `-0.0023` n `6`; index avg `0.0372` n `23`; metal avg `0.0751` n `20`; unknown avg `0.2554` n `764`
- 1h: commodity avg `-0.0523` n `12`; crypto_alt avg `-0.0538` n `228`; crypto_major avg `0.0372` n `8`; equity avg `-0.0563` n `86`; fx avg `0.002` n `6`; index avg `-0.0009` n `23`; metal avg `-0.2703` n `20`; unknown avg `0.1882` n `764`
- 4h: commodity avg `-0.0898` n `12`; crypto_alt avg `-0.3453` n `228`; crypto_major avg `-0.1688` n `8`; equity avg `0.0712` n `86`; fx avg `-0.0383` n `6`; index avg `0.0594` n `23`; metal avg `-0.6007` n `20`; unknown avg `-0.0893` n `764`
- 24h: commodity avg `-0.5412` n `12`; crypto_alt avg `-0.6461` n `228`; crypto_major avg `-0.3978` n `8`; equity avg `4.5247` n `86`; fx avg `-0.0206` n `6`; index avg `0.1366` n `23`; metal avg `-0.8696` n `20`; unknown avg `0.0072` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
