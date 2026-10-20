# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T21:37:33.901824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `13`; crypto_alt avg `-0.0635` n `237`; crypto_major avg `-0.0829` n `8`; equity avg `0.1884` n `151`; fx avg `0.0017` n `6`; index avg `0.0133` n `26`; metal avg `-0.0057` n `20`; unknown avg `1.7125` n `1171`
- 1h: commodity avg `0.0634` n `13`; crypto_alt avg `0.1524` n `237`; crypto_major avg `0.1183` n `8`; equity avg `0.909` n `151`; fx avg `0.0039` n `6`; index avg `0.0968` n `26`; metal avg `0.0289` n `20`; unknown avg `0.7487` n `1157`
- 4h: commodity avg `0.1364` n `13`; crypto_alt avg `0.3211` n `237`; crypto_major avg `0.3997` n `8`; equity avg `1.0877` n `151`; fx avg `0.0098` n `6`; index avg `0.1088` n `26`; metal avg `0.0118` n `20`; unknown avg `0.1045` n `1093`
- 24h: commodity avg `-0.0126` n `13`; crypto_alt avg `3.0077` n `237`; crypto_major avg `1.8577` n `8`; equity avg `1.2797` n `151`; fx avg `0.0206` n `6`; index avg `0.1437` n `26`; metal avg `0.0604` n `20`; unknown avg `4.349` n `1054`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1736`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
