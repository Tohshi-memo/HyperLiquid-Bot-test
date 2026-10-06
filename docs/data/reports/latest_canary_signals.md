# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T19:37:35.603050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `13`; crypto_alt avg `-0.1116` n `235`; crypto_major avg `0.0461` n `8`; equity avg `-0.1365` n `150`; fx avg `-0.0052` n `6`; index avg `-0.0265` n `26`; metal avg `-0.0382` n `20`; unknown avg `3.6157` n `1076`
- 1h: commodity avg `0.1774` n `13`; crypto_alt avg `-0.4718` n `235`; crypto_major avg `-0.2907` n `8`; equity avg `-0.2613` n `150`; fx avg `0.0058` n `6`; index avg `-0.0446` n `26`; metal avg `0.0073` n `20`; unknown avg `3.4334` n `1074`
- 4h: commodity avg `0.5315` n `13`; crypto_alt avg `-1.3335` n `235`; crypto_major avg `-1.0248` n `8`; equity avg `-0.4869` n `150`; fx avg `-0.019` n `6`; index avg `-0.13` n `26`; metal avg `0.0461` n `20`; unknown avg `2.4027` n `1068`
- 24h: commodity avg `0.2984` n `13`; crypto_alt avg `-0.8404` n `235`; crypto_major avg `-0.5213` n `8`; equity avg `0.3501` n `149`; fx avg `0.1052` n `6`; index avg `-0.0377` n `26`; metal avg `0.0265` n `20`; unknown avg `382.2979` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
