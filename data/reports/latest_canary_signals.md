# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T18:22:28.254109+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0472` n `12`; crypto_alt avg `0.0784` n `233`; crypto_major avg `0.2153` n `8`; equity avg `-0.1136` n `136`; fx avg `0.0025` n `6`; index avg `-0.0116` n `27`; metal avg `0.0016` n `20`; unknown avg `0.0979` n `908`
- 1h: commodity avg `-0.0575` n `12`; crypto_alt avg `0.4114` n `233`; crypto_major avg `0.6612` n `8`; equity avg `0.0079` n `136`; fx avg `0.0012` n `6`; index avg `0.0092` n `27`; metal avg `0.0053` n `20`; unknown avg `0.0324` n `906`
- 4h: commodity avg `-0.3501` n `12`; crypto_alt avg `1.2162` n `233`; crypto_major avg `1.396` n `8`; equity avg `0.6903` n `136`; fx avg `0.0046` n `6`; index avg `0.1343` n `27`; metal avg `0.2582` n `20`; unknown avg `0.1881` n `864`
- 24h: commodity avg `0.2688` n `12`; crypto_alt avg `0.3187` n `233`; crypto_major avg `2.2922` n `8`; equity avg `-0.2362` n `136`; fx avg `0.0711` n `6`; index avg `-0.1293` n `27`; metal avg `-0.306` n `20`; unknown avg `1.3568` n `688`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
