# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T00:52:25.632936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.2251` n `237`; crypto_major avg `0.2025` n `8`; equity avg `0.2384` n `151`; fx avg `-0.0038` n `6`; index avg `0.0252` n `26`; metal avg `0.0051` n `20`; unknown avg `0.2271` n `1193`
- 1h: commodity avg `-0.0264` n `13`; crypto_alt avg `0.0062` n `236`; crypto_major avg `0.232` n `8`; equity avg `-0.05` n `151`; fx avg `-0.001` n `6`; index avg `0.0022` n `26`; metal avg `0.003` n `20`; unknown avg `5.3911` n `1185`
- 4h: commodity avg `-0.064` n `13`; crypto_alt avg `-0.9156` n `236`; crypto_major avg `-0.5215` n `8`; equity avg `-0.7089` n `151`; fx avg `0.0007` n `6`; index avg `-0.0811` n `26`; metal avg `-0.0353` n `20`; unknown avg `0.0915` n `1179`
- 24h: commodity avg `-0.1446` n `13`; crypto_alt avg `-2.0627` n `236`; crypto_major avg `-0.6215` n `8`; equity avg `-0.7086` n `151`; fx avg `-0.0196` n `6`; index avg `-0.0885` n `26`; metal avg `-0.0598` n `20`; unknown avg `5.241` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1634`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
