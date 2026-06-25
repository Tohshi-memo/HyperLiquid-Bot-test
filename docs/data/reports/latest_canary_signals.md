# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T06:37:33.477628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `12`; crypto_alt avg `-0.0265` n `228`; crypto_major avg `-0.0915` n `8`; equity avg `-0.0817` n `86`; fx avg `-0.0147` n `6`; index avg `-0.0225` n `23`; metal avg `-0.1186` n `20`; unknown avg `0.028` n `765`
- 1h: commodity avg `0.0304` n `12`; crypto_alt avg `-0.1911` n `228`; crypto_major avg `0.099` n `8`; equity avg `-0.0686` n `86`; fx avg `0.0138` n `6`; index avg `-0.0231` n `23`; metal avg `-0.2404` n `20`; unknown avg `1.151` n `749`
- 4h: commodity avg `0.0294` n `12`; crypto_alt avg `0.887` n `228`; crypto_major avg `1.0712` n `8`; equity avg `0.375` n `86`; fx avg `-0.0445` n `6`; index avg `0.0886` n `23`; metal avg `-0.1664` n `20`; unknown avg `-0.7147` n `748`
- 24h: commodity avg `-0.4427` n `12`; crypto_alt avg `-1.1361` n `228`; crypto_major avg `-1.0389` n `8`; equity avg `-0.198` n `86`; fx avg `-0.037` n `6`; index avg `0.5266` n `23`; metal avg `-2.0001` n `20`; unknown avg `-0.5121` n `708`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
