# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T06:52:35.861507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `12`; crypto_alt avg `0.0183` n `230`; crypto_major avg `0.0151` n `8`; equity avg `-0.0292` n `108`; fx avg `0.0292` n `6`; index avg `-0.0051` n `25`; metal avg `-0.025` n `20`; unknown avg `-0.0008` n `782`
- 1h: commodity avg `0.1567` n `12`; crypto_alt avg `0.2016` n `230`; crypto_major avg `-0.1453` n `8`; equity avg `-0.1217` n `108`; fx avg `0.099` n `6`; index avg `-0.0139` n `25`; metal avg `-0.134` n `20`; unknown avg `0.0248` n `750`
- 4h: commodity avg `0.024` n `12`; crypto_alt avg `0.4667` n `230`; crypto_major avg `0.3429` n `8`; equity avg `-0.3592` n `108`; fx avg `0.0649` n `6`; index avg `-0.0681` n `25`; metal avg `-0.2259` n `20`; unknown avg `0.0025` n `750`
- 24h: commodity avg `0.0783` n `12`; crypto_alt avg `0.1355` n `230`; crypto_major avg `-0.1452` n `8`; equity avg `-2.1913` n `108`; fx avg `0.0425` n `6`; index avg `-0.4176` n `25`; metal avg `0.0733` n `20`; unknown avg `0.8607` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
