# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T19:37:30.025755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.0392` n `238`; crypto_major avg `-0.0059` n `8`; equity avg `0.001` n `156`; fx avg `-0.0052` n `6`; index avg `0.004` n `27`; metal avg `-0.0025` n `20`; unknown avg `1.4366` n `1262`
- 1h: commodity avg `-0.0121` n `13`; crypto_alt avg `-0.1957` n `238`; crypto_major avg `-0.0844` n `8`; equity avg `0.0004` n `156`; fx avg `-0.0169` n `6`; index avg `-0.0067` n `27`; metal avg `-0.0001` n `20`; unknown avg `-0.0916` n `1254`
- 4h: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.508` n `238`; crypto_major avg `0.0492` n `8`; equity avg `0.0316` n `156`; fx avg `-0.0208` n `6`; index avg `0.0075` n `27`; metal avg `-0.0075` n `20`; unknown avg `17.2241` n `1204`
- 24h: commodity avg `-0.2362` n `13`; crypto_alt avg `1.0877` n `238`; crypto_major avg `0.486` n `8`; equity avg `0.8749` n `156`; fx avg `-0.0438` n `6`; index avg `0.0326` n `27`; metal avg `0.1176` n `20`; unknown avg `1.042` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
