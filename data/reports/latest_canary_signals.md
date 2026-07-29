# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T17:37:27.607694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.89` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0539` n `12`; crypto_alt avg `0.0159` n `230`; crypto_major avg `-0.0617` n `8`; equity avg `-0.2656` n `102`; fx avg `0.0162` n `6`; index avg `-0.031` n `25`; metal avg `-0.1025` n `20`; unknown avg `-0.0529` n `778`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `0.1704` n `230`; crypto_major avg `0.2104` n `8`; equity avg `0.7199` n `102`; fx avg `0.041` n `6`; index avg `0.1741` n `25`; metal avg `0.1668` n `20`; unknown avg `-0.0036` n `778`
- 4h: commodity avg `0.1123` n `12`; crypto_alt avg `-0.4723` n `230`; crypto_major avg `-0.3978` n `8`; equity avg `-1.758` n `102`; fx avg `-0.0039` n `6`; index avg `-0.197` n `25`; metal avg `0.1303` n `20`; unknown avg `-0.1323` n `777`
- 24h: commodity avg `1.1805` n `12`; crypto_alt avg `-1.8286` n `230`; crypto_major avg `0.0989` n `8`; equity avg `-1.6985` n `102`; fx avg `-0.0526` n `6`; index avg `-0.3575` n `25`; metal avg `-0.0699` n `20`; unknown avg `-0.2742` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
