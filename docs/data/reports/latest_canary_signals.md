# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T05:07:28.226709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `13`; crypto_alt avg `-0.0182` n `239`; crypto_major avg `-0.0287` n `8`; equity avg `-0.1531` n `166`; fx avg `0.0048` n `6`; index avg `-0.0299` n `27`; metal avg `-0.0515` n `20`; unknown avg `-0.0837` n `1254`
- 1h: commodity avg `-0.013` n `13`; crypto_alt avg `0.0839` n `239`; crypto_major avg `-0.0575` n `8`; equity avg `-0.1918` n `166`; fx avg `-0.0064` n `6`; index avg `0.0018` n `27`; metal avg `0.0113` n `20`; unknown avg `19.1198` n `1260`
- 4h: commodity avg `0.0468` n `13`; crypto_alt avg `0.6136` n `239`; crypto_major avg `0.5419` n `8`; equity avg `0.3722` n `166`; fx avg `0.0783` n `6`; index avg `-0.0659` n `27`; metal avg `-0.0019` n `20`; unknown avg `163.866` n `1239`
- 24h: commodity avg `-0.3171` n `13`; crypto_alt avg `1.9637` n `239`; crypto_major avg `2.6963` n `8`; equity avg `1.9919` n `166`; fx avg `0.2224` n `6`; index avg `0.1596` n `27`; metal avg `0.3849` n `20`; unknown avg `293.8228` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
