# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T23:22:26.881360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1582` n `12`; crypto_alt avg `0.3571` n `228`; crypto_major avg `0.3692` n `8`; equity avg `-0.0856` n `74`; fx avg `0.0056` n `6`; index avg `0.012` n `23`; metal avg `-0.1789` n `18`; unknown avg `0.095` n `550`
- 1h: commodity avg `0.1005` n `12`; crypto_alt avg `0.9626` n `228`; crypto_major avg `0.6725` n `8`; equity avg `-0.3745` n `74`; fx avg `0.0095` n `6`; index avg `-0.0396` n `23`; metal avg `-0.0556` n `18`; unknown avg `0.1435` n `550`
- 4h: commodity avg `0.6767` n `12`; crypto_alt avg `-0.8909` n `228`; crypto_major avg `-0.3949` n `8`; equity avg `-1.2389` n `74`; fx avg `-0.0891` n `6`; index avg `-0.4007` n `23`; metal avg `-1.2316` n `18`; unknown avg `-0.0546` n `550`
- 24h: commodity avg `1.5702` n `12`; crypto_alt avg `-2.3661` n `228`; crypto_major avg `-2.3967` n `8`; equity avg `-2.6248` n `74`; fx avg `-0.1052` n `6`; index avg `-1.7525` n `23`; metal avg `-2.8755` n `18`; unknown avg `-0.4074` n `537`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
