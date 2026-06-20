# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T06:52:30.259327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.0955` n `228`; crypto_major avg `0.0191` n `8`; equity avg `0.034` n `78`; fx avg `0.0068` n `6`; index avg `-0.0046` n `23`; metal avg `0.0049` n `18`; unknown avg `-0.0344` n `679`
- 1h: commodity avg `0.0419` n `12`; crypto_alt avg `0.3323` n `228`; crypto_major avg `0.4331` n `8`; equity avg `0.0804` n `78`; fx avg `0.0084` n `6`; index avg `-0.0184` n `23`; metal avg `0.0108` n `18`; unknown avg `0.0497` n `639`
- 4h: commodity avg `0.1002` n `12`; crypto_alt avg `0.9868` n `228`; crypto_major avg `1.4873` n `8`; equity avg `0.4412` n `78`; fx avg `-0.0161` n `6`; index avg `0.0172` n `23`; metal avg `0.0253` n `18`; unknown avg `0.0876` n `639`
- 24h: commodity avg `0.5245` n `12`; crypto_alt avg `-2.9633` n `228`; crypto_major avg `-3.2117` n `8`; equity avg `1.4165` n `78`; fx avg `-0.0995` n `6`; index avg `0.3277` n `23`; metal avg `-4.1053` n `18`; unknown avg `-0.2771` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
