# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T17:22:34.510779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0778` n `13`; crypto_alt avg `-0.2163` n `239`; crypto_major avg `-0.2458` n `8`; equity avg `-0.3185` n `162`; fx avg `-0.0083` n `6`; index avg `-0.022` n `27`; metal avg `-0.0274` n `20`; unknown avg `0.0663` n `1260`
- 1h: commodity avg `-0.1433` n `13`; crypto_alt avg `-0.2573` n `239`; crypto_major avg `0.0951` n `8`; equity avg `0.6657` n `162`; fx avg `-0.0179` n `6`; index avg `0.0648` n `27`; metal avg `-0.0051` n `20`; unknown avg `5.7612` n `1260`
- 4h: commodity avg `-0.209` n `13`; crypto_alt avg `-0.8152` n `239`; crypto_major avg `-1.1544` n `8`; equity avg `-2.5387` n `162`; fx avg `-0.0653` n `6`; index avg `-0.2464` n `27`; metal avg `-0.2458` n `20`; unknown avg `165.3757` n `1250`
- 24h: commodity avg `0.0762` n `13`; crypto_alt avg `-0.0084` n `239`; crypto_major avg `-1.8857` n `8`; equity avg `-3.156` n `162`; fx avg `-0.03` n `6`; index avg `-0.2789` n `27`; metal avg `-0.1965` n `20`; unknown avg `2.2893` n `1091`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
