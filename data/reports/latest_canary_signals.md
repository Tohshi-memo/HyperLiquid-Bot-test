# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T01:07:26.649531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0772` n `13`; crypto_alt avg `-0.1349` n `237`; crypto_major avg `-0.3836` n `8`; equity avg `-0.0641` n `151`; fx avg `-0.0018` n `6`; index avg `-0.0018` n `26`; metal avg `-0.1859` n `20`; unknown avg `6.2675` n `1193`
- 1h: commodity avg `0.0772` n `13`; crypto_alt avg `-0.1349` n `237`; crypto_major avg `-0.3836` n `8`; equity avg `-0.0641` n `151`; fx avg `-0.0018` n `6`; index avg `-0.0018` n `26`; metal avg `-0.1859` n `20`; unknown avg `6.2675` n `1193`
- 4h: commodity avg `0.1554` n `13`; crypto_alt avg `-0.766` n `237`; crypto_major avg `-0.8975` n `8`; equity avg `-1.049` n `151`; fx avg `-0.0253` n `6`; index avg `-0.1611` n `26`; metal avg `-0.1947` n `20`; unknown avg `4.8713` n `1042`
- 24h: commodity avg `-0.5951` n `13`; crypto_alt avg `1.653` n `237`; crypto_major avg `0.8183` n `8`; equity avg `-0.6808` n `151`; fx avg `-0.0034` n `6`; index avg `-0.031` n `26`; metal avg `-0.2443` n `20`; unknown avg `120.293` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `671`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `671`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `671`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `671`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0886`, n `671`, weak_sample_signal
