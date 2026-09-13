# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T00:52:32.381881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.0054` n `233`; crypto_major avg `-0.0015` n `8`; equity avg `0.0028` n `136`; fx avg `-0.0005` n `6`; index avg `0.0` n `26`; metal avg `-0.0002` n `20`; unknown avg `2.7724` n `838`
- 1h: commodity avg `0.0281` n `12`; crypto_alt avg `0.1715` n `233`; crypto_major avg `-0.1254` n `8`; equity avg `-0.0177` n `136`; fx avg `0.0041` n `6`; index avg `-0.008` n `26`; metal avg `0.005` n `20`; unknown avg `52.5369` n `830`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `0.2557` n `233`; crypto_major avg `0.0097` n `8`; equity avg `-0.0462` n `136`; fx avg `0.0023` n `6`; index avg `-0.0126` n `26`; metal avg `-0.016` n `20`; unknown avg `11.9597` n `796`
- 24h: commodity avg `-0.019` n `12`; crypto_alt avg `1.1554` n `233`; crypto_major avg `0.3017` n `8`; equity avg `-0.3861` n `136`; fx avg `0.0042` n `6`; index avg `-0.0402` n `26`; metal avg `0.0001` n `20`; unknown avg `10.6649` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0429`, n `668`, weak_sample_signal
