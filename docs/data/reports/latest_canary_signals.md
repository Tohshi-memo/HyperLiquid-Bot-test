# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T14:22:33.667901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `-0.0417` n `228`; crypto_major avg `0.1763` n `8`; equity avg `0.0097` n `74`; fx avg `-0.0059` n `6`; index avg `0.0023` n `23`; metal avg `0.0581` n `18`; unknown avg `-0.0242` n `644`
- 1h: commodity avg `0.132` n `12`; crypto_alt avg `-0.1664` n `228`; crypto_major avg `0.0835` n `8`; equity avg `0.0012` n `74`; fx avg `-0.0161` n `6`; index avg `-0.0171` n `23`; metal avg `-0.0707` n `18`; unknown avg `-0.1034` n `644`
- 4h: commodity avg `-0.0836` n `12`; crypto_alt avg `0.4415` n `228`; crypto_major avg `0.9928` n `8`; equity avg `0.1496` n `74`; fx avg `-0.0156` n `6`; index avg `0.2605` n `23`; metal avg `0.1942` n `18`; unknown avg `0.1864` n `644`
- 24h: commodity avg `-1.2975` n `12`; crypto_alt avg `1.7465` n `228`; crypto_major avg `1.0193` n `8`; equity avg `0.0398` n `74`; fx avg `0.0233` n `6`; index avg `0.7169` n `23`; metal avg `1.2269` n `18`; unknown avg `0.3285` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
