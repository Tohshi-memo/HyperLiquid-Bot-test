# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T12:21:03.777695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `0.0786` n `230`; crypto_major avg `0.1839` n `8`; equity avg `0.0013` n `92`; fx avg `0.0013` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0258` n `20`; unknown avg `0.0005` n `766`
- 1h: commodity avg `-0.0632` n `12`; crypto_alt avg `0.0588` n `230`; crypto_major avg `0.1087` n `8`; equity avg `-0.1851` n `92`; fx avg `0.0094` n `6`; index avg `-0.003` n `25`; metal avg `-0.0581` n `20`; unknown avg `0.0056` n `766`
- 4h: commodity avg `0.0161` n `12`; crypto_alt avg `0.0191` n `230`; crypto_major avg `0.3949` n `8`; equity avg `-0.3007` n `92`; fx avg `0.0435` n `6`; index avg `0.0391` n `25`; metal avg `-0.1053` n `20`; unknown avg `0.0817` n `766`
- 24h: commodity avg `1.1625` n `12`; crypto_alt avg `-0.6591` n `230`; crypto_major avg `-0.0759` n `8`; equity avg `-0.7888` n `92`; fx avg `-0.0284` n `6`; index avg `-0.0342` n `25`; metal avg `-0.2105` n `20`; unknown avg `-0.2788` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
