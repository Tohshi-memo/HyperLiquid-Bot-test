# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T00:37:31.960235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0491` n `12`; crypto_alt avg `-0.7263` n `234`; crypto_major avg `-0.7873` n `8`; equity avg `-0.3652` n `141`; fx avg `0.0112` n `6`; index avg `-0.0529` n `26`; metal avg `-0.1019` n `20`; unknown avg `26.5251` n `962`
- 1h: commodity avg `-0.1125` n `12`; crypto_alt avg `0.0668` n `234`; crypto_major avg `-0.162` n `8`; equity avg `-0.199` n `141`; fx avg `0.0803` n `6`; index avg `0.0286` n `26`; metal avg `-0.1542` n `20`; unknown avg `50.123` n `954`
- 4h: commodity avg `-0.391` n `12`; crypto_alt avg `-0.048` n `234`; crypto_major avg `-0.5097` n `8`; equity avg `-0.572` n `141`; fx avg `0.0749` n `6`; index avg `-0.0514` n `26`; metal avg `-0.3377` n `20`; unknown avg `3.1258` n `886`
- 24h: commodity avg `-0.4511` n `12`; crypto_alt avg `0.7903` n `234`; crypto_major avg `-0.2299` n `8`; equity avg `-0.2613` n `141`; fx avg `0.0565` n `6`; index avg `-0.0089` n `26`; metal avg `-0.3494` n `20`; unknown avg `11.8029` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
