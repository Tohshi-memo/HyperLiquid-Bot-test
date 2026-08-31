# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T04:07:27.190842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `-0.1324` n `232`; crypto_major avg `-0.2324` n `8`; equity avg `-0.0142` n `128`; fx avg `0.002` n `6`; index avg `0.0024` n `26`; metal avg `-0.0492` n `20`; unknown avg `-0.1698` n `791`
- 1h: commodity avg `0.0002` n `12`; crypto_alt avg `0.4037` n `231`; crypto_major avg `0.156` n `8`; equity avg `0.0446` n `128`; fx avg `-0.0137` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0461` n `20`; unknown avg `-0.0202` n `791`
- 4h: commodity avg `0.1925` n `12`; crypto_alt avg `1.1685` n `231`; crypto_major avg `0.1685` n `8`; equity avg `0.2854` n `128`; fx avg `-0.0823` n `6`; index avg `0.1482` n `26`; metal avg `-0.2994` n `20`; unknown avg `-0.1696` n `779`
- 24h: commodity avg `0.378` n `12`; crypto_alt avg `-0.137` n `231`; crypto_major avg `-2.057` n `8`; equity avg `-1.1948` n `128`; fx avg `-0.0573` n `6`; index avg `-0.2316` n `26`; metal avg `-0.4287` n `20`; unknown avg `-0.4515` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
