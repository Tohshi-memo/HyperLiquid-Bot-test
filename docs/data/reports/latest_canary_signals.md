# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T09:37:17.696712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0641` n `12`; crypto_alt avg `0.0418` n `228`; crypto_major avg `0.125` n `8`; equity avg `0.0306` n `67`; fx avg `-0.0089` n `6`; index avg `-0.0081` n `23`; metal avg `0.0846` n `18`; unknown avg `0.0258` n `397`
- 1h: commodity avg `-0.2714` n `12`; crypto_alt avg `0.0614` n `228`; crypto_major avg `0.0576` n `8`; equity avg `0.1159` n `67`; fx avg `-0.0018` n `6`; index avg `0.0351` n `23`; metal avg `0.042` n `18`; unknown avg `0.0538` n `397`
- 4h: commodity avg `0.2427` n `12`; crypto_alt avg `0.2931` n `228`; crypto_major avg `0.4223` n `8`; equity avg `0.0701` n `67`; fx avg `0.0628` n `6`; index avg `0.0919` n `23`; metal avg `0.115` n `18`; unknown avg `0.3239` n `387`
- 24h: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0731` n `228`; crypto_major avg `-0.1006` n `8`; equity avg `0.6154` n `67`; fx avg `-0.0016` n `6`; index avg `-0.0653` n `23`; metal avg `0.5285` n `18`; unknown avg `0.9258` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
