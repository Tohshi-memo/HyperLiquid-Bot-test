# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T21:22:34.603114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `0.0153` n `230`; crypto_major avg `-0.0696` n `8`; equity avg `0.016` n `103`; fx avg `0.0009` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0005` n `784`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `-0.03` n `230`; crypto_major avg `-0.3142` n `8`; equity avg `0.0392` n `103`; fx avg `0.0143` n `6`; index avg `-0.0062` n `25`; metal avg `0.0519` n `20`; unknown avg `0.1039` n `784`
- 4h: commodity avg `0.063` n `12`; crypto_alt avg `0.1874` n `230`; crypto_major avg `-0.1568` n `8`; equity avg `0.6057` n `103`; fx avg `0.0085` n `6`; index avg `0.095` n `25`; metal avg `0.1993` n `20`; unknown avg `-0.19` n `784`
- 24h: commodity avg `-0.0971` n `12`; crypto_alt avg `0.3311` n `230`; crypto_major avg `0.1995` n `8`; equity avg `2.0281` n `103`; fx avg `-0.3137` n `6`; index avg `0.0707` n `25`; metal avg `-0.3918` n `20`; unknown avg `0.014` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
