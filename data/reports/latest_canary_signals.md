# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T07:22:39.699291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.084` n `13`; crypto_alt avg `0.1881` n `239`; crypto_major avg `0.2655` n `8`; equity avg `0.1416` n `157`; fx avg `0.0149` n `6`; index avg `0.0096` n `27`; metal avg `0.0213` n `20`; unknown avg `18.9131` n `1264`
- 1h: commodity avg `0.2188` n `13`; crypto_alt avg `-0.0387` n `239`; crypto_major avg `0.2384` n `8`; equity avg `0.0747` n `157`; fx avg `0.005` n `6`; index avg `-0.016` n `27`; metal avg `-0.0757` n `20`; unknown avg `0.1377` n `1250`
- 4h: commodity avg `0.3634` n `13`; crypto_alt avg `-0.2336` n `239`; crypto_major avg `-0.0066` n `8`; equity avg `-0.9336` n `157`; fx avg `0.0461` n `6`; index avg `-0.1581` n `27`; metal avg `-0.3406` n `20`; unknown avg `0.0243` n `1164`
- 24h: commodity avg `-0.5123` n `13`; crypto_alt avg `-2.6075` n `238`; crypto_major avg `-1.4628` n `8`; equity avg `-4.5168` n `157`; fx avg `-0.0165` n `6`; index avg `-0.3583` n `27`; metal avg `-0.4831` n `20`; unknown avg `8.2639` n `949`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
