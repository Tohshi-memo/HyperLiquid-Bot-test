# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T22:22:43.204690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.1974` n `228`; crypto_major avg `0.1477` n `8`; equity avg `0.0312` n `74`; fx avg `0.0307` n `6`; index avg `0.029` n `23`; metal avg `-0.0318` n `18`; unknown avg `0.0114` n `643`
- 1h: commodity avg `-0.0574` n `12`; crypto_alt avg `-0.1191` n `228`; crypto_major avg `-0.2401` n `8`; equity avg `0.0923` n `74`; fx avg `0.0198` n `6`; index avg `0.1475` n `23`; metal avg `-0.0269` n `18`; unknown avg `0.1656` n `643`
- 4h: commodity avg `-0.16` n `12`; crypto_alt avg `0.15` n `228`; crypto_major avg `-0.3925` n `8`; equity avg `0.0084` n `74`; fx avg `-0.0258` n `6`; index avg `0.2401` n `23`; metal avg `-0.1745` n `18`; unknown avg `0.2473` n `643`
- 24h: commodity avg `-0.3711` n `12`; crypto_alt avg `-0.3332` n `228`; crypto_major avg `0.1077` n `8`; equity avg `-0.486` n `74`; fx avg `0.0005` n `6`; index avg `0.3553` n `23`; metal avg `0.4249` n `18`; unknown avg `41.2553` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
