# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T04:07:30.198460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.2485` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.9624` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.8992` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.61` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4911` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.034` n `13`; crypto_alt avg `0.4269` n `239`; crypto_major avg `0.2117` n `8`; equity avg `-0.1048` n `162`; fx avg `0.0027` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0021` n `20`; unknown avg `-0.0471` n `1250`
- 1h: commodity avg `0.0139` n `13`; crypto_alt avg `-1.3514` n `239`; crypto_major avg `-1.6202` n `8`; equity avg `-0.8858` n `162`; fx avg `0.0114` n `6`; index avg `-0.1291` n `27`; metal avg `-0.0102` n `20`; unknown avg `-0.1341` n `1248`
- 4h: commodity avg `-0.0987` n `13`; crypto_alt avg `-2.4819` n `239`; crypto_major avg `-3.0611` n `8`; equity avg `-1.7984` n `162`; fx avg `-0.0191` n `6`; index avg `-0.1619` n `27`; metal avg `0.1874` n `20`; unknown avg `0.581` n `1245`
- 24h: commodity avg `0.879` n `13`; crypto_alt avg `-2.9356` n `239`; crypto_major avg `-4.4257` n `8`; equity avg `-1.6932` n `162`; fx avg `-0.003` n `6`; index avg `-0.0772` n `27`; metal avg `-0.3929` n `20`; unknown avg `95.1873` n `1121`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
