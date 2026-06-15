# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T14:22:45.433706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.18` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8065` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8057` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `0.1147` n `228`; crypto_major avg `0.1851` n `8`; equity avg `-0.0348` n `74`; fx avg `-0.0156` n `6`; index avg `-0.1064` n `23`; metal avg `-0.3984` n `18`; unknown avg `-0.0059` n `690`
- 1h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.4267` n `228`; crypto_major avg `-0.6004` n `8`; equity avg `0.2636` n `74`; fx avg `-0.0007` n `6`; index avg `0.0094` n `23`; metal avg `-0.2756` n `18`; unknown avg `0.7841` n `689`
- 4h: commodity avg `0.229` n `12`; crypto_alt avg `1.809` n `228`; crypto_major avg `2.177` n `8`; equity avg `0.3705` n `74`; fx avg `-0.0182` n `6`; index avg `0.1745` n `23`; metal avg `0.3713` n `18`; unknown avg `0.4946` n `689`
- 24h: commodity avg `-1.4211` n `12`; crypto_alt avg `5.7596` n `228`; crypto_major avg `6.0426` n `8`; equity avg `2.147` n `74`; fx avg `0.0424` n `6`; index avg `1.0882` n `23`; metal avg `2.8173` n `18`; unknown avg `2.0002` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
