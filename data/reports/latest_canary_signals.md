# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T18:09:47.020704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `13`; crypto_alt avg `0.2771` n `239`; crypto_major avg `0.2083` n `8`; equity avg `0.2366` n `158`; fx avg `0.0069` n `6`; index avg `0.0294` n `27`; metal avg `0.0386` n `20`; unknown avg `0.6616` n `1219`
- 1h: commodity avg `0.0965` n `13`; crypto_alt avg `0.05` n `239`; crypto_major avg `0.1435` n `8`; equity avg `0.1356` n `158`; fx avg `0.0068` n `6`; index avg `0.0232` n `27`; metal avg `0.0037` n `20`; unknown avg `0.7351` n `1219`
- 4h: commodity avg `0.0966` n `13`; crypto_alt avg `0.444` n `239`; crypto_major avg `0.729` n `8`; equity avg `0.7803` n `158`; fx avg `0.0736` n `6`; index avg `0.0471` n `27`; metal avg `-0.1772` n `20`; unknown avg `0.4953` n `1215`
- 24h: commodity avg `0.285` n `13`; crypto_alt avg `0.8257` n `239`; crypto_major avg `1.4597` n `8`; equity avg `0.1828` n `158`; fx avg `0.0745` n `6`; index avg `-0.0092` n `27`; metal avg `-0.5825` n `20`; unknown avg `374.6326` n `1049`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
