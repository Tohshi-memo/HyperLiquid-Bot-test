# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T11:52:30.049465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.4162` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.3049` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1118` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6006` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0737` n `12`; crypto_alt avg `-0.2343` n `228`; crypto_major avg `-0.3475` n `8`; equity avg `-0.1662` n `86`; fx avg `0.0012` n `6`; index avg `-0.0165` n `23`; metal avg `-0.099` n `20`; unknown avg `-0.0345` n `765`
- 1h: commodity avg `0.181` n `12`; crypto_alt avg `-0.178` n `228`; crypto_major avg `-0.3203` n `8`; equity avg `-0.0662` n `86`; fx avg `-0.007` n `6`; index avg `-0.0072` n `23`; metal avg `-0.0756` n `20`; unknown avg `-0.0374` n `765`
- 4h: commodity avg `0.0965` n `12`; crypto_alt avg `-1.589` n `228`; crypto_major avg `-2.2084` n `8`; equity avg `-0.6078` n `86`; fx avg `0.0202` n `6`; index avg `-0.0966` n `23`; metal avg `0.2078` n `20`; unknown avg `-0.1283` n `765`
- 24h: commodity avg `0.2035` n `12`; crypto_alt avg `-2.0351` n `228`; crypto_major avg `-2.1613` n `8`; equity avg `-4.2449` n `86`; fx avg `0.0728` n `6`; index avg `-0.6161` n `23`; metal avg `0.5657` n `20`; unknown avg `0.6952` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2689`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
