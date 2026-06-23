# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T05:07:31.265552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `12`; crypto_alt avg `-0.1102` n `228`; crypto_major avg `-0.0583` n `8`; equity avg `-0.1051` n `86`; fx avg `-0.0072` n `6`; index avg `-0.0261` n `23`; metal avg `-0.0482` n `20`; unknown avg `-0.4403` n `716`
- 1h: commodity avg `0.1069` n `12`; crypto_alt avg `-0.5736` n `228`; crypto_major avg `-0.6526` n `8`; equity avg `-0.6174` n `86`; fx avg `0.0018` n `6`; index avg `-0.1542` n `23`; metal avg `-0.1077` n `20`; unknown avg `1.4221` n `716`
- 4h: commodity avg `0.0772` n `12`; crypto_alt avg `-0.3351` n `228`; crypto_major avg `-0.6838` n `8`; equity avg `-1.8083` n `86`; fx avg `-0.0416` n `6`; index avg `-0.3981` n `23`; metal avg `-0.6874` n `20`; unknown avg `-0.0767` n `708`
- 24h: commodity avg `-0.4046` n `12`; crypto_alt avg `-1.1648` n `228`; crypto_major avg `-1.0871` n `8`; equity avg `-2.9416` n `85`; fx avg `-0.0449` n `6`; index avg `-0.4744` n `23`; metal avg `-0.8494` n `18`; unknown avg `1.118` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
