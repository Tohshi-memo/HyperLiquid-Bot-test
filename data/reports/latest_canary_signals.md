# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T09:07:30.521679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.3459` n `234`; crypto_major avg `-0.3011` n `8`; equity avg `-0.0216` n `141`; fx avg `-0.0018` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.4602` n `959`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `-0.4914` n `234`; crypto_major avg `-0.3861` n `8`; equity avg `0.0133` n `141`; fx avg `-0.0082` n `6`; index avg `0.0145` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.4502` n `959`
- 4h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.9347` n `234`; crypto_major avg `0.8831` n `8`; equity avg `0.1514` n `141`; fx avg `-0.0128` n `6`; index avg `0.0269` n `26`; metal avg `-0.0017` n `20`; unknown avg `1.7533` n `923`
- 24h: commodity avg `0.0319` n `12`; crypto_alt avg `0.9434` n `234`; crypto_major avg `0.5141` n `8`; equity avg `0.3423` n `141`; fx avg `-0.0084` n `6`; index avg `0.0322` n `26`; metal avg `-0.0141` n `20`; unknown avg `6.458` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
