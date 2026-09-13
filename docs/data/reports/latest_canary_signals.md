# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T19:37:26.537779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.1211` n `233`; crypto_major avg `-0.0476` n `8`; equity avg `-0.0639` n `136`; fx avg `0.0015` n `6`; index avg `-0.0119` n `27`; metal avg `0.0001` n `20`; unknown avg `1.7159` n `840`
- 1h: commodity avg `0.0901` n `12`; crypto_alt avg `-0.3981` n `233`; crypto_major avg `-0.2102` n `8`; equity avg `-0.1316` n `136`; fx avg `-0.0006` n `6`; index avg `-0.026` n `27`; metal avg `-0.0211` n `20`; unknown avg `1.2919` n `830`
- 4h: commodity avg `0.0822` n `12`; crypto_alt avg `0.2993` n `233`; crypto_major avg `0.3807` n `8`; equity avg `0.2201` n `136`; fx avg `-0.0018` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0019` n `20`; unknown avg `2.0413` n `766`
- 24h: commodity avg `0.3221` n `12`; crypto_alt avg `0.0619` n `233`; crypto_major avg `-0.5725` n `8`; equity avg `-1.3011` n `136`; fx avg `0.0157` n `6`; index avg `-0.2669` n `26`; metal avg `-0.0908` n `20`; unknown avg `2.6691` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
