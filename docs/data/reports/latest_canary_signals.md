# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T15:07:34.758504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.6509` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.2477` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.7942` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.6389` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.2878` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.0763` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0931` n `13`; crypto_alt avg `-0.9252` n `239`; crypto_major avg `-1.0576` n `8`; equity avg `-0.3779` n `158`; fx avg `-0.0117` n `6`; index avg `-0.0688` n `27`; metal avg `0.0674` n `20`; unknown avg `36.9588` n `1248`
- 1h: commodity avg `0.2029` n `13`; crypto_alt avg `-2.3322` n `239`; crypto_major avg `-2.436` n `8`; equity avg `-3.662` n `158`; fx avg `0.0174` n `6`; index avg `-0.3597` n `27`; metal avg `-0.1482` n `20`; unknown avg `65.72` n `1252`
- 4h: commodity avg `0.4194` n `13`; crypto_alt avg `-2.9904` n `239`; crypto_major avg `-3.2315` n `8`; equity avg `-4.5941` n `158`; fx avg `0.035` n `6`; index avg `-0.4373` n `27`; metal avg `0.0162` n `20`; unknown avg `65.589` n `1245`
- 24h: commodity avg `-0.5395` n `13`; crypto_alt avg `-4.5147` n `239`; crypto_major avg `-4.3719` n `8`; equity avg `-7.2188` n `158`; fx avg `0.0075` n `6`; index avg `-0.7779` n `27`; metal avg `0.6281` n `20`; unknown avg `197.3749` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2329`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1936`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
