# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T22:22:28.268382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.2403` n `228`; crypto_major avg `-0.2391` n `8`; equity avg `-0.0982` n `74`; fx avg `0.0512` n `6`; index avg `-0.1603` n `23`; metal avg `-0.0204` n `18`; unknown avg `0.025` n `517`
- 1h: commodity avg `-0.1216` n `12`; crypto_alt avg `-0.6462` n `228`; crypto_major avg `-0.7197` n `8`; equity avg `-0.2297` n `74`; fx avg `-0.0059` n `6`; index avg `-0.1391` n `23`; metal avg `-0.1763` n `18`; unknown avg `-0.1551` n `517`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `-0.8082` n `228`; crypto_major avg `-0.3395` n `8`; equity avg `-0.6084` n `74`; fx avg `-0.0261` n `6`; index avg `-0.2798` n `23`; metal avg `-0.371` n `18`; unknown avg `-0.2399` n `517`
- 24h: commodity avg `-0.7054` n `12`; crypto_alt avg `0.7055` n `228`; crypto_major avg `1.5514` n `8`; equity avg `1.9249` n `74`; fx avg `-0.2755` n `6`; index avg `0.8747` n `23`; metal avg `0.1024` n `18`; unknown avg `-2.3071` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
