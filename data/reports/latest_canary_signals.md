# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T06:52:25.507396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.0282` n `234`; crypto_major avg `-0.0308` n `8`; equity avg `0.0237` n `141`; fx avg `0.0007` n `6`; index avg `0.0014` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.1224` n `961`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.1832` n `234`; crypto_major avg `0.108` n `8`; equity avg `0.0454` n `141`; fx avg `-0.0029` n `6`; index avg `0.0059` n `26`; metal avg `0.0032` n `20`; unknown avg `-0.2174` n `939`
- 4h: commodity avg `0.0384` n `12`; crypto_alt avg `0.4174` n `234`; crypto_major avg `0.0921` n `8`; equity avg `0.0601` n `141`; fx avg `0.0119` n `6`; index avg `0.0161` n `26`; metal avg `-0.011` n `20`; unknown avg `23.0456` n `933`
- 24h: commodity avg `0.0179` n `12`; crypto_alt avg `0.9209` n `234`; crypto_major avg `0.1921` n `8`; equity avg `0.2913` n `141`; fx avg `0.0191` n `6`; index avg `0.0074` n `26`; metal avg `-0.018` n `20`; unknown avg `4.6869` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
