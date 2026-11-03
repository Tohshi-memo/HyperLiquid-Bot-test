# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T09:37:29.925715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0434` n `13`; crypto_alt avg `-0.031` n `239`; crypto_major avg `0.0866` n `8`; equity avg `0.0346` n `157`; fx avg `0.0143` n `6`; index avg `-0.0131` n `27`; metal avg `0.0451` n `20`; unknown avg `6.0613` n `1264`
- 1h: commodity avg `0.0282` n `13`; crypto_alt avg `0.6214` n `239`; crypto_major avg `0.5997` n `8`; equity avg `0.6878` n `157`; fx avg `0.0267` n `6`; index avg `0.0561` n `27`; metal avg `0.0035` n `20`; unknown avg `0.3857` n `1248`
- 4h: commodity avg `0.3887` n `13`; crypto_alt avg `0.281` n `239`; crypto_major avg `0.4813` n `8`; equity avg `0.8456` n `157`; fx avg `0.0693` n `6`; index avg `0.0805` n `27`; metal avg `-0.1957` n `20`; unknown avg `0.5578` n `1210`
- 24h: commodity avg `-0.2244` n `13`; crypto_alt avg `-1.8212` n `238`; crypto_major avg `-1.1647` n `8`; equity avg `-3.6774` n `157`; fx avg `0.0095` n `6`; index avg `-0.2751` n `27`; metal avg `-0.4826` n `20`; unknown avg `4.0564` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
