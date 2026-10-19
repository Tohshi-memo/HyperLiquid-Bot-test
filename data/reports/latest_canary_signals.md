# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T15:37:49.287804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `13`; crypto_alt avg `-0.3459` n `237`; crypto_major avg `-0.3944` n `8`; equity avg `0.2142` n `151`; fx avg `0.005` n `6`; index avg `0.04` n `26`; metal avg `0.0515` n `20`; unknown avg `0.6168` n `1194`
- 1h: commodity avg `0.0458` n `13`; crypto_alt avg `0.7422` n `237`; crypto_major avg `0.3811` n `8`; equity avg `0.7992` n `151`; fx avg `0.0146` n `6`; index avg `0.1443` n `26`; metal avg `0.0671` n `20`; unknown avg `3.252` n `1193`
- 4h: commodity avg `-0.1867` n `13`; crypto_alt avg `0.7367` n `237`; crypto_major avg `0.0751` n `8`; equity avg `0.8224` n `151`; fx avg `0.0286` n `6`; index avg `0.1849` n `26`; metal avg `-0.1425` n `20`; unknown avg `1.0068` n `1103`
- 24h: commodity avg `-0.3244` n `13`; crypto_alt avg `1.4447` n `237`; crypto_major avg `1.6689` n `8`; equity avg `3.8014` n `151`; fx avg `-0.0161` n `6`; index avg `0.7319` n `26`; metal avg `0.1443` n `20`; unknown avg `5.9226` n `916`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
