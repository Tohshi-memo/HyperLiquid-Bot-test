# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T23:22:25.844121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0372` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.8272` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.796` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `-0.1766` n `231`; crypto_major avg `-0.1405` n `8`; equity avg `-0.2435` n `128`; fx avg `-0.0048` n `6`; index avg `-0.0416` n `26`; metal avg `-0.0277` n `20`; unknown avg `-0.1082` n `793`
- 1h: commodity avg `-0.1019` n `12`; crypto_alt avg `-0.5342` n `231`; crypto_major avg `-0.4391` n `8`; equity avg `-0.5355` n `128`; fx avg `0.011` n `6`; index avg `-0.0906` n `26`; metal avg `0.0291` n `20`; unknown avg `-0.2623` n `791`
- 4h: commodity avg `0.0616` n `12`; crypto_alt avg `-1.7064` n `231`; crypto_major avg `-1.9756` n `8`; equity avg `-0.8542` n `128`; fx avg `0.0008` n `6`; index avg `-0.1796` n `26`; metal avg `-0.1484` n `20`; unknown avg `0.7804` n `791`
- 24h: commodity avg `0.2523` n `12`; crypto_alt avg `0.0762` n `231`; crypto_major avg `-1.0754` n `8`; equity avg `-0.6871` n `128`; fx avg `0.0295` n `6`; index avg `-0.1575` n `26`; metal avg `-0.0508` n `20`; unknown avg `-0.2654` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
