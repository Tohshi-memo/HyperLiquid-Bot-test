# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T10:07:29.702456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.146` n `13`; crypto_alt avg `-0.0363` n `239`; crypto_major avg `0.0102` n `8`; equity avg `-0.0001` n `164`; fx avg `-0.0014` n `6`; index avg `-0.0146` n `27`; metal avg `0.0359` n `20`; unknown avg `0.6803` n `1260`
- 1h: commodity avg `0.137` n `13`; crypto_alt avg `-0.028` n `239`; crypto_major avg `-0.0144` n `8`; equity avg `0.0781` n `164`; fx avg `-0.0087` n `6`; index avg `0.0789` n `27`; metal avg `0.0063` n `20`; unknown avg `0.8309` n `1260`
- 4h: commodity avg `0.0525` n `13`; crypto_alt avg `0.6415` n `239`; crypto_major avg `0.49` n `8`; equity avg `1.0715` n `164`; fx avg `0.0816` n `6`; index avg `0.2223` n `27`; metal avg `0.0005` n `20`; unknown avg `265.5111` n `1218`
- 24h: commodity avg `0.2945` n `13`; crypto_alt avg `0.149` n `239`; crypto_major avg `-0.5336` n `8`; equity avg `0.0815` n `164`; fx avg `0.0251` n `6`; index avg `0.2147` n `27`; metal avg `-0.1701` n `20`; unknown avg `3.5715` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
