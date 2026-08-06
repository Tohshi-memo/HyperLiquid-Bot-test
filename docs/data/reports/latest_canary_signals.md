# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T01:22:29.621810+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1068` n `12`; crypto_alt avg `-0.1892` n `230`; crypto_major avg `-0.1463` n `8`; equity avg `-0.2746` n `108`; fx avg `0.0046` n `6`; index avg `-0.0392` n `25`; metal avg `-0.2196` n `20`; unknown avg `-0.1124` n `782`
- 1h: commodity avg `0.2027` n `12`; crypto_alt avg `-0.1156` n `230`; crypto_major avg `-0.3217` n `8`; equity avg `-0.6993` n `108`; fx avg `-0.0602` n `6`; index avg `-0.1495` n `25`; metal avg `-0.0266` n `20`; unknown avg `-0.1922` n `782`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `0.0248` n `230`; crypto_major avg `-0.3564` n `8`; equity avg `-0.7582` n `108`; fx avg `-0.0546` n `6`; index avg `-0.2` n `25`; metal avg `0.1337` n `20`; unknown avg `-0.0016` n `782`
- 24h: commodity avg `-0.0968` n `12`; crypto_alt avg `0.5184` n `230`; crypto_major avg `0.5265` n `8`; equity avg `-1.7351` n `108`; fx avg `-0.0453` n `6`; index avg `-0.3344` n `25`; metal avg `0.9712` n `20`; unknown avg `1.0511` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
