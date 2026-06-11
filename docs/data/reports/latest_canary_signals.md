# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T03:22:37.751293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `-0.0223` n `228`; crypto_major avg `-0.112` n `8`; equity avg `-0.1219` n `74`; fx avg `-0.0118` n `6`; index avg `-0.108` n `23`; metal avg `-0.2027` n `18`; unknown avg `1.17` n `550`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.059` n `228`; crypto_major avg `0.0749` n `8`; equity avg `0.0685` n `74`; fx avg `-0.0443` n `6`; index avg `-0.0147` n `23`; metal avg `-0.5224` n `18`; unknown avg `1.1575` n `550`
- 4h: commodity avg `-0.2439` n `12`; crypto_alt avg `1.3953` n `228`; crypto_major avg `1.0703` n `8`; equity avg `1.0775` n `74`; fx avg `0.1279` n `6`; index avg `0.4379` n `23`; metal avg `0.7379` n `18`; unknown avg `0.3303` n `550`
- 24h: commodity avg `1.3725` n `12`; crypto_alt avg `-0.4534` n `228`; crypto_major avg `-0.4494` n `8`; equity avg `-1.4027` n `74`; fx avg `0.0238` n `6`; index avg `-1.1666` n `23`; metal avg `-0.9273` n `18`; unknown avg `0.1073` n `537`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
