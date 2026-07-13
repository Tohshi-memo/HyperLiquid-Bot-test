# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T13:22:30.201842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1753` n `12`; crypto_alt avg `-0.1184` n `230`; crypto_major avg `-0.1695` n `8`; equity avg `-0.095` n `92`; fx avg `-0.008` n `6`; index avg `-0.0141` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.0119` n `766`
- 1h: commodity avg `-0.2495` n `12`; crypto_alt avg `-0.2828` n `230`; crypto_major avg `-0.539` n `8`; equity avg `-0.1082` n `92`; fx avg `-0.0259` n `6`; index avg `0.046` n `25`; metal avg `0.085` n `20`; unknown avg `-0.0522` n `766`
- 4h: commodity avg `0.0931` n `12`; crypto_alt avg `-0.4219` n `230`; crypto_major avg `-0.8969` n `8`; equity avg `-0.2335` n `92`; fx avg `-0.0284` n `6`; index avg `-0.0252` n `25`; metal avg `-0.031` n `20`; unknown avg `0.098` n `766`
- 24h: commodity avg `-0.2405` n `12`; crypto_alt avg `-1.6003` n `230`; crypto_major avg `-2.3067` n `8`; equity avg `-2.2571` n `92`; fx avg `-0.0603` n `6`; index avg `-0.4158` n `25`; metal avg `-0.1733` n `20`; unknown avg `-0.2365` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
