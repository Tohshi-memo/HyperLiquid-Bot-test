# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T22:22:27.770230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9604` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.6458` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5974` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.4526` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.2139` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.166` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-1.659` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-1.5407` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0727` n `13`; crypto_alt avg `0.4483` n `239`; crypto_major avg `0.2917` n `8`; equity avg `0.1585` n `158`; fx avg `0.0095` n `6`; index avg `0.0175` n `27`; metal avg `0.0197` n `20`; unknown avg `0.9687` n `1254`
- 1h: commodity avg `0.1973` n `13`; crypto_alt avg `-1.8727` n `239`; crypto_major avg `-2.2553` n `8`; equity avg `-0.5963` n `158`; fx avg `-0.0218` n `6`; index avg `-0.0414` n `27`; metal avg `-0.0893` n `20`; unknown avg `0.8951` n `1238`
- 4h: commodity avg `0.2363` n `13`; crypto_alt avg `-2.2225` n `239`; crypto_major avg `-2.7241` n `8`; equity avg `-1.1834` n `158`; fx avg `-0.0527` n `6`; index avg `-0.1267` n `27`; metal avg `-0.0783` n `20`; unknown avg `1.0485` n `1190`
- 24h: commodity avg `0.0906` n `13`; crypto_alt avg `-3.339` n `239`; crypto_major avg `-2.6883` n `8`; equity avg `-0.5579` n `158`; fx avg `0.0183` n `6`; index avg `-0.1018` n `27`; metal avg `-0.1065` n `20`; unknown avg `-0.6093` n `1016`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
