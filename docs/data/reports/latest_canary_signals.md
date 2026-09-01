# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T17:52:26.155509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0383` n `12`; crypto_alt avg `-0.4171` n `232`; crypto_major avg `-0.4525` n `8`; equity avg `-0.0972` n `131`; fx avg `0.0115` n `6`; index avg `-0.0182` n `26`; metal avg `-0.046` n `20`; unknown avg `-0.4238` n `793`
- 1h: commodity avg `0.1581` n `12`; crypto_alt avg `-0.0478` n `232`; crypto_major avg `-0.2517` n `8`; equity avg `-0.1552` n `131`; fx avg `0.0181` n `6`; index avg `-0.0427` n `26`; metal avg `-0.1263` n `20`; unknown avg `-0.5981` n `791`
- 4h: commodity avg `0.4939` n `12`; crypto_alt avg `-0.6357` n `232`; crypto_major avg `-0.9006` n `8`; equity avg `-0.0167` n `131`; fx avg `-0.0007` n `6`; index avg `-0.0652` n `26`; metal avg `-0.1223` n `20`; unknown avg `-1.1575` n `790`
- 24h: commodity avg `0.7604` n `12`; crypto_alt avg `-0.2703` n `232`; crypto_major avg `-1.7872` n `8`; equity avg `-1.5322` n `130`; fx avg `0.0509` n `6`; index avg `-0.2744` n `26`; metal avg `-0.6911` n `20`; unknown avg `-0.4811` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0372`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0359`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0352`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0349`, n `668`, weak_sample_signal
