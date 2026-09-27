# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T04:52:26.835721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `-0.1606` n `234`; crypto_major avg `-0.1363` n `8`; equity avg `-0.0196` n `141`; fx avg `0.0106` n `6`; index avg `0.0062` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.0978` n `961`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.5418` n `234`; crypto_major avg `-0.3061` n `8`; equity avg `-0.0011` n `141`; fx avg `0.0074` n `6`; index avg `0.011` n `26`; metal avg `-0.0093` n `20`; unknown avg `103.6639` n `953`
- 4h: commodity avg `0.0806` n `12`; crypto_alt avg `-0.4293` n `234`; crypto_major avg `-0.2487` n `8`; equity avg `0.04` n `141`; fx avg `-0.0019` n `6`; index avg `0.0197` n `26`; metal avg `-0.0173` n `20`; unknown avg `0.0244` n `949`
- 24h: commodity avg `0.0002` n `12`; crypto_alt avg `0.0477` n `234`; crypto_major avg `-0.65` n `8`; equity avg `0.2312` n `141`; fx avg `0.0141` n `6`; index avg `0.0094` n `26`; metal avg `-0.0145` n `20`; unknown avg `4.5189` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
