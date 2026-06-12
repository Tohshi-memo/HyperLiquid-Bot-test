# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T08:52:31.820677+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0337` n `12`; crypto_alt avg `0.0578` n `228`; crypto_major avg `0.1073` n `8`; equity avg `0.0448` n `74`; fx avg `0.0004` n `6`; index avg `0.0297` n `23`; metal avg `-0.0712` n `18`; unknown avg `2.9529` n `643`
- 1h: commodity avg `-0.7718` n `12`; crypto_alt avg `0.7927` n `228`; crypto_major avg `1.0041` n `8`; equity avg `0.4952` n `74`; fx avg `-0.0093` n `6`; index avg `0.2323` n `23`; metal avg `0.8439` n `18`; unknown avg `2.0105` n `643`
- 4h: commodity avg `-1.0322` n `12`; crypto_alt avg `-0.3156` n `228`; crypto_major avg `-0.3599` n `8`; equity avg `-0.4501` n `74`; fx avg `-0.0383` n `6`; index avg `-0.2623` n `23`; metal avg `0.1703` n `18`; unknown avg `0.0115` n `515`
- 24h: commodity avg `-2.5642` n `12`; crypto_alt avg `1.3751` n `228`; crypto_major avg `1.5272` n `8`; equity avg `2.3839` n `74`; fx avg `-0.0133` n `6`; index avg `1.3637` n `23`; metal avg `2.9055` n `18`; unknown avg `2.1511` n `514`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
