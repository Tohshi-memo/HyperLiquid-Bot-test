# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T06:22:32.986238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0026` n `12`; crypto_alt avg `-0.1096` n `233`; crypto_major avg `-0.1995` n `8`; equity avg `-0.0511` n `136`; fx avg `0.0146` n `6`; index avg `-0.0035` n `27`; metal avg `-0.0189` n `20`; unknown avg `0.5097` n `878`
- 1h: commodity avg `-0.0605` n `12`; crypto_alt avg `0.403` n `233`; crypto_major avg `0.2654` n `8`; equity avg `0.0239` n `136`; fx avg `0.0142` n `6`; index avg `0.0268` n `27`; metal avg `0.0028` n `20`; unknown avg `0.238` n `850`
- 4h: commodity avg `-0.0366` n `12`; crypto_alt avg `0.4657` n `233`; crypto_major avg `0.8792` n `8`; equity avg `-0.2597` n `136`; fx avg `-0.0214` n `6`; index avg `-0.0487` n `27`; metal avg `-0.0954` n `20`; unknown avg `8.2913` n `838`
- 24h: commodity avg `0.519` n `12`; crypto_alt avg `-0.2379` n `233`; crypto_major avg `0.3142` n `8`; equity avg `-1.3354` n `136`; fx avg `0.0451` n `6`; index avg `-0.2871` n `26`; metal avg `-0.1502` n `20`; unknown avg `1.8883` n `660`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
