# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T19:22:34.965186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `13`; crypto_alt avg `0.0858` n `237`; crypto_major avg `0.0551` n `8`; equity avg `0.1609` n `151`; fx avg `0.0043` n `6`; index avg `0.0226` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.1589` n `1196`
- 1h: commodity avg `-0.1199` n `13`; crypto_alt avg `0.2945` n `237`; crypto_major avg `0.1021` n `8`; equity avg `0.2061` n `151`; fx avg `0.0029` n `6`; index avg `0.0358` n `26`; metal avg `-0.038` n `20`; unknown avg `-0.5758` n `1194`
- 4h: commodity avg `0.058` n `13`; crypto_alt avg `-0.6301` n `237`; crypto_major avg `-0.7018` n `8`; equity avg `-0.7646` n `151`; fx avg `0.0001` n `6`; index avg `-0.1043` n `26`; metal avg `0.0174` n `20`; unknown avg `-0.3827` n `1186`
- 24h: commodity avg `-0.2785` n `13`; crypto_alt avg `2.0884` n `237`; crypto_major avg `1.7651` n `8`; equity avg `2.9488` n `151`; fx avg `-0.0266` n `6`; index avg `0.5842` n `26`; metal avg `0.1014` n `20`; unknown avg `2.9983` n `920`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
