# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T04:07:26.669414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `0.1868` n `232`; crypto_major avg `0.1205` n `8`; equity avg `0.0602` n `133`; fx avg `0.0075` n `6`; index avg `-0.0003` n `26`; metal avg `0.0115` n `20`; unknown avg `-0.052` n `790`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `-0.0024` n `232`; crypto_major avg `-0.0072` n `8`; equity avg `0.2483` n `133`; fx avg `-0.0088` n `6`; index avg `0.0257` n `26`; metal avg `0.0434` n `20`; unknown avg `-0.111` n `790`
- 4h: commodity avg `0.0649` n `12`; crypto_alt avg `0.7769` n `232`; crypto_major avg `0.7523` n `8`; equity avg `0.3039` n `133`; fx avg `-0.1544` n `6`; index avg `0.0538` n `26`; metal avg `0.2528` n `20`; unknown avg `0.1898` n `790`
- 24h: commodity avg `0.2092` n `12`; crypto_alt avg `0.538` n `232`; crypto_major avg `0.6084` n `8`; equity avg `1.7546` n `133`; fx avg `-0.3895` n `6`; index avg `0.2224` n `26`; metal avg `0.9268` n `20`; unknown avg `-0.3979` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
