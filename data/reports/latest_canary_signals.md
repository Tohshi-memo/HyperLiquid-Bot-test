# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T22:43:43.863795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0781` n `13`; crypto_alt avg `-0.6303` n `237`; crypto_major avg `-0.5165` n `8`; equity avg `-0.9848` n `151`; fx avg `-0.0235` n `6`; index avg `-0.1592` n `26`; metal avg `-0.0088` n `20`; unknown avg `1.1618` n `1042`
- 1h: commodity avg `0.0781` n `13`; crypto_alt avg `-0.6303` n `237`; crypto_major avg `-0.5165` n `8`; equity avg `-0.9848` n `151`; fx avg `-0.0235` n `6`; index avg `-0.1592` n `26`; metal avg `-0.0088` n `20`; unknown avg `1.1618` n `1042`
- 4h: commodity avg `0.0972` n `13`; crypto_alt avg `-0.3623` n `237`; crypto_major avg `-0.4788` n `8`; equity avg `-0.5486` n `151`; fx avg `-0.0068` n `6`; index avg `-0.1305` n `26`; metal avg `-0.078` n `20`; unknown avg `0.8645` n `1014`
- 24h: commodity avg `-0.5535` n `13`; crypto_alt avg `1.5092` n `237`; crypto_major avg `0.9141` n `8`; equity avg `-0.67` n `151`; fx avg `0.0025` n `6`; index avg `-0.1206` n `26`; metal avg `-0.216` n `20`; unknown avg `117.7772` n `931`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `671`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1447`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `671`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1198`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1173`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.111`, n `671`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `671`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0884`, n `671`, weak_sample_signal
