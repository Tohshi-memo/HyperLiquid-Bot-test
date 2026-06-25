# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T02:07:26.340918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0406` n `228`; crypto_major avg `-0.0287` n `8`; equity avg `-0.0912` n `86`; fx avg `-0.0023` n `6`; index avg `0.0116` n `23`; metal avg `-0.2072` n `20`; unknown avg `-0.1895` n `764`
- 1h: commodity avg `-0.1146` n `12`; crypto_alt avg `0.2298` n `228`; crypto_major avg `0.2692` n `8`; equity avg `0.1899` n `86`; fx avg `0.023` n `6`; index avg `0.1156` n `23`; metal avg `-0.298` n `20`; unknown avg `0.1821` n `764`
- 4h: commodity avg `-0.0792` n `12`; crypto_alt avg `-0.234` n `228`; crypto_major avg `0.0066` n `8`; equity avg `-0.2603` n `86`; fx avg `0.1361` n `6`; index avg `-0.0147` n `23`; metal avg `-0.4032` n `20`; unknown avg `-0.9336` n `748`
- 24h: commodity avg `-0.5851` n `12`; crypto_alt avg `-2.2433` n `228`; crypto_major avg `-2.043` n `8`; equity avg `-0.4168` n `86`; fx avg `0.0993` n `6`; index avg `0.4493` n `23`; metal avg `-1.8487` n `20`; unknown avg `-1.2785` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
