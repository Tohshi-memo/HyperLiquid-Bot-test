# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T05:22:16.377394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0789` n `12`; crypto_alt avg `-0.0701` n `228`; crypto_major avg `-0.0554` n `8`; equity avg `0.0423` n `67`; fx avg `0.0204` n `6`; index avg `0.0035` n `23`; metal avg `-0.1332` n `18`; unknown avg `-0.5143` n `397`
- 1h: commodity avg `-0.1854` n `12`; crypto_alt avg `0.9042` n `228`; crypto_major avg `0.7698` n `8`; equity avg `0.1427` n `67`; fx avg `-0.0002` n `6`; index avg `-0.0458` n `23`; metal avg `-0.1124` n `18`; unknown avg `-0.4198` n `397`
- 4h: commodity avg `-0.6889` n `12`; crypto_alt avg `0.8018` n `228`; crypto_major avg `0.3172` n `8`; equity avg `0.4293` n `67`; fx avg `-0.0242` n `6`; index avg `0.1612` n `23`; metal avg `-0.1763` n `18`; unknown avg `-0.4327` n `396`
- 24h: commodity avg `-0.1012` n `12`; crypto_alt avg `0.2697` n `228`; crypto_major avg `0.6114` n `8`; equity avg `0.5619` n `67`; fx avg `-0.0647` n `6`; index avg `-0.1012` n `23`; metal avg `0.4529` n `18`; unknown avg `0.0406` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
