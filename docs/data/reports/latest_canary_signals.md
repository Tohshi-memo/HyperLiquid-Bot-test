# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T00:07:24.350183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `12`; crypto_alt avg `0.2459` n `228`; crypto_major avg `0.0951` n `8`; equity avg `-0.0196` n `74`; fx avg `0.0255` n `6`; index avg `0.0256` n `23`; metal avg `-0.0942` n `18`; unknown avg `-0.1277` n `550`
- 1h: commodity avg `-0.1335` n `12`; crypto_alt avg `0.9092` n `228`; crypto_major avg `0.5663` n `8`; equity avg `0.2477` n `74`; fx avg `0.0839` n `6`; index avg `0.2581` n `23`; metal avg `-0.1088` n `18`; unknown avg `-0.0215` n `550`
- 4h: commodity avg `0.5681` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `-0.1256` n `8`; equity avg `-0.5356` n `74`; fx avg `0.0059` n `6`; index avg `0.0636` n `23`; metal avg `-0.7597` n `18`; unknown avg `0.1604` n `550`
- 24h: commodity avg `1.7135` n `12`; crypto_alt avg `-2.0524` n `228`; crypto_major avg `-2.4084` n `8`; equity avg `-2.9392` n `74`; fx avg `0.0462` n `6`; index avg `-1.6981` n `23`; metal avg `-2.7827` n `18`; unknown avg `-0.4851` n `537`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
