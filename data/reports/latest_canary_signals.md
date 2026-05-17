# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T17:22:12.339507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.1019` n `228`; crypto_major avg `-0.1307` n `8`; equity avg `0.0491` n `65`; fx avg `0.0` n `5`; index avg `0.0094` n `23`; metal avg `-0.006` n `18`; unknown avg `0.0593` n `384`
- 1h: commodity avg `-0.0769` n `12`; crypto_alt avg `-0.5281` n `228`; crypto_major avg `-0.3124` n `8`; equity avg `-0.1109` n `65`; fx avg `0.0116` n `5`; index avg `-0.0623` n `23`; metal avg `-0.0203` n `18`; unknown avg `-0.0982` n `384`
- 4h: commodity avg `-0.0656` n `12`; crypto_alt avg `-0.3512` n `228`; crypto_major avg `-0.1823` n `8`; equity avg `-0.0884` n `65`; fx avg `0.0322` n `5`; index avg `-0.0015` n `23`; metal avg `-0.0282` n `18`; unknown avg `-0.108` n `383`
- 24h: commodity avg `1.7508` n `12`; crypto_alt avg `-9.6405` n `228`; crypto_major avg `-2.7023` n `8`; equity avg `-2.6504` n `65`; fx avg `-0.1543` n `5`; index avg `-1.6345` n `23`; metal avg `-5.8554` n `18`; unknown avg `549.9352` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
