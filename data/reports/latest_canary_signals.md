# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T09:52:23.406398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0433` n `13`; crypto_alt avg `0.1716` n `239`; crypto_major avg `0.1483` n `8`; equity avg `-0.0571` n `162`; fx avg `-0.0045` n `6`; index avg `-0.0021` n `27`; metal avg `0.0041` n `20`; unknown avg `0.077` n `1263`
- 1h: commodity avg `-0.0578` n `13`; crypto_alt avg `1.3012` n `239`; crypto_major avg `1.3806` n `8`; equity avg `0.3376` n `162`; fx avg `-0.0032` n `6`; index avg `0.0445` n `27`; metal avg `0.0623` n `20`; unknown avg `0.6029` n `1261`
- 4h: commodity avg `-0.0794` n `13`; crypto_alt avg `0.5052` n `239`; crypto_major avg `0.8821` n `8`; equity avg `0.1984` n `162`; fx avg `-0.0211` n `6`; index avg `0.0302` n `27`; metal avg `0.1413` n `20`; unknown avg `163.7099` n `1225`
- 24h: commodity avg `-0.0012` n `13`; crypto_alt avg `-4.4399` n `239`; crypto_major avg `-3.5981` n `8`; equity avg `-0.8099` n `162`; fx avg `0.0335` n `6`; index avg `-0.069` n `27`; metal avg `-0.3435` n `20`; unknown avg `44.5809` n `1120`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
