# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T19:37:26.492852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0613` n `12`; crypto_alt avg `0.0108` n `233`; crypto_major avg `-0.0655` n `8`; equity avg `-0.1457` n `134`; fx avg `-0.0027` n `6`; index avg `-0.0014` n `26`; metal avg `-0.0233` n `20`; unknown avg `1.0052` n `797`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `-0.3208` n `233`; crypto_major avg `-0.3133` n `8`; equity avg `-0.4059` n `134`; fx avg `-0.0234` n `6`; index avg `-0.0604` n `26`; metal avg `-0.1483` n `20`; unknown avg `1.6501` n `795`
- 4h: commodity avg `0.1481` n `12`; crypto_alt avg `-0.7578` n `232`; crypto_major avg `0.0144` n `8`; equity avg `-0.4016` n `134`; fx avg `-0.0402` n `6`; index avg `-0.0485` n `26`; metal avg `-0.2175` n `20`; unknown avg `0.5781` n `765`
- 24h: commodity avg `-0.0684` n `12`; crypto_alt avg `-0.263` n `232`; crypto_major avg `-0.2176` n `8`; equity avg `0.4216` n `134`; fx avg `-0.0962` n `6`; index avg `-0.1185` n `26`; metal avg `-0.2387` n `20`; unknown avg `3.9846` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
