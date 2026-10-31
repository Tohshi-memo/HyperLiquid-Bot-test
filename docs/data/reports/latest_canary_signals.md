# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T00:37:25.037202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.0482` n `238`; crypto_major avg `-0.0071` n `8`; equity avg `0.004` n `156`; fx avg `0.002` n `6`; index avg `0.0002` n `27`; metal avg `0.0091` n `20`; unknown avg `-0.1794` n `1260`
- 1h: commodity avg `-0.0753` n `13`; crypto_alt avg `0.2331` n `238`; crypto_major avg `0.1639` n `8`; equity avg `0.0414` n `156`; fx avg `0.0052` n `6`; index avg `0.0142` n `27`; metal avg `0.0226` n `20`; unknown avg `-0.2508` n `1248`
- 4h: commodity avg `-0.0922` n `13`; crypto_alt avg `1.7256` n `238`; crypto_major avg `0.6377` n `8`; equity avg `0.2574` n `156`; fx avg `-0.0212` n `6`; index avg `0.0439` n `27`; metal avg `0.087` n `20`; unknown avg `-0.0423` n `1233`
- 24h: commodity avg `0.0229` n `13`; crypto_alt avg `5.1178` n `238`; crypto_major avg `1.5156` n `8`; equity avg `-2.3201` n `156`; fx avg `-0.1487` n `6`; index avg `-0.1953` n `27`; metal avg `-0.8616` n `20`; unknown avg `8.8587` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
