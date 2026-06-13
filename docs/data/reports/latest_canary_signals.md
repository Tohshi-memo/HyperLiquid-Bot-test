# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T15:07:29.996865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0959` n `12`; crypto_alt avg `0.2283` n `228`; crypto_major avg `0.0244` n `8`; equity avg `0.0267` n `74`; fx avg `0.0046` n `6`; index avg `-0.0064` n `23`; metal avg `0.1058` n `18`; unknown avg `0.0972` n `644`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `0.2654` n `228`; crypto_major avg `0.3225` n `8`; equity avg `0.1507` n `74`; fx avg `-0.0045` n `6`; index avg `0.0234` n `23`; metal avg `0.1265` n `18`; unknown avg `0.1112` n `644`
- 4h: commodity avg `-0.1256` n `12`; crypto_alt avg `0.7118` n `228`; crypto_major avg `1.0358` n `8`; equity avg `0.3076` n `74`; fx avg `-0.0128` n `6`; index avg `0.1743` n `23`; metal avg `0.1585` n `18`; unknown avg `0.3863` n `644`
- 24h: commodity avg `-0.7011` n `12`; crypto_alt avg `0.7937` n `228`; crypto_major avg `-0.4389` n `8`; equity avg `-0.3294` n `74`; fx avg `0.0281` n `6`; index avg `0.5065` n `23`; metal avg `0.8873` n `18`; unknown avg `0.2805` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
