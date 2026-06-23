# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T05:37:25.814535+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0324` n `12`; crypto_alt avg `-0.2325` n `228`; crypto_major avg `-0.3017` n `8`; equity avg `-0.321` n `86`; fx avg `-0.0008` n `6`; index avg `-0.0702` n `23`; metal avg `0.0566` n `20`; unknown avg `0.2232` n `716`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.7163` n `228`; crypto_major avg `-0.6768` n `8`; equity avg `-0.8148` n `86`; fx avg `-0.0014` n `6`; index avg `-0.1967` n `23`; metal avg `-0.0434` n `20`; unknown avg `1.5817` n `716`
- 4h: commodity avg `-0.0965` n `12`; crypto_alt avg `-0.4565` n `228`; crypto_major avg `-0.7673` n `8`; equity avg `-1.9751` n `86`; fx avg `-0.0385` n `6`; index avg `-0.4205` n `23`; metal avg `-0.4478` n `20`; unknown avg `-0.3842` n `708`
- 24h: commodity avg `-0.4899` n `12`; crypto_alt avg `-1.5238` n `228`; crypto_major avg `-1.5182` n `8`; equity avg `-3.3947` n `85`; fx avg `-0.0482` n `6`; index avg `-0.6016` n `23`; metal avg `-1.0704` n `18`; unknown avg `1.0715` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
