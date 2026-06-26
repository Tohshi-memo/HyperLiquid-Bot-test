# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T02:22:30.676045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6559` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.634` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6085` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-1.5307` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0072` n `12`; crypto_alt avg `-1.6663` n `228`; crypto_major avg `-1.4859` n `8`; equity avg `-0.5908` n `86`; fx avg `-0.0054` n `6`; index avg `-0.0821` n `23`; metal avg `-0.1211` n `20`; unknown avg `0.7145` n `765`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `-2.1498` n `228`; crypto_major avg `-1.8915` n `8`; equity avg `-1.2406` n `86`; fx avg `-0.0182` n `6`; index avg `-0.2575` n `23`; metal avg `-0.3608` n `20`; unknown avg `-1.0182` n `765`
- 4h: commodity avg `-0.0259` n `12`; crypto_alt avg `-2.1942` n `228`; crypto_major avg `-1.9635` n `8`; equity avg `-1.5532` n `86`; fx avg `0.0298` n `6`; index avg `-0.3076` n `23`; metal avg `-0.355` n `20`; unknown avg `-1.0148` n `749`
- 24h: commodity avg `0.4651` n `12`; crypto_alt avg `-3.4827` n `228`; crypto_major avg `-3.5091` n `8`; equity avg `-3.5682` n `86`; fx avg `0.04` n `6`; index avg `-0.4833` n `23`; metal avg `0.0638` n `20`; unknown avg `0.1666` n `716`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
