# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T01:22:27.458398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `0.1221` n `237`; crypto_major avg `0.1479` n `8`; equity avg `-0.1526` n `151`; fx avg `0.0005` n `6`; index avg `-0.0257` n `26`; metal avg `-0.0422` n `20`; unknown avg `-0.3128` n `1201`
- 1h: commodity avg `0.078` n `13`; crypto_alt avg `-0.0131` n `237`; crypto_major avg `-0.2364` n `8`; equity avg `-0.217` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0276` n `26`; metal avg `-0.2279` n `20`; unknown avg `2.3097` n `1193`
- 4h: commodity avg `0.1563` n `13`; crypto_alt avg `-0.6454` n `237`; crypto_major avg `-0.7511` n `8`; equity avg `-1.1989` n `151`; fx avg `-0.0248` n `6`; index avg `-0.1867` n `26`; metal avg `-0.2366` n `20`; unknown avg `0.7769` n `1042`
- 24h: commodity avg `-0.5845` n `13`; crypto_alt avg `1.705` n `237`; crypto_major avg `0.8926` n `8`; equity avg `-0.9977` n `151`; fx avg `-0.0005` n `6`; index avg `-0.1165` n `26`; metal avg `-0.3075` n `20`; unknown avg `117.1708` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `670`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `670`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.118`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `670`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `670`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `670`, weak_sample_signal
