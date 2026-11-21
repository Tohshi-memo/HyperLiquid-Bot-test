# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T04:07:34.086775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.9219` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.8263` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-4.714` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.4985` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-3.4451` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `3.4013` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-3.3142` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.2408` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0238` n `13`; crypto_alt avg `-1.1019` n `239`; crypto_major avg `-1.1185` n `8`; equity avg `-0.3181` n `166`; fx avg `-0.0076` n `6`; index avg `-0.0258` n `27`; metal avg `-0.074` n `20`; unknown avg `2.6125` n `1244`
- 1h: commodity avg `-0.084` n `13`; crypto_alt avg `-3.2718` n `239`; crypto_major avg `-3.5291` n `8`; equity avg `-1.2883` n `166`; fx avg `-0.0253` n `6`; index avg `-0.1278` n `27`; metal avg `-0.2149` n `20`; unknown avg `2.8194` n `1244`
- 4h: commodity avg `-0.0435` n `13`; crypto_alt avg `-4.484` n `239`; crypto_major avg `-4.9654` n `8`; equity avg `-1.4669` n `166`; fx avg `-0.026` n `6`; index avg `-0.1391` n `27`; metal avg `-0.2514` n `20`; unknown avg `1.4888` n `1248`
- 24h: commodity avg `0.1917` n `13`; crypto_alt avg `-7.6067` n `239`; crypto_major avg `-9.4575` n `8`; equity avg `-6.4124` n `166`; fx avg `-0.0719` n `6`; index avg `-0.6456` n `27`; metal avg `-0.2947` n `20`; unknown avg `13.0099` n `1109`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
