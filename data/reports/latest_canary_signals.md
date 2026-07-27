# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T01:07:27.377045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0462` n `12`; crypto_alt avg `-0.0141` n `230`; crypto_major avg `0.0081` n `8`; equity avg `-0.1901` n `100`; fx avg `0.0061` n `6`; index avg `-0.0792` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.069` n `775`
- 1h: commodity avg `0.0144` n `12`; crypto_alt avg `-0.033` n `230`; crypto_major avg `-0.1173` n `8`; equity avg `-0.0194` n `100`; fx avg `0.0663` n `6`; index avg `-0.0219` n `25`; metal avg `-0.0194` n `20`; unknown avg `-0.2276` n `775`
- 4h: commodity avg `-0.3969` n `12`; crypto_alt avg `0.8575` n `230`; crypto_major avg `0.8391` n `8`; equity avg `0.2528` n `100`; fx avg `0.0806` n `6`; index avg `0.0364` n `25`; metal avg `0.2156` n `20`; unknown avg `-0.1189` n `775`
- 24h: commodity avg `-0.4891` n `12`; crypto_alt avg `1.6385` n `230`; crypto_major avg `1.5828` n `8`; equity avg `0.771` n `100`; fx avg `0.124` n `6`; index avg `0.1086` n `25`; metal avg `0.4261` n `20`; unknown avg `0.0521` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1728`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
