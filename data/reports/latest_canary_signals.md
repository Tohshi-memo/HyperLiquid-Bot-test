# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T22:37:16.705811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0997` n `12`; crypto_alt avg `-0.0351` n `228`; crypto_major avg `0.007` n `8`; equity avg `-0.0491` n `67`; fx avg `-0.0082` n `6`; index avg `-0.0326` n `23`; metal avg `-0.0548` n `18`; unknown avg `0.0984` n `419`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `-0.9918` n `228`; crypto_major avg `-0.4746` n `8`; equity avg `-0.1464` n `67`; fx avg `-0.0217` n `6`; index avg `-0.0757` n `23`; metal avg `0.1092` n `18`; unknown avg `0.8885` n `419`
- 4h: commodity avg `0.2151` n `12`; crypto_alt avg `-0.9422` n `228`; crypto_major avg `-0.395` n `8`; equity avg `-0.0406` n `67`; fx avg `-0.004` n `6`; index avg `0.0281` n `23`; metal avg `0.1406` n `18`; unknown avg `-0.0977` n `418`
- 24h: commodity avg `-1.1075` n `12`; crypto_alt avg `-1.7165` n `228`; crypto_major avg `-0.7866` n `8`; equity avg `-0.3275` n `67`; fx avg `-0.1111` n `6`; index avg `-0.462` n `23`; metal avg `-1.2032` n `18`; unknown avg `-0.2394` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
