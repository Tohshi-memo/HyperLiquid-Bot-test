# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T07:07:29.248952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1144` n `12`; crypto_alt avg `-0.0994` n `228`; crypto_major avg `-0.0476` n `8`; equity avg `-0.0464` n `74`; fx avg `-0.0029` n `6`; index avg `-0.031` n `23`; metal avg `-0.0296` n `18`; unknown avg `-0.0528` n `516`
- 1h: commodity avg `-0.1313` n `12`; crypto_alt avg `0.6814` n `228`; crypto_major avg `0.6785` n `8`; equity avg `0.2315` n `74`; fx avg `-0.0022` n `6`; index avg `-0.0163` n `23`; metal avg `0.0844` n `18`; unknown avg `5.8423` n `516`
- 4h: commodity avg `-0.1422` n `12`; crypto_alt avg `0.9226` n `228`; crypto_major avg `1.4368` n `8`; equity avg `0.7232` n `74`; fx avg `-0.0026` n `6`; index avg `0.1679` n `23`; metal avg `0.1791` n `18`; unknown avg `0.0653` n `506`
- 24h: commodity avg `0.3205` n `12`; crypto_alt avg `3.4934` n `228`; crypto_major avg `2.6099` n `8`; equity avg `2.2174` n `74`; fx avg `0.0563` n `6`; index avg `1.0865` n `23`; metal avg `0.6079` n `18`; unknown avg `0.7226` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
