# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T06:07:30.619818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.0091` n `232`; crypto_major avg `-0.0155` n `8`; equity avg `0.1097` n `133`; fx avg `-0.0506` n `6`; index avg `0.0277` n `26`; metal avg `0.0226` n `20`; unknown avg `-0.0253` n `756`
- 1h: commodity avg `-0.1276` n `12`; crypto_alt avg `-0.1801` n `232`; crypto_major avg `-0.1481` n `8`; equity avg `-0.0637` n `133`; fx avg `-0.0831` n `6`; index avg `-0.0006` n `26`; metal avg `0.0411` n `20`; unknown avg `15.0763` n `756`
- 4h: commodity avg `-0.276` n `12`; crypto_alt avg `0.7083` n `232`; crypto_major avg `0.5452` n `8`; equity avg `0.0189` n `133`; fx avg `-0.0942` n `6`; index avg `-0.0103` n `26`; metal avg `0.1088` n `20`; unknown avg `0.14` n `756`
- 24h: commodity avg `-0.0384` n `12`; crypto_alt avg `0.2827` n `232`; crypto_major avg `0.1499` n `8`; equity avg `1.1615` n `133`; fx avg `-0.3355` n `6`; index avg `0.1601` n `26`; metal avg `0.7546` n `20`; unknown avg `-0.4683` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
