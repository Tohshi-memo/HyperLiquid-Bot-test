# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T07:07:36.095507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0826` n `13`; crypto_alt avg `0.0392` n `239`; crypto_major avg `0.0448` n `8`; equity avg `-0.0751` n `166`; fx avg `-0.0049` n `6`; index avg `-0.0234` n `27`; metal avg `0.0422` n `20`; unknown avg `0.0569` n `1256`
- 1h: commodity avg `-0.1926` n `13`; crypto_alt avg `-0.0258` n `239`; crypto_major avg `-0.2192` n `8`; equity avg `-0.3533` n `166`; fx avg `-0.0342` n `6`; index avg `-0.058` n `27`; metal avg `-0.0086` n `20`; unknown avg `451.6067` n `1260`
- 4h: commodity avg `-0.1882` n `13`; crypto_alt avg `1.5048` n `239`; crypto_major avg `1.1437` n `8`; equity avg `1.0616` n `166`; fx avg `0.0105` n `6`; index avg `0.0381` n `27`; metal avg `0.36` n `20`; unknown avg `163.3744` n `1224`
- 24h: commodity avg `-0.5561` n `13`; crypto_alt avg `2.6831` n `239`; crypto_major avg `3.1805` n `8`; equity avg `2.4555` n `166`; fx avg `0.2022` n `6`; index avg `0.1428` n `27`; metal avg `0.6027` n `20`; unknown avg `340.4855` n `1017`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
