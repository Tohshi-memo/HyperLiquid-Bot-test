# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T07:37:30.243815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1379` n `12`; crypto_alt avg `0.0493` n `228`; crypto_major avg `0.0559` n `8`; equity avg `0.1592` n `74`; fx avg `-0.0048` n `6`; index avg `0.1043` n `23`; metal avg `0.0151` n `18`; unknown avg `-0.0952` n `557`
- 1h: commodity avg `-0.0617` n `12`; crypto_alt avg `0.3537` n `228`; crypto_major avg `0.3523` n `8`; equity avg `-0.1919` n `74`; fx avg `-0.0146` n `6`; index avg `-0.1532` n `23`; metal avg `-0.2546` n `18`; unknown avg `13.3906` n `557`
- 4h: commodity avg `-0.3827` n `12`; crypto_alt avg `-0.9234` n `228`; crypto_major avg `-1.02` n `8`; equity avg `-0.9909` n `74`; fx avg `-0.0099` n `6`; index avg `-0.4671` n `23`; metal avg `-0.867` n `18`; unknown avg `15.6399` n `535`
- 24h: commodity avg `-1.781` n `12`; crypto_alt avg `0.9366` n `228`; crypto_major avg `1.1` n `8`; equity avg `2.1412` n `74`; fx avg `-0.0404` n `6`; index avg `1.2413` n `23`; metal avg `1.8794` n `18`; unknown avg `1.5737` n `534`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
