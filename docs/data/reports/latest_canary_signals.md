# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T04:37:27.198695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.3247` n `234`; crypto_major avg `-0.5915` n `8`; equity avg `-0.0917` n `140`; fx avg `-0.0225` n `6`; index avg `-0.0067` n `26`; metal avg `0.019` n `20`; unknown avg `-0.1065` n `944`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.1916` n `234`; crypto_major avg `0.1216` n `8`; equity avg `-0.6112` n `140`; fx avg `-0.0017` n `6`; index avg `-0.0602` n `26`; metal avg `-0.0272` n `20`; unknown avg `1.1837` n `936`
- 4h: commodity avg `0.1059` n `12`; crypto_alt avg `-0.6797` n `234`; crypto_major avg `-0.9089` n `8`; equity avg `-0.6971` n `140`; fx avg `-0.0504` n `6`; index avg `-0.0967` n `26`; metal avg `-0.1459` n `20`; unknown avg `1.3185` n `936`
- 24h: commodity avg `-0.1584` n `12`; crypto_alt avg `2.7013` n `234`; crypto_major avg `4.3845` n `8`; equity avg `1.9324` n `140`; fx avg `-0.2672` n `6`; index avg `0.4163` n `26`; metal avg `-0.0671` n `20`; unknown avg `8.7597` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
