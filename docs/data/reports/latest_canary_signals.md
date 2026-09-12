# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T18:22:33.204271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.0276` n `233`; crypto_major avg `-0.0665` n `8`; equity avg `-0.0157` n `136`; fx avg `0.0043` n `6`; index avg `0.0021` n `26`; metal avg `0.0095` n `20`; unknown avg `-0.1474` n `838`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `-0.1328` n `233`; crypto_major avg `-0.1851` n `8`; equity avg `-0.0133` n `136`; fx avg `-0.0046` n `6`; index avg `-0.0017` n `26`; metal avg `-0.002` n `20`; unknown avg `3.2714` n `836`
- 4h: commodity avg `0.0781` n `12`; crypto_alt avg `0.0079` n `233`; crypto_major avg `-0.4105` n `8`; equity avg `-0.019` n `136`; fx avg `-0.0034` n `6`; index avg `0.0048` n `26`; metal avg `0.0154` n `20`; unknown avg `1.7427` n `790`
- 24h: commodity avg `-0.1597` n `12`; crypto_alt avg `1.0487` n `233`; crypto_major avg `0.0157` n `8`; equity avg `-0.1893` n `136`; fx avg `-0.0163` n `6`; index avg `0.0102` n `26`; metal avg `0.0349` n `20`; unknown avg `1.5858` n `692`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
