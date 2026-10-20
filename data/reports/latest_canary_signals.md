# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T16:22:40.169382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0685` n `13`; crypto_alt avg `-0.516` n `237`; crypto_major avg `-0.3825` n `8`; equity avg `-0.2655` n `151`; fx avg `-0.0057` n `6`; index avg `-0.0569` n `26`; metal avg `-0.0551` n `20`; unknown avg `2.6149` n `1199`
- 1h: commodity avg `0.148` n `13`; crypto_alt avg `0.0973` n `237`; crypto_major avg `0.0675` n `8`; equity avg `-0.0667` n `151`; fx avg `-0.0141` n `6`; index avg `-0.0436` n `26`; metal avg `-0.073` n `20`; unknown avg `-0.2007` n `1191`
- 4h: commodity avg `-0.5213` n `13`; crypto_alt avg `1.8397` n `237`; crypto_major avg `1.177` n `8`; equity avg `2.0349` n `151`; fx avg `0.0398` n `6`; index avg `0.3088` n `26`; metal avg `0.186` n `20`; unknown avg `4.2532` n `1100`
- 24h: commodity avg `-0.4604` n `13`; crypto_alt avg `1.8586` n `237`; crypto_major avg `0.9827` n `8`; equity avg `-0.4631` n `151`; fx avg `0.0226` n `6`; index avg `-0.0963` n `26`; metal avg `-0.0113` n `20`; unknown avg `3.7389` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
