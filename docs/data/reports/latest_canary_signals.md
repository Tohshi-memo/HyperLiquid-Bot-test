# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T16:07:28.125327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0271` n `12`; crypto_alt avg `0.0637` n `230`; crypto_major avg `-0.0763` n `8`; equity avg `-0.0761` n `92`; fx avg `-0.0017` n `6`; index avg `-0.0211` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0037` n `766`
- 1h: commodity avg `0.116` n `12`; crypto_alt avg `-0.4166` n `230`; crypto_major avg `-0.3917` n `8`; equity avg `-0.4929` n `92`; fx avg `-0.0062` n `6`; index avg `-0.111` n `25`; metal avg `-0.0309` n `20`; unknown avg `-0.0875` n `766`
- 4h: commodity avg `0.1643` n `12`; crypto_alt avg `-0.1954` n `230`; crypto_major avg `-0.49` n `8`; equity avg `-0.3799` n `92`; fx avg `-0.0319` n `6`; index avg `-0.0194` n `25`; metal avg `-0.1503` n `20`; unknown avg `-0.063` n `766`
- 24h: commodity avg `0.1474` n `12`; crypto_alt avg `-1.573` n `230`; crypto_major avg `-2.524` n `8`; equity avg `-2.4718` n `92`; fx avg `-0.0687` n `6`; index avg `-0.5263` n `25`; metal avg `-0.4062` n `20`; unknown avg `-0.1682` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
