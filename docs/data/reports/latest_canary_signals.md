# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T15:22:36.134994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.5422` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.3517` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6703` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0692` n `12`; crypto_alt avg `-0.1788` n `228`; crypto_major avg `-0.0838` n `8`; equity avg `-0.1496` n `86`; fx avg `0.0048` n `6`; index avg `-0.0361` n `23`; metal avg `0.2134` n `20`; unknown avg `-0.0617` n `765`
- 1h: commodity avg `0.1082` n `12`; crypto_alt avg `-0.1095` n `228`; crypto_major avg `-0.3433` n `8`; equity avg `-0.2075` n `86`; fx avg `0.0249` n `6`; index avg `-0.0391` n `23`; metal avg `0.2853` n `20`; unknown avg `0.6077` n `765`
- 4h: commodity avg `0.3863` n `12`; crypto_alt avg `-2.3046` n `228`; crypto_major avg `-2.9654` n `8`; equity avg `-2.5142` n `86`; fx avg `0.0575` n `6`; index avg `-0.2951` n `23`; metal avg `0.5768` n `20`; unknown avg `0.9098` n `765`
- 24h: commodity avg `0.4189` n `12`; crypto_alt avg `-2.7973` n `228`; crypto_major avg `-3.0802` n `8`; equity avg `-1.2995` n `86`; fx avg `0.0578` n `6`; index avg `0.2258` n `23`; metal avg `0.2055` n `20`; unknown avg `0.2274` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
