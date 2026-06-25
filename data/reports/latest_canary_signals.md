# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T05:07:33.591203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.7817` n `228`; crypto_major avg `0.8064` n `8`; equity avg `0.1318` n `86`; fx avg `0.0005` n `6`; index avg `0.0105` n `23`; metal avg `-0.0009` n `20`; unknown avg `4.5299` n `765`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `1.1176` n `228`; crypto_major avg `1.2903` n `8`; equity avg `0.3036` n `86`; fx avg `-0.0273` n `6`; index avg `0.0298` n `23`; metal avg `0.0059` n `20`; unknown avg `4.3626` n `765`
- 4h: commodity avg `-0.0796` n `12`; crypto_alt avg `1.1483` n `228`; crypto_major avg `1.3221` n `8`; equity avg `0.4886` n `86`; fx avg `0.0097` n `6`; index avg `0.1684` n `23`; metal avg `0.0307` n `20`; unknown avg `0.5861` n `748`
- 24h: commodity avg `-0.4911` n `12`; crypto_alt avg `-0.8313` n `228`; crypto_major avg `-0.6315` n `8`; equity avg `0.2692` n `86`; fx avg `0.0328` n `6`; index avg `0.5885` n `23`; metal avg `-1.3136` n `20`; unknown avg `-0.3609` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
