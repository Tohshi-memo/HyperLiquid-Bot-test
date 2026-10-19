# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T02:18:13.537655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `-0.2112` n `237`; crypto_major avg `-0.1434` n `8`; equity avg `-0.0687` n `151`; fx avg `-0.0359` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0408` n `20`; unknown avg `0.2877` n `1194`
- 1h: commodity avg `-0.0729` n `13`; crypto_alt avg `0.1333` n `237`; crypto_major avg `0.0266` n `8`; equity avg `-0.0464` n `151`; fx avg `-0.0605` n `6`; index avg `-0.0176` n `26`; metal avg `0.0633` n `20`; unknown avg `0.1043` n `1192`
- 4h: commodity avg `-0.1612` n `13`; crypto_alt avg `1.627` n `237`; crypto_major avg `1.1073` n `8`; equity avg `1.6457` n `151`; fx avg `-0.044` n `6`; index avg `0.2547` n `26`; metal avg `0.0878` n `20`; unknown avg `3.0248` n `1128`
- 24h: commodity avg `-0.4104` n `13`; crypto_alt avg `-0.107` n `237`; crypto_major avg `0.7011` n `8`; equity avg `2.2544` n `151`; fx avg `-0.0555` n `6`; index avg `0.4515` n `26`; metal avg `0.2653` n `20`; unknown avg `2.8306` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2001`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1439`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1094`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0917`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0622`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0611`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
