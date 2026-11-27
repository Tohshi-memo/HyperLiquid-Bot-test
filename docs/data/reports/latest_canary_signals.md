# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T01:07:23.131650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `0.1237` n `239`; crypto_major avg `0.1374` n `8`; equity avg `0.2999` n `168`; fx avg `-0.0063` n `6`; index avg `0.0399` n `27`; metal avg `0.1589` n `20`; unknown avg `1.0162` n `1249`
- 1h: commodity avg `0.0427` n `13`; crypto_alt avg `0.3425` n `239`; crypto_major avg `0.3751` n `8`; equity avg `0.1982` n `168`; fx avg `-0.0639` n `6`; index avg `0.0032` n `27`; metal avg `0.0985` n `20`; unknown avg `72.3364` n `1253`
- 4h: commodity avg `0.1008` n `13`; crypto_alt avg `0.0033` n `239`; crypto_major avg `-0.2372` n `8`; equity avg `0.0362` n `168`; fx avg `-0.0246` n `6`; index avg `0.0203` n `27`; metal avg `0.0488` n `20`; unknown avg `60.8351` n `1201`
- 24h: commodity avg `0.1161` n `13`; crypto_alt avg `0.8719` n `239`; crypto_major avg `0.555` n `8`; equity avg `0.007` n `168`; fx avg `-0.0086` n `6`; index avg `-0.0139` n `27`; metal avg `0.1893` n `20`; unknown avg `208.4952` n `997`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
