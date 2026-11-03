# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T20:53:47.951195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `0.0869` n `239`; crypto_major avg `0.1169` n `8`; equity avg `-0.0475` n `158`; fx avg `0.0012` n `6`; index avg `0.0015` n `27`; metal avg `0.0086` n `20`; unknown avg `9.9143` n `1247`
- 1h: commodity avg `0.0233` n `13`; crypto_alt avg `0.1273` n `239`; crypto_major avg `0.2657` n `8`; equity avg `0.1553` n `158`; fx avg `0.0002` n `6`; index avg `0.0132` n `27`; metal avg `-0.0226` n `20`; unknown avg `26.0223` n `1219`
- 4h: commodity avg `0.208` n `13`; crypto_alt avg `-0.1022` n `239`; crypto_major avg `-0.0762` n `8`; equity avg `0.0949` n `158`; fx avg `0.0202` n `6`; index avg `-0.0233` n `27`; metal avg `-0.0847` n `20`; unknown avg `0.3454` n `1185`
- 24h: commodity avg `0.4253` n `13`; crypto_alt avg `1.2117` n `239`; crypto_major avg `1.6276` n `8`; equity avg `1.8624` n `158`; fx avg `0.0733` n `6`; index avg `0.1789` n `27`; metal avg `-0.5128` n `20`; unknown avg `376.1154` n `1043`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
