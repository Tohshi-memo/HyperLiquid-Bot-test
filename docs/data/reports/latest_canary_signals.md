# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T15:22:15.082030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.1201` n `228`; crypto_major avg `-0.1178` n `8`; equity avg `0.1128` n `65`; fx avg `-0.0009` n `5`; index avg `0.0181` n `23`; metal avg `0.0199` n `18`; unknown avg `-0.0486` n `384`
- 1h: commodity avg `0.1989` n `12`; crypto_alt avg `0.3256` n `228`; crypto_major avg `0.2802` n `8`; equity avg `0.0977` n `65`; fx avg `0.0207` n `5`; index avg `0.017` n `23`; metal avg `-0.0019` n `18`; unknown avg `0.0025` n `383`
- 4h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.382` n `228`; crypto_major avg `-0.1854` n `8`; equity avg `0.0199` n `65`; fx avg `0.0012` n `5`; index avg `0.0493` n `23`; metal avg `0.0255` n `18`; unknown avg `-0.0833` n `383`
- 24h: commodity avg `1.7634` n `12`; crypto_alt avg `-9.3101` n `228`; crypto_major avg `-2.4485` n `8`; equity avg `-2.6091` n `65`; fx avg `-0.1657` n `5`; index avg `-1.6168` n `23`; metal avg `-5.8354` n `18`; unknown avg `550.0094` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
