# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T16:07:35.041661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.7574` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.6292` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0028` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0491` n `12`; crypto_alt avg `0.3604` n `228`; crypto_major avg `0.1957` n `8`; equity avg `0.1552` n `86`; fx avg `-0.0` n `6`; index avg `0.0223` n `23`; metal avg `-0.0523` n `20`; unknown avg `0.1972` n `765`
- 1h: commodity avg `0.1174` n `12`; crypto_alt avg `0.5872` n `228`; crypto_major avg `0.7278` n `8`; equity avg `0.1186` n `86`; fx avg `0.0185` n `6`; index avg `0.0237` n `23`; metal avg `0.244` n `20`; unknown avg `0.0208` n `765`
- 4h: commodity avg `0.4016` n `12`; crypto_alt avg `-1.5811` n `228`; crypto_major avg `-2.2276` n `8`; equity avg `-2.2261` n `86`; fx avg `0.088` n `6`; index avg `-0.2248` n `23`; metal avg `0.5298` n `20`; unknown avg `0.8451` n `765`
- 24h: commodity avg `0.4418` n `12`; crypto_alt avg `-0.9583` n `228`; crypto_major avg `-0.9773` n `8`; equity avg `-0.6663` n `86`; fx avg `0.0874` n `6`; index avg `0.3039` n `23`; metal avg `0.3646` n `20`; unknown avg `0.1008` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
