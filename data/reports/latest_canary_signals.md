# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T16:07:35.659289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2941` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4765` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1847` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `-0.6208` n `228`; crypto_major avg `-0.5566` n `8`; equity avg `-0.5051` n `74`; fx avg `-0.0124` n `6`; index avg `-0.1636` n `23`; metal avg `-0.1524` n `18`; unknown avg `0.9628` n `424`
- 1h: commodity avg `-0.3068` n `12`; crypto_alt avg `-2.0282` n `228`; crypto_major avg `-1.6369` n `8`; equity avg `-1.2758` n `74`; fx avg `-0.0614` n `6`; index avg `-0.4522` n `23`; metal avg `-0.8805` n `18`; unknown avg `-0.6469` n `424`
- 4h: commodity avg `-1.0576` n `12`; crypto_alt avg `-3.1` n `228`; crypto_major avg `-3.3517` n `8`; equity avg `-3.6483` n `74`; fx avg `-0.2133` n `6`; index avg `-1.8752` n `23`; metal avg `-3.6237` n `18`; unknown avg `-1.121` n `424`
- 24h: commodity avg `-1.1324` n `12`; crypto_alt avg `-9.4452` n `228`; crypto_major avg `-7.4426` n `8`; equity avg `-5.3363` n `74`; fx avg `-0.0582` n `6`; index avg `-2.4992` n `23`; metal avg `-4.0854` n `18`; unknown avg `-0.2903` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
