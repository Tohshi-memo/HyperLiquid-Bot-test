# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T21:37:31.061923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.3383` n `234`; crypto_major avg `-0.3675` n `8`; equity avg `-0.0066` n `141`; fx avg `0.0091` n `6`; index avg `0.0074` n `26`; metal avg `0.0034` n `20`; unknown avg `1.6944` n `964`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.2202` n `234`; crypto_major avg `-0.3177` n `8`; equity avg `-0.0048` n `141`; fx avg `-0.0296` n `6`; index avg `0.0099` n `26`; metal avg `0.0003` n `20`; unknown avg `2.4552` n `926`
- 4h: commodity avg `0.0466` n `12`; crypto_alt avg `0.1344` n `234`; crypto_major avg `-0.0692` n `8`; equity avg `0.0729` n `141`; fx avg `-0.0412` n `6`; index avg `0.0194` n `26`; metal avg `0.0025` n `20`; unknown avg `1.7523` n `894`
- 24h: commodity avg `-0.1359` n `12`; crypto_alt avg `0.6049` n `234`; crypto_major avg `0.0141` n `8`; equity avg `0.3815` n `141`; fx avg `-0.0505` n `6`; index avg `0.0604` n `26`; metal avg `-0.0188` n `20`; unknown avg `9.3135` n `837`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
