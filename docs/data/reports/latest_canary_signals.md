# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T04:22:30.159649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `0.0306` n `233`; crypto_major avg `-0.0781` n `8`; equity avg `-0.1488` n `136`; fx avg `0.0141` n `6`; index avg `-0.0432` n `27`; metal avg `-0.0174` n `20`; unknown avg `0.3584` n `908`
- 1h: commodity avg `0.0559` n `12`; crypto_alt avg `0.0699` n `233`; crypto_major avg `-0.0301` n `8`; equity avg `-0.2707` n `136`; fx avg `0.0` n `6`; index avg `-0.0744` n `27`; metal avg `-0.0553` n `20`; unknown avg `0.1614` n `898`
- 4h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.554` n `233`; crypto_major avg `-0.3974` n `8`; equity avg `-0.2893` n `136`; fx avg `0.0555` n `6`; index avg `-0.0658` n `27`; metal avg `0.2057` n `20`; unknown avg `-0.2082` n `890`
- 24h: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.9042` n `233`; crypto_major avg `0.1215` n `8`; equity avg `-0.3212` n `136`; fx avg `0.1246` n `6`; index avg `-0.068` n `27`; metal avg `-0.2633` n `20`; unknown avg `4.976` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
