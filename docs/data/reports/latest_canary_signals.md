# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T08:07:30.793390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `-0.1342` n `228`; crypto_major avg `-0.1552` n `8`; equity avg `0.0126` n `78`; fx avg `0.0246` n `6`; index avg `-0.0052` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.0402` n `687`
- 1h: commodity avg `0.007` n `12`; crypto_alt avg `-0.0785` n `228`; crypto_major avg `-0.0098` n `8`; equity avg `0.0293` n `78`; fx avg `0.0217` n `6`; index avg `-0.038` n `23`; metal avg `0.0136` n `18`; unknown avg `0.111` n `687`
- 4h: commodity avg `0.0834` n `12`; crypto_alt avg `0.3601` n `228`; crypto_major avg `0.9363` n `8`; equity avg `0.2438` n `78`; fx avg `0.0055` n `6`; index avg `-0.0198` n `23`; metal avg `0.0688` n `18`; unknown avg `0.0063` n `639`
- 24h: commodity avg `0.5198` n `12`; crypto_alt avg `-3.3511` n `228`; crypto_major avg `-3.5673` n `8`; equity avg `1.3203` n `78`; fx avg `-0.0892` n `6`; index avg `0.2697` n `23`; metal avg `-4.0737` n `18`; unknown avg `0.0404` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
