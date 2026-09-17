# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T21:37:26.771712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1347` n `234`; crypto_major avg `0.0213` n `8`; equity avg `0.0116` n `140`; fx avg `0.003` n `6`; index avg `-0.0015` n `26`; metal avg `-0.0106` n `20`; unknown avg `5.3557` n `911`
- 1h: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.0509` n `234`; crypto_major avg `-0.0963` n `8`; equity avg `0.03` n `140`; fx avg `-0.0112` n `6`; index avg `0.0067` n `26`; metal avg `0.0036` n `20`; unknown avg `6.9861` n `887`
- 4h: commodity avg `-0.2058` n `12`; crypto_alt avg `-0.0002` n `234`; crypto_major avg `-0.1588` n `8`; equity avg `0.1353` n `140`; fx avg `-0.0178` n `6`; index avg `-0.0119` n `26`; metal avg `-0.1597` n `20`; unknown avg `0.7478` n `857`
- 24h: commodity avg `-0.2066` n `12`; crypto_alt avg `3.931` n `234`; crypto_major avg `2.0359` n `8`; equity avg `2.3082` n `138`; fx avg `-0.0005` n `6`; index avg `0.4459` n `26`; metal avg `0.5418` n `20`; unknown avg `2.17` n `763`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
