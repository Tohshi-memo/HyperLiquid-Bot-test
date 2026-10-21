# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T03:22:25.620236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `13`; crypto_alt avg `-0.1109` n `237`; crypto_major avg `-0.081` n `8`; equity avg `0.0287` n `151`; fx avg `-0.0093` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.5636` n `1200`
- 1h: commodity avg `0.0334` n `13`; crypto_alt avg `-0.0058` n `237`; crypto_major avg `-0.0142` n `8`; equity avg `-0.0101` n `151`; fx avg `-0.006` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.4542` n `1197`
- 4h: commodity avg `0.1676` n `13`; crypto_alt avg `0.228` n `237`; crypto_major avg `0.0247` n `8`; equity avg `0.3732` n `151`; fx avg `0.021` n `6`; index avg `0.0706` n `26`; metal avg `-0.0912` n `20`; unknown avg `0.474` n `1191`
- 24h: commodity avg `0.0132` n `13`; crypto_alt avg `2.4462` n `237`; crypto_major avg `1.6808` n `8`; equity avg `2.1042` n `151`; fx avg `0.0425` n `6`; index avg `0.309` n `26`; metal avg `-0.146` n `20`; unknown avg `212.48` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
