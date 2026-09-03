# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T08:37:23.821540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0504` n `12`; crypto_alt avg `0.1094` n `232`; crypto_major avg `0.1615` n `8`; equity avg `0.0123` n `133`; fx avg `-0.0099` n `6`; index avg `0.0006` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.3027` n `792`
- 1h: commodity avg `0.0577` n `12`; crypto_alt avg `0.0901` n `232`; crypto_major avg `0.1097` n `8`; equity avg `0.1089` n `133`; fx avg `-0.0316` n `6`; index avg `0.0412` n `26`; metal avg `0.0759` n `20`; unknown avg `0.9192` n `790`
- 4h: commodity avg `-0.0507` n `12`; crypto_alt avg `0.6618` n `232`; crypto_major avg `0.5761` n `8`; equity avg `-0.1974` n `133`; fx avg `-0.0685` n `6`; index avg `-0.0691` n `26`; metal avg `0.0304` n `20`; unknown avg `-0.1617` n `754`
- 24h: commodity avg `0.2278` n `12`; crypto_alt avg `1.0164` n `232`; crypto_major avg `1.2857` n `8`; equity avg `1.517` n `133`; fx avg `-0.3637` n `6`; index avg `0.1345` n `26`; metal avg `0.8284` n `20`; unknown avg `-0.2751` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
