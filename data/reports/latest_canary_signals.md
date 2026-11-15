# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T06:07:26.986947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.3804` n `239`; crypto_major avg `-0.7293` n `8`; equity avg `-0.1467` n `162`; fx avg `0.0006` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0514` n `20`; unknown avg `1.5738` n `1239`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.3385` n `239`; crypto_major avg `-0.745` n `8`; equity avg `-0.1944` n `162`; fx avg `0.0068` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0394` n `20`; unknown avg `0.0663` n `1241`
- 4h: commodity avg `0.0175` n `13`; crypto_alt avg `1.3533` n `239`; crypto_major avg `1.399` n `8`; equity avg `0.2901` n `162`; fx avg `0.0195` n `6`; index avg `0.0049` n `27`; metal avg `0.0183` n `20`; unknown avg `2.0648` n `1223`
- 24h: commodity avg `0.0834` n `13`; crypto_alt avg `-5.9914` n `239`; crypto_major avg `-5.1582` n `8`; equity avg `-1.1128` n `162`; fx avg `0.0443` n `6`; index avg `-0.1083` n `27`; metal avg `-0.507` n `20`; unknown avg `48.4962` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
