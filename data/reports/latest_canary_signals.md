# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T17:07:42.491596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.6804` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.4146` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5454` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2238` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1514` n `13`; crypto_alt avg `-0.1876` n `239`; crypto_major avg `-0.2873` n `8`; equity avg `0.226` n `166`; fx avg `-0.0066` n `6`; index avg `0.0207` n `27`; metal avg `0.0262` n `20`; unknown avg `0.1528` n `1258`
- 1h: commodity avg `0.3378` n `13`; crypto_alt avg `-0.7712` n `239`; crypto_major avg `-1.2507` n `8`; equity avg `-0.2956` n `166`; fx avg `-0.0565` n `6`; index avg `-0.0269` n `27`; metal avg `-0.0182` n `20`; unknown avg `180.5492` n `1264`
- 4h: commodity avg `-0.3804` n `13`; crypto_alt avg `2.1449` n `239`; crypto_major avg `2.0342` n `8`; equity avg `4.7146` n `166`; fx avg `-0.2013` n `6`; index avg `0.5439` n `27`; metal avg `0.4888` n `20`; unknown avg `9.3584` n `1254`
- 24h: commodity avg `-1.341` n `13`; crypto_alt avg `2.581` n `239`; crypto_major avg `2.9236` n `8`; equity avg `6.4216` n `166`; fx avg `-0.075` n `6`; index avg `0.5832` n `27`; metal avg `0.7463` n `20`; unknown avg `297.5685` n `1063`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
