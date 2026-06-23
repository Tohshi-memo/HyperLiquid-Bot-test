# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T08:07:37.813764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2573` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.826` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7347` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.052` n `12`; crypto_alt avg `-0.0945` n `228`; crypto_major avg `-0.2017` n `8`; equity avg `-0.0674` n `86`; fx avg `-0.0223` n `6`; index avg `-0.0411` n `23`; metal avg `-0.0087` n `20`; unknown avg `-0.1239` n `764`
- 1h: commodity avg `0.1028` n `12`; crypto_alt avg `-0.2548` n `228`; crypto_major avg `-0.5168` n `8`; equity avg `-0.3345` n `86`; fx avg `-0.0316` n `6`; index avg `-0.069` n `23`; metal avg `-0.2238` n `20`; unknown avg `-0.2617` n `620`
- 4h: commodity avg `-0.0177` n `12`; crypto_alt avg `-2.3264` n `228`; crypto_major avg `-2.275` n `8`; equity avg `-1.5959` n `86`; fx avg `-0.0086` n `6`; index avg `-0.449` n `23`; metal avg `-0.5403` n `20`; unknown avg `0.0953` n `604`
- 24h: commodity avg `-0.8048` n `12`; crypto_alt avg `-3.0264` n `228`; crypto_major avg `-3.1657` n `8`; equity avg `-4.1003` n `85`; fx avg `-0.044` n `6`; index avg `-0.7875` n `23`; metal avg `-1.489` n `18`; unknown avg `0.7508` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
