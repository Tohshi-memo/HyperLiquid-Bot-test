# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T03:22:29.526475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1582` n `12`; crypto_alt avg `-0.4138` n `228`; crypto_major avg `-0.3378` n `8`; equity avg `-0.1316` n `74`; fx avg `-0.0023` n `6`; index avg `-0.0175` n `23`; metal avg `0.002` n `18`; unknown avg `0.4912` n `643`
- 1h: commodity avg `-0.1338` n `12`; crypto_alt avg `-0.3764` n `228`; crypto_major avg `-0.5068` n `8`; equity avg `-0.1672` n `74`; fx avg `0.0052` n `6`; index avg `-0.0386` n `23`; metal avg `-0.0378` n `18`; unknown avg `0.6721` n `643`
- 4h: commodity avg `-0.1066` n `12`; crypto_alt avg `0.7435` n `228`; crypto_major avg `0.0063` n `8`; equity avg `0.0111` n `74`; fx avg `0.032` n `6`; index avg `0.2209` n `23`; metal avg `0.037` n `18`; unknown avg `-0.4198` n `643`
- 24h: commodity avg `-1.1678` n `12`; crypto_alt avg `-0.0035` n `228`; crypto_major avg `-0.257` n `8`; equity avg `-0.6008` n `74`; fx avg `0.0139` n `6`; index avg `0.7806` n `23`; metal avg `0.2258` n `18`; unknown avg `39.846` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
