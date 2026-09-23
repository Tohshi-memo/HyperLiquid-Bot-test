# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T15:37:35.733327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.474` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0951` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0534` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.9413` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.182` n `12`; crypto_alt avg `-0.9368` n `234`; crypto_major avg `-0.6701` n `8`; equity avg `-0.1427` n `140`; fx avg `0.0143` n `6`; index avg `-0.0408` n `26`; metal avg `-0.1061` n `20`; unknown avg `-0.2546` n `944`
- 1h: commodity avg `0.2729` n `12`; crypto_alt avg `-0.9951` n `234`; crypto_major avg `-0.4579` n `8`; equity avg `0.2984` n `140`; fx avg `-0.0019` n `6`; index avg `0.0112` n `26`; metal avg `-0.0832` n `20`; unknown avg `1.6146` n `942`
- 4h: commodity avg `0.2333` n `12`; crypto_alt avg `-3.2124` n `234`; crypto_major avg `-2.2407` n `8`; equity avg `-0.2994` n `140`; fx avg `0.0011` n `6`; index avg `-0.1456` n `26`; metal avg `-0.1873` n `20`; unknown avg `510.7091` n `898`
- 24h: commodity avg `0.52` n `12`; crypto_alt avg `-1.6799` n `234`; crypto_major avg `-2.7741` n `8`; equity avg `-0.5555` n `140`; fx avg `0.0348` n `6`; index avg `-0.2118` n `26`; metal avg `-0.5451` n `20`; unknown avg `16.4489` n `838`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2544`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
