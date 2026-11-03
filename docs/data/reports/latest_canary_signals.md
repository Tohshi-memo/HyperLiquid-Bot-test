# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T10:37:24.390332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0618` n `13`; crypto_alt avg `0.1767` n `239`; crypto_major avg `0.1011` n `8`; equity avg `-0.0226` n `157`; fx avg `0.0028` n `6`; index avg `0.0043` n `27`; metal avg `-0.0157` n `20`; unknown avg `0.2556` n `1264`
- 1h: commodity avg `-0.0567` n `13`; crypto_alt avg `0.2318` n `239`; crypto_major avg `0.1337` n `8`; equity avg `0.2142` n `157`; fx avg `-0.0069` n `6`; index avg `0.0462` n `27`; metal avg `-0.0082` n `20`; unknown avg `0.0462` n `1258`
- 4h: commodity avg `0.2998` n `13`; crypto_alt avg `0.6131` n `239`; crypto_major avg `0.4584` n `8`; equity avg `0.9203` n `157`; fx avg `0.0595` n `6`; index avg `0.1004` n `27`; metal avg `-0.2219` n `20`; unknown avg `0.8139` n `1228`
- 24h: commodity avg `-0.3565` n `13`; crypto_alt avg `-1.4734` n `238`; crypto_major avg `-0.8797` n `8`; equity avg `-3.4019` n `157`; fx avg `0.0205` n `6`; index avg `-0.2079` n `27`; metal avg `-0.4705` n `20`; unknown avg `4.1277` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
