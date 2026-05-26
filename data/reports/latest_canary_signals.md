# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T05:56:11.958965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `-0.2357` n `228`; crypto_major avg `-0.1349` n `8`; equity avg `-0.0361` n `67`; fx avg `-0.006` n `6`; index avg `-0.049` n `23`; metal avg `-0.2501` n `18`; unknown avg `-0.9216` n `407`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.3517` n `228`; crypto_major avg `0.2864` n `8`; equity avg `-0.0554` n `67`; fx avg `-0.0249` n `6`; index avg `-0.0696` n `23`; metal avg `-0.0705` n `18`; unknown avg `-0.7022` n `407`
- 4h: commodity avg `-0.0992` n `12`; crypto_alt avg `0.7341` n `228`; crypto_major avg `0.5014` n `8`; equity avg `0.1815` n `67`; fx avg `-0.0429` n `6`; index avg `0.051` n `23`; metal avg `0.0079` n `18`; unknown avg `-0.7876` n `407`
- 24h: commodity avg `0.5923` n `12`; crypto_alt avg `-0.402` n `228`; crypto_major avg `-1.0332` n `8`; equity avg `-0.6239` n `67`; fx avg `-0.0655` n `6`; index avg `-0.0239` n `23`; metal avg `-0.3142` n `18`; unknown avg `0.3663` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
