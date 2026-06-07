# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T06:52:23.332872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.0079` n `228`; crypto_major avg `0.1199` n `8`; equity avg `0.0123` n `74`; fx avg `0.0` n `6`; index avg `-0.0006` n `23`; metal avg `0.0302` n `18`; unknown avg `0.0281` n `516`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `0.5517` n `228`; crypto_major avg `0.596` n `8`; equity avg `0.2921` n `74`; fx avg `-0.0022` n `6`; index avg `0.0504` n `23`; metal avg `0.0852` n `18`; unknown avg `-0.1224` n `506`
- 4h: commodity avg `-0.0377` n `12`; crypto_alt avg `1.1706` n `228`; crypto_major avg `1.7113` n `8`; equity avg `0.8143` n `74`; fx avg `0.0003` n `6`; index avg `0.3438` n `23`; metal avg `0.3236` n `18`; unknown avg `0.1024` n `506`
- 24h: commodity avg `0.4911` n `12`; crypto_alt avg `3.713` n `228`; crypto_major avg `2.7287` n `8`; equity avg `2.1662` n `74`; fx avg `0.0551` n `6`; index avg `1.0214` n `23`; metal avg `0.6619` n `18`; unknown avg `0.7846` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
