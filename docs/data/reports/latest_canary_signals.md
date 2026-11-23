# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T20:37:25.410646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1519` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1415` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.1182` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.886` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.058` n `13`; crypto_alt avg `-0.3214` n `239`; crypto_major avg `-0.34` n `8`; equity avg `0.1691` n `166`; fx avg `0.0044` n `6`; index avg `0.0193` n `27`; metal avg `0.0012` n `20`; unknown avg `167.0933` n `1266`
- 1h: commodity avg `0.045` n `13`; crypto_alt avg `-0.0003` n `239`; crypto_major avg `0.0471` n `8`; equity avg `0.5011` n `166`; fx avg `0.0129` n `6`; index avg `0.0583` n `27`; metal avg `0.0295` n `20`; unknown avg `384.9211` n `1258`
- 4h: commodity avg `0.0268` n `13`; crypto_alt avg `-2.1236` n `239`; crypto_major avg `-2.1251` n `8`; equity avg `-0.0069` n `166`; fx avg `-0.0136` n `6`; index avg `0.0164` n `27`; metal avg `-0.2391` n `20`; unknown avg `385.2313` n `1258`
- 24h: commodity avg `-1.504` n `13`; crypto_alt avg `1.2156` n `239`; crypto_major avg `1.61` n `8`; equity avg `6.1283` n `166`; fx avg `-0.0781` n `6`; index avg `0.5955` n `27`; metal avg `0.6406` n `20`; unknown avg `310.9187` n `1066`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
