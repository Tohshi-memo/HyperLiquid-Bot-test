# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T18:37:33.161563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `0.3167` n `228`; crypto_major avg `0.3035` n `8`; equity avg `0.1217` n `74`; fx avg `0.0006` n `6`; index avg `0.0989` n `23`; metal avg `-0.0271` n `18`; unknown avg `-0.0999` n `643`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.3508` n `228`; crypto_major avg `-0.225` n `8`; equity avg `-0.2327` n `74`; fx avg `0.0109` n `6`; index avg `-0.0495` n `23`; metal avg `0.2765` n `18`; unknown avg `-0.2021` n `643`
- 4h: commodity avg `-0.4924` n `12`; crypto_alt avg `-0.6883` n `228`; crypto_major avg `-0.2879` n `8`; equity avg `-0.1674` n `74`; fx avg `0.0075` n `6`; index avg `0.2842` n `23`; metal avg `1.1136` n `18`; unknown avg `-0.4909` n `643`
- 24h: commodity avg `-1.5406` n `12`; crypto_alt avg `0.1139` n `228`; crypto_major avg `1.0466` n `8`; equity avg `0.9257` n `74`; fx avg `0.0572` n `6`; index avg `1.1013` n `23`; metal avg `1.4965` n `18`; unknown avg `41.8274` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
