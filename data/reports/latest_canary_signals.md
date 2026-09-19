# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T15:22:26.405294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `-0.2656` n `234`; crypto_major avg `-0.1885` n `8`; equity avg `-0.0002` n `140`; fx avg `-0.0162` n `6`; index avg `0.0034` n `26`; metal avg `-0.0064` n `20`; unknown avg `-0.0053` n `943`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.341` n `234`; crypto_major avg `-0.229` n `8`; equity avg `-0.0052` n `140`; fx avg `-0.0096` n `6`; index avg `0.0055` n `26`; metal avg `0.0075` n `20`; unknown avg `1.0144` n `940`
- 4h: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.0184` n `234`; crypto_major avg `0.3091` n `8`; equity avg `0.0422` n `140`; fx avg `-0.031` n `6`; index avg `0.019` n `26`; metal avg `0.023` n `20`; unknown avg `0.448` n `932`
- 24h: commodity avg `-0.2062` n `12`; crypto_alt avg `2.7404` n `234`; crypto_major avg `1.4713` n `8`; equity avg `0.7911` n `140`; fx avg `0.0056` n `6`; index avg `0.1454` n `26`; metal avg `0.0743` n `20`; unknown avg `1.6682` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
