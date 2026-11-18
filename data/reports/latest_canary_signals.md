# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T06:07:28.177762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `13`; crypto_alt avg `0.1396` n `239`; crypto_major avg `0.0308` n `8`; equity avg `-0.1687` n `163`; fx avg `-0.003` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0913` n `20`; unknown avg `0.058` n `1244`
- 1h: commodity avg `0.0893` n `13`; crypto_alt avg `0.8862` n `239`; crypto_major avg `0.5662` n `8`; equity avg `0.4737` n `163`; fx avg `0.0171` n `6`; index avg `0.052` n `27`; metal avg `0.0052` n `20`; unknown avg `-0.103` n `1238`
- 4h: commodity avg `-0.109` n `13`; crypto_alt avg `0.5814` n `239`; crypto_major avg `0.7545` n `8`; equity avg `0.3966` n `163`; fx avg `-0.0081` n `6`; index avg `0.0974` n `27`; metal avg `-0.1531` n `20`; unknown avg `3.6826` n `1228`
- 24h: commodity avg `0.1531` n `13`; crypto_alt avg `0.3396` n `239`; crypto_major avg `0.545` n `8`; equity avg `0.4884` n `163`; fx avg `-0.0997` n `6`; index avg `0.0413` n `27`; metal avg `-0.8772` n `20`; unknown avg `496.5797` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
