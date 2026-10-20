# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T22:52:39.236421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.0698` n `237`; crypto_major avg `-0.0126` n `8`; equity avg `-0.0238` n `151`; fx avg `-0.006` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0217` n `20`; unknown avg `-0.0437` n `1199`
- 1h: commodity avg `-0.013` n `13`; crypto_alt avg `-0.0287` n `237`; crypto_major avg `0.1451` n `8`; equity avg `0.2477` n `151`; fx avg `-0.0165` n `6`; index avg `0.0223` n `26`; metal avg `-0.0222` n `20`; unknown avg `-0.2418` n `1157`
- 4h: commodity avg `0.075` n `13`; crypto_alt avg `0.7171` n `237`; crypto_major avg `0.9223` n `8`; equity avg `1.4867` n `151`; fx avg `-0.0194` n `6`; index avg `0.1881` n `26`; metal avg `0.0217` n `20`; unknown avg `-0.0352` n `1065`
- 24h: commodity avg `-0.0183` n `13`; crypto_alt avg `2.4636` n `237`; crypto_major avg `1.7725` n `8`; equity avg `1.4295` n `151`; fx avg `0.0255` n `6`; index avg `0.1495` n `26`; metal avg `0.0872` n `20`; unknown avg `205.4357` n `1019`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
