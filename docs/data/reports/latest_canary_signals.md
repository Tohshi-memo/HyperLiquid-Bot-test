# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T05:07:30.065893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.3321` n `228`; crypto_major avg `-0.3283` n `8`; equity avg `-0.0564` n `74`; fx avg `0.0198` n `6`; index avg `-0.0303` n `23`; metal avg `-0.0153` n `18`; unknown avg `0.3957` n `643`
- 1h: commodity avg `0.0309` n `12`; crypto_alt avg `-0.0076` n `228`; crypto_major avg `-0.2084` n `8`; equity avg `-0.0877` n `74`; fx avg `0.0203` n `6`; index avg `-0.0535` n `23`; metal avg `-0.011` n `18`; unknown avg `-0.0237` n `635`
- 4h: commodity avg `-0.0462` n `12`; crypto_alt avg `-0.2245` n `228`; crypto_major avg `-0.628` n `8`; equity avg `-0.2474` n `74`; fx avg `0.0529` n `6`; index avg `0.0942` n `23`; metal avg `-0.0999` n `18`; unknown avg `-0.0998` n `635`
- 24h: commodity avg `-0.6408` n `12`; crypto_alt avg `-0.1827` n `228`; crypto_major avg `-0.6809` n `8`; equity avg `-0.9346` n `74`; fx avg `0.0128` n `6`; index avg `0.508` n `23`; metal avg `0.4753` n `18`; unknown avg `40.58` n `507`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
