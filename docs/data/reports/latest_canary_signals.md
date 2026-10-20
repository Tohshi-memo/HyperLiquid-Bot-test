# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T18:42:31.139274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1231` n `13`; crypto_alt avg `-0.1906` n `237`; crypto_major avg `-0.1647` n `8`; equity avg `-0.2877` n `151`; fx avg `0.0064` n `6`; index avg `-0.0552` n `26`; metal avg `-0.0365` n `20`; unknown avg `1.4974` n `1199`
- 1h: commodity avg `0.0664` n `13`; crypto_alt avg `-0.3634` n `237`; crypto_major avg `-0.314` n `8`; equity avg `-0.3283` n `151`; fx avg `0.0133` n `6`; index avg `-0.0576` n `26`; metal avg `-0.0194` n `20`; unknown avg `8.3058` n `1185`
- 4h: commodity avg `0.377` n `13`; crypto_alt avg `-1.159` n `237`; crypto_major avg `-1.0845` n `8`; equity avg `-0.7627` n `151`; fx avg `-0.0071` n `6`; index avg `-0.1179` n `26`; metal avg `-0.2045` n `20`; unknown avg `9.6945` n `1177`
- 24h: commodity avg `-0.1449` n `13`; crypto_alt avg `2.6896` n `237`; crypto_major avg `1.5529` n `8`; equity avg `0.1444` n `151`; fx avg `0.032` n `6`; index avg `0.0051` n `26`; metal avg `-0.0117` n `20`; unknown avg `4.1449` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
