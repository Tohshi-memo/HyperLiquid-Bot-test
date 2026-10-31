# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T19:52:27.430290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0418` n `10`; crypto_alt avg `-0.125` n `231`; crypto_major avg `-0.0721` n `8`; equity avg `-0.019` n `118`; fx avg `0.0127` n `5`; index avg `-0.0075` n `8`; metal avg `0.0026` n `16`; unknown avg `-0.2932` n `1233`
- 1h: commodity avg `-0.0437` n `10`; crypto_alt avg `-0.3221` n `231`; crypto_major avg `-0.153` n `8`; equity avg `-0.0365` n `118`; fx avg `0.0023` n `5`; index avg `0.0103` n `8`; metal avg `-0.0004` n `16`; unknown avg `0.2461` n `1225`
- 4h: commodity avg `-0.0643` n `10`; crypto_alt avg `-0.7186` n `231`; crypto_major avg `0.0704` n `8`; equity avg `0.0527` n `118`; fx avg `-0.004` n `5`; index avg `0.0236` n `8`; metal avg `-0.0019` n `16`; unknown avg `1.4843` n `1175`
- 24h: commodity avg `-0.324` n `10`; crypto_alt avg `0.489` n `231`; crypto_major avg `0.1095` n `8`; equity avg `0.3146` n `118`; fx avg `-0.0323` n `5`; index avg `-0.0764` n `8`; metal avg `0.0474` n `16`; unknown avg `0.7293` n `1012`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
