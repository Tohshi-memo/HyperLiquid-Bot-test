# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T04:37:34.687121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.1841` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.9961` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9228` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7012` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `-0.3057` n `239`; crypto_major avg `-0.3289` n `8`; equity avg `0.0212` n `162`; fx avg `0.007` n `6`; index avg `0.0212` n `27`; metal avg `-0.0162` n `20`; unknown avg `39.2711` n `1262`
- 1h: commodity avg `0.0448` n `13`; crypto_alt avg `-0.8204` n `239`; crypto_major avg `-0.9699` n `8`; equity avg `-0.2785` n `162`; fx avg `0.0071` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0973` n `20`; unknown avg `1.3449` n `1248`
- 4h: commodity avg `-0.0343` n `13`; crypto_alt avg `-2.5159` n `239`; crypto_major avg `-3.0304` n `8`; equity avg `-1.3292` n `162`; fx avg `-0.0136` n `6`; index avg `-0.1076` n `27`; metal avg `0.1537` n `20`; unknown avg `1.4182` n `1245`
- 24h: commodity avg `0.9156` n `13`; crypto_alt avg `-3.0073` n `239`; crypto_major avg `-4.5348` n `8`; equity avg `-1.4082` n `162`; fx avg `-0.0077` n `6`; index avg `-0.0058` n `27`; metal avg `-0.4287` n `20`; unknown avg `99.5265` n `1121`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
