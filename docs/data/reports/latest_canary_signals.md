# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T19:52:37.203145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0339` n `12`; crypto_alt avg `-0.0981` n `234`; crypto_major avg `-0.0259` n `8`; equity avg `0.0018` n `141`; fx avg `0.0015` n `6`; index avg `0.0016` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.5024` n `962`
- 1h: commodity avg `-0.0231` n `12`; crypto_alt avg `-0.2442` n `234`; crypto_major avg `-0.1519` n `8`; equity avg `0.0136` n `141`; fx avg `0.0014` n `6`; index avg `0.0007` n `26`; metal avg `0.0019` n `20`; unknown avg `3.6612` n `934`
- 4h: commodity avg `0.0293` n `12`; crypto_alt avg `1.1267` n `234`; crypto_major avg `0.5497` n `8`; equity avg `0.1761` n `141`; fx avg `0.005` n `6`; index avg `0.0114` n `26`; metal avg `0.0117` n `20`; unknown avg `3.1374` n `928`
- 24h: commodity avg `-0.139` n `12`; crypto_alt avg `0.7609` n `234`; crypto_major avg `0.6058` n `8`; equity avg `0.3953` n `141`; fx avg `-0.0277` n `6`; index avg `0.0398` n `26`; metal avg `-0.0086` n `20`; unknown avg `118.6541` n `871`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
