# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T15:37:31.327747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.3112` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.08` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5201` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.1636` n `228`; crypto_major avg `0.3441` n `8`; equity avg `0.1054` n `86`; fx avg `0.001` n `6`; index avg `0.0235` n `23`; metal avg `-0.0682` n `20`; unknown avg `0.2369` n `765`
- 1h: commodity avg `0.2549` n `12`; crypto_alt avg `-0.2144` n `228`; crypto_major avg `-0.0743` n `8`; equity avg `-0.1142` n `86`; fx avg `0.0314` n `6`; index avg `-0.0214` n `23`; metal avg `0.2004` n `20`; unknown avg `0.2478` n `765`
- 4h: commodity avg `0.3302` n `12`; crypto_alt avg `-2.2658` n `228`; crypto_major avg `-2.7498` n `8`; equity avg `-2.3868` n `86`; fx avg `0.0595` n `6`; index avg `-0.2297` n `23`; metal avg `0.5614` n `20`; unknown avg `1.1222` n `765`
- 24h: commodity avg `0.339` n `12`; crypto_alt avg `-2.0517` n `228`; crypto_major avg `-1.9469` n `8`; equity avg `-1.1269` n `86`; fx avg `0.0693` n `6`; index avg `0.2278` n `23`; metal avg `0.1705` n `20`; unknown avg `0.5161` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
