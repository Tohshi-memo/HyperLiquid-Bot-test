# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T21:37:23.729416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `0.203` n `239`; crypto_major avg `0.1286` n `8`; equity avg `0.0834` n `162`; fx avg `0.0` n `6`; index avg `0.0092` n `27`; metal avg `0.0082` n `20`; unknown avg `16.7157` n `1263`
- 1h: commodity avg `-0.0461` n `13`; crypto_alt avg `-0.4156` n `239`; crypto_major avg `-0.191` n `8`; equity avg `0.1054` n `162`; fx avg `0.0118` n `6`; index avg `0.008` n `27`; metal avg `-0.0184` n `20`; unknown avg `15.433` n `1245`
- 4h: commodity avg `0.0291` n `13`; crypto_alt avg `0.6582` n `239`; crypto_major avg `0.8973` n `8`; equity avg `0.5511` n `162`; fx avg `0.0636` n `6`; index avg `0.061` n `27`; metal avg `0.085` n `20`; unknown avg `20.4999` n `1233`
- 24h: commodity avg `0.0534` n `13`; crypto_alt avg `2.6613` n `239`; crypto_major avg `3.0414` n `8`; equity avg `1.2564` n `162`; fx avg `0.046` n `6`; index avg `0.1185` n `27`; metal avg `0.2999` n `20`; unknown avg `33.9976` n `1154`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
