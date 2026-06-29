# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T16:52:27.017871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.51` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `0.2535` n `228`; crypto_major avg `0.4899` n `8`; equity avg `0.1987` n `88`; fx avg `-0.003` n `6`; index avg `0.0158` n `23`; metal avg `0.036` n `20`; unknown avg `1.2091` n `765`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `0.1053` n `228`; crypto_major avg `0.2041` n `8`; equity avg `0.5776` n `88`; fx avg `0.0085` n `6`; index avg `0.0482` n `23`; metal avg `-0.1921` n `20`; unknown avg `1.0893` n `765`
- 4h: commodity avg `0.1513` n `12`; crypto_alt avg `0.1944` n `228`; crypto_major avg `0.5262` n `8`; equity avg `0.4381` n `88`; fx avg `0.0148` n `6`; index avg `0.0309` n `23`; metal avg `-0.3491` n `20`; unknown avg `0.5063` n `764`
- 24h: commodity avg `-0.6242` n `12`; crypto_alt avg `0.7097` n `228`; crypto_major avg `1.2143` n `8`; equity avg `0.8923` n `88`; fx avg `0.1163` n `6`; index avg `0.0933` n `23`; metal avg `-0.6629` n `20`; unknown avg `3.6382` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
