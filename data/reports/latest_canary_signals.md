# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T19:52:25.489426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `0.2331` n `239`; crypto_major avg `0.0792` n `8`; equity avg `0.0644` n `162`; fx avg `0.0183` n `6`; index avg `0.004` n `27`; metal avg `0.0158` n `20`; unknown avg `-0.0248` n `1265`
- 1h: commodity avg `0.0428` n `13`; crypto_alt avg `0.7247` n `239`; crypto_major avg `0.7487` n `8`; equity avg `0.4616` n `162`; fx avg `0.0205` n `6`; index avg `0.0547` n `27`; metal avg `0.0074` n `20`; unknown avg `3.1521` n `1261`
- 4h: commodity avg `0.0371` n `13`; crypto_alt avg `0.4808` n `239`; crypto_major avg `0.5431` n `8`; equity avg `0.5548` n `162`; fx avg `0.0519` n `6`; index avg `0.0509` n `27`; metal avg `0.1006` n `20`; unknown avg `3.961` n `1252`
- 24h: commodity avg `0.0929` n `13`; crypto_alt avg `0.0385` n `239`; crypto_major avg `0.1623` n `8`; equity avg `0.5997` n `162`; fx avg `0.0281` n `6`; index avg `0.0876` n `27`; metal avg `-0.0525` n `20`; unknown avg `3.1907` n `1134`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
