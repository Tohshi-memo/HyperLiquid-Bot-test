# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T14:07:13.533450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2639` n `12`; crypto_alt avg `-0.2861` n `228`; crypto_major avg `-0.1686` n `8`; equity avg `0.0794` n `65`; fx avg `0.0` n `5`; index avg `0.0417` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.0291` n `383`
- 1h: commodity avg `-0.2803` n `12`; crypto_alt avg `-0.3269` n `228`; crypto_major avg `-0.3883` n `8`; equity avg `-0.0202` n `65`; fx avg `0.0` n `5`; index avg `0.0907` n `23`; metal avg `0.015` n `18`; unknown avg `-0.0718` n `383`
- 4h: commodity avg `-0.2396` n `12`; crypto_alt avg `-0.8788` n `228`; crypto_major avg `-0.3529` n `8`; equity avg `0.1871` n `65`; fx avg `-0.0108` n `5`; index avg `0.1793` n `23`; metal avg `0.0225` n `18`; unknown avg `-0.2961` n `383`
- 24h: commodity avg `1.5368` n `12`; crypto_alt avg `-9.3864` n `228`; crypto_major avg `-2.5787` n `8`; equity avg `-2.5449` n `65`; fx avg `-0.1861` n `5`; index avg `-1.5597` n `23`; metal avg `-5.8253` n `18`; unknown avg `549.9608` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
