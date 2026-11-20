# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T06:37:25.863822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0838` n `13`; crypto_alt avg `-0.0522` n `239`; crypto_major avg `-0.0631` n `8`; equity avg `-0.1224` n `165`; fx avg `-0.0144` n `6`; index avg `-0.0215` n `27`; metal avg `-0.0756` n `20`; unknown avg `0.4535` n `1260`
- 1h: commodity avg `-0.063` n `13`; crypto_alt avg `0.4649` n `239`; crypto_major avg `0.5602` n `8`; equity avg `0.2282` n `165`; fx avg `0.0192` n `6`; index avg `0.0359` n `27`; metal avg `0.4111` n `20`; unknown avg `0.11` n `1238`
- 4h: commodity avg `-0.0767` n `13`; crypto_alt avg `0.3253` n `239`; crypto_major avg `0.5467` n `8`; equity avg `-0.3813` n `165`; fx avg `0.0134` n `6`; index avg `-0.053` n `27`; metal avg `0.076` n `20`; unknown avg `163.9795` n `1220`
- 24h: commodity avg `-0.154` n `13`; crypto_alt avg `-3.0751` n `239`; crypto_major avg `-2.5753` n `8`; equity avg `-6.6013` n `165`; fx avg `0.0419` n `6`; index avg `-0.6112` n `27`; metal avg `-1.535` n `20`; unknown avg `222.3548` n `1167`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
