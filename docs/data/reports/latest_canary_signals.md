# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T06:22:33.785380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `-0.0318` n `230`; crypto_major avg `-0.1874` n `8`; equity avg `-0.2324` n `92`; fx avg `-0.0312` n `6`; index avg `-0.0413` n `25`; metal avg `0.0506` n `20`; unknown avg `0.0268` n `766`
- 1h: commodity avg `-0.016` n `12`; crypto_alt avg `0.0621` n `230`; crypto_major avg `-0.1433` n `8`; equity avg `-0.1121` n `92`; fx avg `0.0145` n `6`; index avg `-0.0353` n `25`; metal avg `-0.0534` n `20`; unknown avg `-0.1152` n `750`
- 4h: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.4616` n `230`; crypto_major avg `-1.1054` n `8`; equity avg `-1.0833` n `92`; fx avg `0.0224` n `6`; index avg `-0.2434` n `25`; metal avg `-0.164` n `20`; unknown avg `-0.255` n `750`
- 24h: commodity avg `0.1779` n `12`; crypto_alt avg `-1.1691` n `230`; crypto_major avg `-0.8902` n `8`; equity avg `-2.4731` n `92`; fx avg `0.038` n `6`; index avg `-0.5506` n `25`; metal avg `-0.4658` n `20`; unknown avg `-0.1138` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
