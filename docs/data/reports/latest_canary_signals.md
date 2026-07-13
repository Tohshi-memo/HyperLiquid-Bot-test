# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T14:52:30.892767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0502` n `12`; crypto_alt avg `0.1095` n `230`; crypto_major avg `0.1462` n `8`; equity avg `-0.1493` n `92`; fx avg `-0.0112` n `6`; index avg `-0.0255` n `25`; metal avg `0.038` n `20`; unknown avg `-0.004` n `766`
- 1h: commodity avg `0.1083` n `12`; crypto_alt avg `0.5481` n `230`; crypto_major avg `0.626` n `8`; equity avg `0.5317` n `92`; fx avg `-0.0205` n `6`; index avg `0.0805` n `25`; metal avg `-0.1809` n `20`; unknown avg `0.2257` n `766`
- 4h: commodity avg `0.0299` n `12`; crypto_alt avg `-0.0628` n `230`; crypto_major avg `-0.2847` n `8`; equity avg `-0.2379` n `92`; fx avg `-0.0235` n `6`; index avg `0.0432` n `25`; metal avg `-0.1684` n `20`; unknown avg `0.0696` n `766`
- 24h: commodity avg `-0.0115` n `12`; crypto_alt avg `-1.2506` n `230`; crypto_major avg `-2.1545` n `8`; equity avg `-2.2901` n `92`; fx avg `-0.0816` n `6`; index avg `-0.4293` n `25`; metal avg `-0.4103` n `20`; unknown avg `-0.1114` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
