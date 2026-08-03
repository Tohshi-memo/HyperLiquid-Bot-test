# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T21:07:31.727462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0806` n `230`; crypto_major avg `0.0143` n `8`; equity avg `0.0409` n `103`; fx avg `-0.0017` n `6`; index avg `-0.0265` n `25`; metal avg `0.0113` n `20`; unknown avg `-0.005` n `784`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `0.1284` n `230`; crypto_major avg `-0.0473` n `8`; equity avg `0.1287` n `103`; fx avg `0.019` n `6`; index avg `0.0196` n `25`; metal avg `0.0739` n `20`; unknown avg `0.0447` n `784`
- 4h: commodity avg `0.0332` n `12`; crypto_alt avg `0.2099` n `230`; crypto_major avg `-0.0326` n `8`; equity avg `0.8657` n `103`; fx avg `0.0122` n `6`; index avg `0.1442` n `25`; metal avg `0.2241` n `20`; unknown avg `-0.1372` n `784`
- 24h: commodity avg `-0.1342` n `12`; crypto_alt avg `0.308` n `230`; crypto_major avg `0.3261` n `8`; equity avg `2.0396` n `103`; fx avg `-0.2807` n `6`; index avg `0.0893` n `25`; metal avg `-0.3457` n `20`; unknown avg `0.0162` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
