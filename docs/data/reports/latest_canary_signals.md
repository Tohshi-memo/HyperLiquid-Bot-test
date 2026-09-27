# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T06:22:24.022046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.1519` n `234`; crypto_major avg `0.0941` n `8`; equity avg `0.0137` n `141`; fx avg `-0.0029` n `6`; index avg `0.0016` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.0266` n `961`
- 1h: commodity avg `0.0244` n `12`; crypto_alt avg `0.3688` n `234`; crypto_major avg `0.4409` n `8`; equity avg `0.029` n `141`; fx avg `-0.0029` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0021` n `20`; unknown avg `2.0961` n `939`
- 4h: commodity avg `0.0821` n `12`; crypto_alt avg `0.1381` n `234`; crypto_major avg `-0.0088` n `8`; equity avg `0.0415` n `141`; fx avg `0.0108` n `6`; index avg `0.0162` n `26`; metal avg `-0.0183` n `20`; unknown avg `2.9796` n `933`
- 24h: commodity avg `0.0223` n `12`; crypto_alt avg `1.0388` n `234`; crypto_major avg `0.2757` n `8`; equity avg `0.2884` n `141`; fx avg `0.0309` n `6`; index avg `0.0025` n `26`; metal avg `-0.0192` n `20`; unknown avg `4.9395` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
