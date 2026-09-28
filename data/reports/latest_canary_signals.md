# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T15:22:32.069741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.2484` n `234`; crypto_major avg `-0.0667` n `8`; equity avg `-0.1936` n `141`; fx avg `0.0097` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.9092` n `962`
- 1h: commodity avg `0.1778` n `12`; crypto_alt avg `-1.646` n `234`; crypto_major avg `-1.0538` n `8`; equity avg `-0.955` n `141`; fx avg `0.0426` n `6`; index avg `-0.1529` n `26`; metal avg `-0.1404` n `20`; unknown avg `2.4422` n `950`
- 4h: commodity avg `-0.0542` n `12`; crypto_alt avg `-1.3183` n `234`; crypto_major avg `-0.6676` n `8`; equity avg `-1.2184` n `141`; fx avg `0.058` n `6`; index avg `-0.1605` n `26`; metal avg `-0.2126` n `20`; unknown avg `47.6441` n `904`
- 24h: commodity avg `-0.0554` n `12`; crypto_alt avg `-3.8062` n `234`; crypto_major avg `-2.4607` n `8`; equity avg `-3.7421` n `141`; fx avg `0.0694` n `6`; index avg `-0.3966` n `26`; metal avg `-1.092` n `20`; unknown avg `5.5973` n `786`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2005`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
