# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T16:52:26.584279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2633` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1342` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0253` n `12`; crypto_alt avg `0.0424` n `229`; crypto_major avg `0.1006` n `8`; equity avg `-0.0669` n `88`; fx avg `0.014` n `6`; index avg `-0.0003` n `25`; metal avg `0.1018` n `20`; unknown avg `-0.0761` n `766`
- 1h: commodity avg `-0.1305` n `12`; crypto_alt avg `0.5132` n `229`; crypto_major avg `0.7056` n `8`; equity avg `0.0488` n `88`; fx avg `0.0155` n `6`; index avg `0.0023` n `25`; metal avg `0.0191` n `20`; unknown avg `0.1723` n `765`
- 4h: commodity avg `0.0662` n `12`; crypto_alt avg `2.6764` n `229`; crypto_major avg `2.3295` n `8`; equity avg `0.8359` n `88`; fx avg `0.0435` n `6`; index avg `0.113` n `25`; metal avg `0.1953` n `20`; unknown avg `1.7512` n `765`
- 24h: commodity avg `-0.1424` n `12`; crypto_alt avg `1.3959` n `229`; crypto_major avg `1.1057` n `8`; equity avg `-0.0354` n `88`; fx avg `0.2083` n `6`; index avg `0.0773` n `25`; metal avg `-0.3055` n `20`; unknown avg `0.7911` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
