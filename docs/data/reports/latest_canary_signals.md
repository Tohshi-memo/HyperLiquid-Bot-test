# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T21:07:27.624599+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.8915` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.7941` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.6825` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `2.0623` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.016` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.0127` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `-1.7064` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0175` n `13`; crypto_alt avg `0.2992` n `238`; crypto_major avg `-0.2021` n `8`; equity avg `-0.1814` n `156`; fx avg `-0.0032` n `6`; index avg `-0.041` n `27`; metal avg `-0.0157` n `20`; unknown avg `154.3872` n `1246`
- 1h: commodity avg `-0.0631` n `13`; crypto_alt avg `-2.6134` n `238`; crypto_major avg `-2.0758` n `8`; equity avg `-0.3694` n `156`; fx avg `0.0205` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0598` n `20`; unknown avg `146.4442` n `1184`
- 4h: commodity avg `0.0133` n `13`; crypto_alt avg `-5.1016` n `238`; crypto_major avg `-3.8782` n `8`; equity avg `-2.3994` n `156`; fx avg `0.016` n `6`; index avg `-0.1957` n `27`; metal avg `-0.0841` n `20`; unknown avg `29.8651` n `1162`
- 24h: commodity avg `-0.2175` n `13`; crypto_alt avg `-5.4444` n `238`; crypto_major avg `-2.3193` n `8`; equity avg `-3.0276` n `155`; fx avg `0.055` n `6`; index avg `-0.2588` n `27`; metal avg `-0.6025` n `20`; unknown avg `32.9185` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
