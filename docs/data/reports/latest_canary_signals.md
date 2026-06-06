# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T21:00:10.429587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.0531` n `228`; crypto_major avg `0.1163` n `8`; equity avg `-0.0321` n `74`; fx avg `-0.0011` n `6`; index avg `0.0019` n `23`; metal avg `0.0097` n `18`; unknown avg `0.0603` n `515`
- 1h: commodity avg `0.0509` n `12`; crypto_alt avg `0.3576` n `228`; crypto_major avg `0.4882` n `8`; equity avg `0.0642` n `74`; fx avg `-0.0018` n `6`; index avg `0.0985` n `23`; metal avg `-0.001` n `18`; unknown avg `-0.0501` n `515`
- 4h: commodity avg `0.1311` n `12`; crypto_alt avg `-0.3533` n `228`; crypto_major avg `-0.3884` n `8`; equity avg `0.1337` n `74`; fx avg `0.0239` n `6`; index avg `-0.0473` n `23`; metal avg `0.0321` n `18`; unknown avg `0.3615` n `515`
- 24h: commodity avg `0.2628` n `12`; crypto_alt avg `-2.7732` n `228`; crypto_major avg `-2.4413` n `8`; equity avg `-0.6796` n `74`; fx avg `0.0696` n `6`; index avg `0.3016` n `23`; metal avg `-0.5258` n `18`; unknown avg `0.4196` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
