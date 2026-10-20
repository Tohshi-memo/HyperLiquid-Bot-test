# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T21:52:31.436070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `0.0097` n `237`; crypto_major avg `-0.0379` n `8`; equity avg `-0.0226` n `151`; fx avg `0.0176` n `6`; index avg `0.0079` n `26`; metal avg `0.0128` n `20`; unknown avg `0.0241` n `1199`
- 1h: commodity avg `-0.0005` n `13`; crypto_alt avg `0.1817` n `237`; crypto_major avg `0.0872` n `8`; equity avg `0.5603` n `151`; fx avg `0.024` n `6`; index avg `0.0511` n `26`; metal avg `0.0269` n `20`; unknown avg `1.0705` n `1157`
- 4h: commodity avg `0.1466` n `13`; crypto_alt avg `0.1295` n `237`; crypto_major avg `0.2581` n `8`; equity avg `1.0052` n `151`; fx avg `0.0192` n `6`; index avg `0.1081` n `26`; metal avg `0.0097` n `20`; unknown avg `-0.0131` n `1099`
- 24h: commodity avg `-0.0114` n `13`; crypto_alt avg `3.008` n `237`; crypto_major avg `1.8369` n `8`; equity avg `1.2727` n `151`; fx avg `0.035` n `6`; index avg `0.1389` n `26`; metal avg `0.0751` n `20`; unknown avg `4.3819` n `1054`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
