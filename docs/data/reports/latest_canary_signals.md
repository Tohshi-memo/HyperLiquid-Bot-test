# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T18:07:27.740063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0423` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0455` n `13`; crypto_alt avg `-0.2205` n `239`; crypto_major avg `-0.0662` n `8`; equity avg `-0.8486` n `165`; fx avg `-0.0208` n `6`; index avg `-0.0855` n `27`; metal avg `-0.0479` n `20`; unknown avg `-0.0862` n `1258`
- 1h: commodity avg `0.1865` n `13`; crypto_alt avg `0.4103` n `239`; crypto_major avg `0.8983` n `8`; equity avg `-0.0379` n `165`; fx avg `0.0003` n `6`; index avg `0.0418` n `27`; metal avg `0.1062` n `20`; unknown avg `2.0886` n `1260`
- 4h: commodity avg `-0.0983` n `13`; crypto_alt avg `-1.9237` n `239`; crypto_major avg `-1.3131` n `8`; equity avg `-3.3554` n `165`; fx avg `-0.0679` n `6`; index avg `-0.4176` n `27`; metal avg `-0.4046` n `20`; unknown avg `13.0555` n `1253`
- 24h: commodity avg `0.3978` n `13`; crypto_alt avg `-0.4215` n `239`; crypto_major avg `0.2903` n `8`; equity avg `-1.1514` n `165`; fx avg `-0.0038` n `6`; index avg `-0.039` n `27`; metal avg `-0.5081` n `20`; unknown avg `3.5388` n `1162`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
