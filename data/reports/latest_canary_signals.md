# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T13:22:39.166788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `13`; crypto_alt avg `-0.0801` n `237`; crypto_major avg `-0.0607` n `8`; equity avg `0.1341` n `151`; fx avg `0.0015` n `6`; index avg `0.0093` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.1276` n `1195`
- 1h: commodity avg `-0.093` n `13`; crypto_alt avg `0.252` n `237`; crypto_major avg `0.0904` n `8`; equity avg `0.1992` n `151`; fx avg `0.011` n `6`; index avg `0.0239` n `26`; metal avg `-0.0572` n `20`; unknown avg `0.1942` n `1167`
- 4h: commodity avg `-0.0536` n `13`; crypto_alt avg `-0.2479` n `237`; crypto_major avg `-0.2782` n `8`; equity avg `0.7118` n `151`; fx avg `0.034` n `6`; index avg `0.0492` n `26`; metal avg `-0.0618` n `20`; unknown avg `0.5254` n `1151`
- 24h: commodity avg `-0.3128` n `13`; crypto_alt avg `-0.0878` n `237`; crypto_major avg `0.9021` n `8`; equity avg `3.2612` n `151`; fx avg `-0.0191` n `6`; index avg `0.5146` n `26`; metal avg `0.1518` n `20`; unknown avg `1.6738` n `951`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2048`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1606`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1346`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1198`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0656`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
