# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T21:34:58.329312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0263` n `12`; crypto_alt avg `-0.0122` n `230`; crypto_major avg `-0.0249` n `8`; equity avg `0.0509` n `108`; fx avg `0.0029` n `6`; index avg `0.0144` n `25`; metal avg `0.0044` n `20`; unknown avg `0.0802` n `781`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `-0.0046` n `230`; crypto_major avg `-0.1355` n `8`; equity avg `0.3531` n `108`; fx avg `0.0076` n `6`; index avg `0.0304` n `25`; metal avg `0.0153` n `20`; unknown avg `0.106` n `781`
- 4h: commodity avg `-0.0782` n `12`; crypto_alt avg `0.2121` n `230`; crypto_major avg `-0.1101` n `8`; equity avg `-0.5788` n `108`; fx avg `0.0545` n `6`; index avg `-0.0079` n `25`; metal avg `-0.1624` n `20`; unknown avg `0.0286` n `781`
- 24h: commodity avg `-1.2447` n `12`; crypto_alt avg `-0.1501` n `230`; crypto_major avg `0.4191` n `8`; equity avg `3.0823` n `107`; fx avg `0.1249` n `6`; index avg `0.7288` n `25`; metal avg `0.855` n `20`; unknown avg `0.4249` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
