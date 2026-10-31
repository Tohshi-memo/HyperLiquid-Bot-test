# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T23:52:32.560723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.0266` n `238`; crypto_major avg `0.0163` n `8`; equity avg `0.0048` n `156`; fx avg `-0.0025` n `6`; index avg `0.0073` n `27`; metal avg `0.0003` n `20`; unknown avg `-0.018` n `1262`
- 1h: commodity avg `-0.0126` n `13`; crypto_alt avg `0.0715` n `238`; crypto_major avg `0.1104` n `8`; equity avg `0.0141` n `156`; fx avg `-0.0089` n `6`; index avg `0.0123` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.4777` n `1238`
- 4h: commodity avg `0.0867` n `10`; crypto_alt avg `-0.1502` n `231`; crypto_major avg `-0.1484` n `8`; equity avg `-0.0223` n `118`; fx avg `0.0008` n `5`; index avg `0.0086` n `8`; metal avg `0.0111` n `16`; unknown avg `3.3662` n `1059`
- 24h: commodity avg `-0.0555` n `13`; crypto_alt avg `-0.932` n `238`; crypto_major avg `-0.471` n `8`; equity avg `0.0402` n `156`; fx avg `0.0073` n `6`; index avg `-0.0511` n `27`; metal avg `0.0424` n `20`; unknown avg `0.893` n `1030`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
