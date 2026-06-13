# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T11:07:31.066019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0713` n `12`; crypto_alt avg `0.1035` n `228`; crypto_major avg `-0.0437` n `8`; equity avg `-0.0071` n `74`; fx avg `0.0006` n `6`; index avg `0.1157` n `23`; metal avg `0.0001` n `18`; unknown avg `0.1358` n `644`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0939` n `228`; crypto_major avg `0.0147` n `8`; equity avg `-0.0102` n `74`; fx avg `0.0015` n `6`; index avg `0.0517` n `23`; metal avg `0.1042` n `18`; unknown avg `13.3493` n `644`
- 4h: commodity avg `-0.191` n `12`; crypto_alt avg `0.8122` n `228`; crypto_major avg `0.3932` n `8`; equity avg `0.0968` n `74`; fx avg `0.0009` n `6`; index avg `0.0695` n `23`; metal avg `0.1271` n `18`; unknown avg `0.7184` n `635`
- 24h: commodity avg `-0.001` n `12`; crypto_alt avg `0.6647` n `228`; crypto_major avg `-0.0597` n `8`; equity avg `-0.6726` n `74`; fx avg `0.0128` n `6`; index avg `0.7023` n `23`; metal avg `0.5023` n `18`; unknown avg `30.5673` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
