# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T07:07:30.153522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.1285` n `234`; crypto_major avg `-0.0267` n `8`; equity avg `0.003` n `141`; fx avg `-0.0022` n `6`; index avg `-0.0002` n `26`; metal avg `0.0033` n `20`; unknown avg `2.092` n `959`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.3267` n `234`; crypto_major avg `0.0029` n `8`; equity avg `0.0374` n `141`; fx avg `-0.0051` n `6`; index avg `0.0051` n `26`; metal avg `0.0097` n `20`; unknown avg `-0.0032` n `959`
- 4h: commodity avg `0.0316` n `12`; crypto_alt avg `0.5881` n `234`; crypto_major avg `0.041` n `8`; equity avg `0.051` n `141`; fx avg `0.0097` n `6`; index avg `0.0147` n `26`; metal avg `-0.0082` n `20`; unknown avg `24.5015` n `933`
- 24h: commodity avg `0.0771` n `12`; crypto_alt avg `0.8191` n `234`; crypto_major avg `0.0374` n `8`; equity avg `0.288` n `141`; fx avg `0.0181` n `6`; index avg `0.0073` n `26`; metal avg `-0.0146` n `20`; unknown avg `4.815` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
