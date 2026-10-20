# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T18:22:29.940175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.0972` n `237`; crypto_major avg `-0.0599` n `8`; equity avg `-0.0342` n `151`; fx avg `-0.0033` n `6`; index avg `0.0005` n `26`; metal avg `0.0032` n `20`; unknown avg `1.313` n `1195`
- 1h: commodity avg `-0.0642` n `13`; crypto_alt avg `-0.0844` n `237`; crypto_major avg `-0.1461` n `8`; equity avg `-0.0696` n `151`; fx avg `0.0036` n `6`; index avg `0.0025` n `26`; metal avg `0.0158` n `20`; unknown avg `8.2411` n `1185`
- 4h: commodity avg `0.0752` n `13`; crypto_alt avg `-0.1634` n `237`; crypto_major avg `-0.4299` n `8`; equity avg `0.173` n `151`; fx avg `-0.026` n `6`; index avg `0.0267` n `26`; metal avg `-0.0564` n `20`; unknown avg `0.864` n `1177`
- 24h: commodity avg `-0.3572` n `13`; crypto_alt avg `2.9392` n `237`; crypto_major avg `1.7528` n `8`; equity avg `0.2971` n `151`; fx avg `0.0194` n `6`; index avg `0.0429` n `26`; metal avg `-0.008` n `20`; unknown avg `4.3263` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
