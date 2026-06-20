# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T06:37:28.145132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1387` n `228`; crypto_major avg `-0.0113` n `8`; equity avg `0.0023` n `78`; fx avg `-0.0009` n `6`; index avg `0.0098` n `23`; metal avg `0.0176` n `18`; unknown avg `-0.1227` n `687`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `0.1922` n `228`; crypto_major avg `0.3719` n `8`; equity avg `0.0813` n `78`; fx avg `0.2972` n `6`; index avg `-0.0017` n `23`; metal avg `-0.0079` n `18`; unknown avg `-0.3148` n `647`
- 4h: commodity avg `0.1053` n `12`; crypto_alt avg `0.7784` n `228`; crypto_major avg `1.4229` n `8`; equity avg `0.4155` n `78`; fx avg `-0.0198` n `6`; index avg `0.0343` n `23`; metal avg `0.0242` n `18`; unknown avg `0.3279` n `647`
- 24h: commodity avg `0.5061` n `12`; crypto_alt avg `-3.0575` n `228`; crypto_major avg `-3.2298` n `8`; equity avg `1.3786` n `78`; fx avg `-0.1064` n `6`; index avg `0.3304` n `23`; metal avg `-4.11` n `18`; unknown avg `-0.018` n `538`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
