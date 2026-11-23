# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T07:22:31.128023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `0.0483` n `239`; crypto_major avg `0.0661` n `8`; equity avg `0.1585` n `166`; fx avg `0.0025` n `6`; index avg `0.0315` n `27`; metal avg `0.0606` n `20`; unknown avg `-0.0876` n `1264`
- 1h: commodity avg `-0.1799` n `13`; crypto_alt avg `0.3172` n `239`; crypto_major avg `0.1981` n `8`; equity avg `0.1888` n `166`; fx avg `-0.0265` n `6`; index avg `0.023` n `27`; metal avg `0.1889` n `20`; unknown avg `158.405` n `1260`
- 4h: commodity avg `-0.2419` n `13`; crypto_alt avg `0.4664` n `239`; crypto_major avg `-0.025` n `8`; equity avg `0.4807` n `166`; fx avg `0.0218` n `6`; index avg `-0.0591` n `27`; metal avg `0.2452` n `20`; unknown avg `-0.2986` n `1230`
- 24h: commodity avg `-0.5594` n `13`; crypto_alt avg `2.7361` n `239`; crypto_major avg `3.2213` n `8`; equity avg `2.6242` n `166`; fx avg `0.2181` n `6`; index avg `0.1716` n `27`; metal avg `0.6624` n `20`; unknown avg `338.4064` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
