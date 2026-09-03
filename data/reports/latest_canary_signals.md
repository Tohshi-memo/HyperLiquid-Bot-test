# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T03:22:29.871304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0426` n `232`; crypto_major avg `-0.0173` n `8`; equity avg `0.143` n `133`; fx avg `-0.0094` n `6`; index avg `0.0197` n `26`; metal avg `0.0071` n `20`; unknown avg `0.0151` n `792`
- 1h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.3391` n `232`; crypto_major avg `0.3701` n `8`; equity avg `0.1511` n `133`; fx avg `-0.0212` n `6`; index avg `0.0283` n `26`; metal avg `0.0637` n `20`; unknown avg `0.4048` n `790`
- 4h: commodity avg `0.0493` n `12`; crypto_alt avg `0.9751` n `232`; crypto_major avg `1.052` n `8`; equity avg `0.2671` n `133`; fx avg `-0.09` n `6`; index avg `0.0152` n `26`; metal avg `0.2302` n `20`; unknown avg `0.7027` n `790`
- 24h: commodity avg `0.1776` n `12`; crypto_alt avg `0.2184` n `232`; crypto_major avg `0.382` n `8`; equity avg `1.4926` n `133`; fx avg `-0.4043` n `6`; index avg `0.1689` n `26`; metal avg `0.8989` n `20`; unknown avg `-0.4346` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0471`, n `668`, weak_sample_signal
