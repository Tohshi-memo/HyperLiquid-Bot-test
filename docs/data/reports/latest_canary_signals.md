# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T22:40:58.650834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0512` n `12`; crypto_alt avg `-0.1417` n `230`; crypto_major avg `-0.1654` n `8`; equity avg `-0.06` n `92`; fx avg `-0.0312` n `6`; index avg `0.0052` n `25`; metal avg `-0.0103` n `20`; unknown avg `-0.1093` n `766`
- 1h: commodity avg `0.0726` n `12`; crypto_alt avg `0.3751` n `230`; crypto_major avg `0.4181` n `8`; equity avg `0.0268` n `92`; fx avg `-0.0405` n `6`; index avg `0.0208` n `25`; metal avg `0.0238` n `20`; unknown avg `-0.0191` n `766`
- 4h: commodity avg `0.0935` n `12`; crypto_alt avg `-0.373` n `230`; crypto_major avg `-0.0018` n `8`; equity avg `0.0192` n `92`; fx avg `-0.0393` n `6`; index avg `-0.0443` n `25`; metal avg `0.0342` n `20`; unknown avg `-0.3448` n `766`
- 24h: commodity avg `0.9018` n `12`; crypto_alt avg `-1.8961` n `230`; crypto_major avg `-2.3305` n `8`; equity avg `-2.9854` n `92`; fx avg `-0.0589` n `6`; index avg `-0.5744` n `25`; metal avg `-0.2895` n `20`; unknown avg `-0.3777` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
