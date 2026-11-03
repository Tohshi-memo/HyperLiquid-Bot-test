# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T11:52:25.506813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `13`; crypto_alt avg `0.2774` n `239`; crypto_major avg `0.1014` n `8`; equity avg `-0.0823` n `157`; fx avg `0.0014` n `6`; index avg `-0.0148` n `27`; metal avg `0.0126` n `20`; unknown avg `20.6296` n `1264`
- 1h: commodity avg `0.1793` n `13`; crypto_alt avg `0.612` n `239`; crypto_major avg `0.1182` n `8`; equity avg `-0.1361` n `157`; fx avg `0.0103` n `6`; index avg `-0.0338` n `27`; metal avg `0.0097` n `20`; unknown avg `1.069` n `1232`
- 4h: commodity avg `0.27` n `13`; crypto_alt avg `1.1042` n `239`; crypto_major avg `0.422` n `8`; equity avg `0.6691` n `157`; fx avg `0.0573` n `6`; index avg `0.0551` n `27`; metal avg `-0.0555` n `20`; unknown avg `1.4909` n `1202`
- 24h: commodity avg `-0.0703` n `13`; crypto_alt avg `-0.9412` n `238`; crypto_major avg `-0.7654` n `8`; equity avg `-3.5289` n `157`; fx avg `0.0175` n `6`; index avg `-0.2542` n `27`; metal avg `-0.426` n `20`; unknown avg `3.9959` n `1022`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
