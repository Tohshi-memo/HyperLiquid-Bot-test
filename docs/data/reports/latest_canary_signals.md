# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T01:22:25.877564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0616` n `12`; crypto_alt avg `0.0838` n `228`; crypto_major avg `0.1056` n `8`; equity avg `0.0249` n `86`; fx avg `-0.0167` n `6`; index avg `-0.0087` n `23`; metal avg `-0.0866` n `20`; unknown avg `-0.2581` n `716`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `0.6001` n `228`; crypto_major avg `0.4151` n `8`; equity avg `-0.0488` n `86`; fx avg `-0.0305` n `6`; index avg `0.0132` n `23`; metal avg `0.0144` n `20`; unknown avg `-0.0112` n `716`
- 4h: commodity avg `-0.036` n `12`; crypto_alt avg `-0.2422` n `228`; crypto_major avg `-0.1691` n `8`; equity avg `-0.8825` n `86`; fx avg `0.0133` n `6`; index avg `-0.1901` n `23`; metal avg `-0.2262` n `20`; unknown avg `-0.7594` n `716`
- 24h: commodity avg `-0.5636` n `12`; crypto_alt avg `-0.9009` n `228`; crypto_major avg `-0.6436` n `8`; equity avg `-1.0867` n `85`; fx avg `-0.0059` n `6`; index avg `-0.1624` n `23`; metal avg `-0.5842` n `18`; unknown avg `-0.0443` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
