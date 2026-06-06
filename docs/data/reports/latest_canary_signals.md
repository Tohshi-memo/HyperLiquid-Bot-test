# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T04:07:21.591347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1788` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.711` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6688` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3143` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2823` n `12`; crypto_alt avg `-0.8715` n `228`; crypto_major avg `-0.7336` n `8`; equity avg `-0.0816` n `74`; fx avg `0.0211` n `6`; index avg `0.1144` n `23`; metal avg `-0.0682` n `18`; unknown avg `-0.259` n `425`
- 1h: commodity avg `-0.0969` n `12`; crypto_alt avg `-1.4133` n `228`; crypto_major avg `-1.1219` n `8`; equity avg `0.2546` n `74`; fx avg `0.0088` n `6`; index avg `0.1924` n `23`; metal avg `-0.1517` n `18`; unknown avg `-0.7287` n `425`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `-3.0589` n `228`; crypto_major avg `-2.1873` n `8`; equity avg `-1.3374` n `74`; fx avg `-0.0212` n `6`; index avg `-0.5185` n `23`; metal avg `-0.4763` n `18`; unknown avg `0.5615` n `425`
- 24h: commodity avg `-1.2413` n `12`; crypto_alt avg `-7.0575` n `228`; crypto_major avg `-6.0407` n `8`; equity avg `-6.5389` n `74`; fx avg `-0.2074` n `6`; index avg `-3.8381` n `23`; metal avg `-4.2246` n `18`; unknown avg `-1.2687` n `404`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
