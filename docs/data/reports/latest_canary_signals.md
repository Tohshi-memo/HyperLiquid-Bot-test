# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T03:22:29.977776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0183` n `12`; crypto_alt avg `-0.0763` n `230`; crypto_major avg `-0.0532` n `8`; equity avg `-0.0901` n `102`; fx avg `0.0168` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.0259` n `784`
- 1h: commodity avg `-0.0683` n `12`; crypto_alt avg `-0.3024` n `230`; crypto_major avg `-0.2874` n `8`; equity avg `-0.2373` n `102`; fx avg `0.035` n `6`; index avg `-0.0572` n `25`; metal avg `-0.0198` n `20`; unknown avg `-0.137` n `784`
- 4h: commodity avg `-0.104` n `12`; crypto_alt avg `-0.6994` n `230`; crypto_major avg `-0.7489` n `8`; equity avg `0.1748` n `102`; fx avg `-0.2974` n `6`; index avg `-0.0803` n `25`; metal avg `-0.1047` n `20`; unknown avg `-0.1143` n `784`
- 24h: commodity avg `-0.1489` n `12`; crypto_alt avg `-0.7179` n `230`; crypto_major avg `-0.4204` n `8`; equity avg `0.8696` n `102`; fx avg `-0.2491` n `6`; index avg `0.0561` n `25`; metal avg `-0.041` n `20`; unknown avg `1.2966` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
