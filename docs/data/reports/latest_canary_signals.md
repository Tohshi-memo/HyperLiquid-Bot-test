# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T07:37:26.476723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `0.0447` n `228`; crypto_major avg `0.0218` n `8`; equity avg `-0.0125` n `78`; fx avg `-0.2916` n `6`; index avg `0.0142` n `23`; metal avg `0.0005` n `18`; unknown avg `0.0159` n `687`
- 1h: commodity avg `0.0348` n `12`; crypto_alt avg `-0.0351` n `228`; crypto_major avg `-0.0767` n `8`; equity avg `-0.0745` n `78`; fx avg `-0.2842` n `6`; index avg `-0.0408` n `23`; metal avg `0.0287` n `18`; unknown avg `0.027` n `679`
- 4h: commodity avg `0.0829` n `12`; crypto_alt avg `0.6883` n `228`; crypto_major avg `1.2261` n `8`; equity avg `0.3021` n `78`; fx avg `-0.3147` n `6`; index avg `-0.0095` n `23`; metal avg `0.0851` n `18`; unknown avg `0.1413` n `639`
- 24h: commodity avg `0.5416` n `12`; crypto_alt avg `-3.0875` n `228`; crypto_major avg `-3.3046` n `8`; equity avg `1.2969` n `78`; fx avg `-0.3875` n `6`; index avg `0.2893` n `23`; metal avg `-4.0833` n `18`; unknown avg `0.187` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
