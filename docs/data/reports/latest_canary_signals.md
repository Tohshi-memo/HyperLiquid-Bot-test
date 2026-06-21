# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T15:07:26.415621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `0.2691` n `228`; crypto_major avg `0.2901` n `8`; equity avg `0.0557` n `78`; fx avg `0.0705` n `6`; index avg `0.0118` n `23`; metal avg `0.0113` n `18`; unknown avg `0.1384` n `702`
- 1h: commodity avg `0.0564` n `12`; crypto_alt avg `0.2391` n `228`; crypto_major avg `0.375` n `8`; equity avg `0.0307` n `78`; fx avg `0.0033` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0017` n `18`; unknown avg `0.0636` n `702`
- 4h: commodity avg `0.1986` n `12`; crypto_alt avg `0.2694` n `228`; crypto_major avg `0.1821` n `8`; equity avg `-0.0668` n `78`; fx avg `0.0392` n `6`; index avg `-0.0111` n `23`; metal avg `-0.0048` n `18`; unknown avg `0.1881` n `702`
- 24h: commodity avg `0.0797` n `12`; crypto_alt avg `1.7954` n `228`; crypto_major avg `0.2332` n `8`; equity avg `0.3511` n `78`; fx avg `0.0456` n `6`; index avg `0.0377` n `23`; metal avg `-0.0873` n `18`; unknown avg `0.6904` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
