# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T08:22:31.607421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `13`; crypto_alt avg `-0.0872` n `237`; crypto_major avg `-0.0465` n `8`; equity avg `-0.0418` n `151`; fx avg `-0.0094` n `6`; index avg `-0.0336` n `26`; metal avg `0.0029` n `20`; unknown avg `0.7585` n `1200`
- 1h: commodity avg `-0.0087` n `13`; crypto_alt avg `0.1054` n `237`; crypto_major avg `0.299` n `8`; equity avg `0.0046` n `151`; fx avg `0.0017` n `6`; index avg `0.0015` n `26`; metal avg `0.0114` n `20`; unknown avg `0.7712` n `1182`
- 4h: commodity avg `-0.136` n `13`; crypto_alt avg `0.5857` n `237`; crypto_major avg `0.6121` n `8`; equity avg `-0.0187` n `151`; fx avg `-0.0039` n `6`; index avg `0.0023` n `26`; metal avg `-0.0966` n `20`; unknown avg `1.198` n `1158`
- 24h: commodity avg `-0.1946` n `13`; crypto_alt avg `3.4645` n `237`; crypto_major avg `2.6361` n `8`; equity avg `2.6529` n `151`; fx avg `0.0053` n `6`; index avg `0.3317` n `26`; metal avg `-0.1365` n `20`; unknown avg `5293.612` n `986`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
