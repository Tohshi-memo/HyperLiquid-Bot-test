# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T18:17:14.470991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `12`; crypto_alt avg `-0.1271` n `228`; crypto_major avg `-0.064` n `8`; equity avg `-0.0996` n `74`; fx avg `-0.0359` n `6`; index avg `-0.0544` n `23`; metal avg `-0.0149` n `18`; unknown avg `0.0869` n `516`
- 1h: commodity avg `0.0756` n `12`; crypto_alt avg `-0.288` n `228`; crypto_major avg `-0.0917` n `8`; equity avg `-0.2688` n `74`; fx avg `-0.036` n `6`; index avg `-0.1275` n `23`; metal avg `-0.0559` n `18`; unknown avg `0.0999` n `516`
- 4h: commodity avg `0.2834` n `12`; crypto_alt avg `0.0639` n `228`; crypto_major avg `0.5629` n `8`; equity avg `-0.1175` n `74`; fx avg `-0.0377` n `6`; index avg `-0.164` n `23`; metal avg `0.0324` n `18`; unknown avg `-2.2078` n `516`
- 24h: commodity avg `0.2804` n `12`; crypto_alt avg `3.2303` n `228`; crypto_major avg `3.9103` n `8`; equity avg `1.8857` n `74`; fx avg `-0.2415` n `6`; index avg `0.3391` n `23`; metal avg `0.6321` n `18`; unknown avg `-4.7053` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
