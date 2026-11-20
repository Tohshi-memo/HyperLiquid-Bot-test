# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T15:52:29.314647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.9462` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.8167` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.7398` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-3.0429` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.8321` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.7922` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7415` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1633` n `13`; crypto_alt avg `-0.3902` n `239`; crypto_major avg `-0.4375` n `8`; equity avg `-0.0216` n `166`; fx avg `0.0197` n `6`; index avg `-0.0142` n `27`; metal avg `-0.0653` n `20`; unknown avg `0.0753` n `1261`
- 1h: commodity avg `0.0474` n `13`; crypto_alt avg `-2.9407` n `239`; crypto_major avg `-2.9955` n `8`; equity avg `-2.2878` n `166`; fx avg `0.0157` n `6`; index avg `-0.2033` n `27`; metal avg `-0.1634` n `20`; unknown avg `1.5207` n `1253`
- 4h: commodity avg `-0.0532` n `13`; crypto_alt avg `-3.7566` n `239`; crypto_major avg `-3.9994` n `8`; equity avg `-2.2579` n `166`; fx avg `0.0492` n `6`; index avg `-0.1827` n `27`; metal avg `-0.2596` n `20`; unknown avg `0.6278` n `1249`
- 24h: commodity avg `-0.307` n `13`; crypto_alt avg `-6.3032` n `239`; crypto_major avg `-6.134` n `8`; equity avg `-8.1885` n `166`; fx avg `-0.0362` n `6`; index avg `-0.678` n `27`; metal avg `-1.1155` n `20`; unknown avg `37.6579` n `1154`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
