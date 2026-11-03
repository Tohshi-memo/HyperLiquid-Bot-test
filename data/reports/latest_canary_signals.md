# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T15:22:57.499876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1351` n `13`; crypto_alt avg `-0.2354` n `239`; crypto_major avg `-0.1037` n `8`; equity avg `0.0151` n `157`; fx avg `-0.0111` n `6`; index avg `-0.0035` n `27`; metal avg `-0.0844` n `20`; unknown avg `27.2392` n `1264`
- 1h: commodity avg `0.1728` n `13`; crypto_alt avg `-0.0585` n `239`; crypto_major avg `0.044` n `8`; equity avg `0.5999` n `157`; fx avg `0.034` n `6`; index avg `0.0208` n `27`; metal avg `-0.1648` n `20`; unknown avg `0.9692` n `1258`
- 4h: commodity avg `-0.5525` n `13`; crypto_alt avg `0.4718` n `239`; crypto_major avg `0.7773` n `8`; equity avg `1.2927` n `157`; fx avg `0.0252` n `6`; index avg `0.1443` n `27`; metal avg `0.1922` n `20`; unknown avg `20.2298` n `1248`
- 24h: commodity avg `-0.2531` n `13`; crypto_alt avg `-0.8619` n `239`; crypto_major avg `-0.2114` n `8`; equity avg `-1.4731` n `157`; fx avg `0.0229` n `6`; index avg `-0.1776` n `27`; metal avg `-0.5905` n `20`; unknown avg `0.0049` n `1020`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
