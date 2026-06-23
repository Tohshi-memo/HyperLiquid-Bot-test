# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T06:22:29.815645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1587` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8472` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7897` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.5629` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.461` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-1.6472` n `228`; crypto_major avg `-1.0611` n `8`; equity avg `-0.3094` n `86`; fx avg `0.036` n `6`; index avg `-0.0844` n `23`; metal avg `0.0325` n `20`; unknown avg `-0.2859` n `716`
- 1h: commodity avg `-0.1293` n `12`; crypto_alt avg `-2.1401` n `228`; crypto_major avg `-1.6911` n `8`; equity avg `-1.0524` n `86`; fx avg `0.0704` n `6`; index avg `-0.2301` n `23`; metal avg `-0.1282` n `20`; unknown avg `-0.4123` n `676`
- 4h: commodity avg `-0.159` n `12`; crypto_alt avg `-2.4502` n `228`; crypto_major avg `-2.3177` n `8`; equity avg `-2.2168` n `86`; fx avg `0.0559` n `6`; index avg `-0.4705` n `23`; metal avg `-0.528` n `20`; unknown avg `0.0243` n `676`
- 24h: commodity avg `-0.5646` n `12`; crypto_alt avg `-3.3313` n `228`; crypto_major avg `-2.7733` n `8`; equity avg `-4.2088` n `85`; fx avg `0.0342` n `6`; index avg `-0.7571` n `23`; metal avg `-1.359` n `18`; unknown avg `0.6189` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
