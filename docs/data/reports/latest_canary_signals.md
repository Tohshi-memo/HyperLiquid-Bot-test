# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T14:37:32.478267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.3409` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.2072` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.8526` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.3373` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `-2.2249` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `2.1045` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1572` n `12`; crypto_alt avg `0.2678` n `228`; crypto_major avg `0.0743` n `8`; equity avg `0.0134` n `86`; fx avg `-0.0055` n `6`; index avg `0.0058` n `23`; metal avg `0.0161` n `20`; unknown avg `0.745` n `765`
- 1h: commodity avg `-0.0022` n `12`; crypto_alt avg `-1.7652` n `228`; crypto_major avg `-2.3395` n `8`; equity avg `-1.6528` n `86`; fx avg `0.0124` n `6`; index avg `-0.235` n `23`; metal avg `-0.1146` n `20`; unknown avg `0.4748` n `765`
- 4h: commodity avg `0.1053` n `12`; crypto_alt avg `-2.2601` n `228`; crypto_major avg `-3.1019` n `8`; equity avg `-2.4812` n `86`; fx avg `0.0179` n `6`; index avg `-0.2493` n `23`; metal avg `0.239` n `20`; unknown avg `0.7541` n `765`
- 24h: commodity avg `0.174` n `12`; crypto_alt avg `-2.6689` n `228`; crypto_major avg `-2.98` n `8`; equity avg `-1.0968` n `86`; fx avg `0.0578` n `6`; index avg `0.2585` n `23`; metal avg `-0.1985` n `20`; unknown avg `-0.1688` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
