# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T11:52:33.838839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5221` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3645` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.1363` n `228`; crypto_major avg `-0.1418` n `8`; equity avg `0.0563` n `86`; fx avg `-0.0137` n `6`; index avg `0.0234` n `23`; metal avg `0.1225` n `20`; unknown avg `-0.0612` n `765`
- 1h: commodity avg `0.0272` n `12`; crypto_alt avg `-0.3218` n `228`; crypto_major avg `-0.4148` n `8`; equity avg `-0.1174` n `86`; fx avg `-0.0258` n `6`; index avg `-0.0402` n `23`; metal avg `0.0597` n `20`; unknown avg `0.015` n `765`
- 4h: commodity avg `-0.0734` n `12`; crypto_alt avg `-1.0324` n `228`; crypto_major avg `-1.3723` n `8`; equity avg `-0.0528` n `86`; fx avg `-0.0116` n `6`; index avg `-0.0078` n `23`; metal avg `0.1498` n `20`; unknown avg `-0.0516` n `765`
- 24h: commodity avg `-0.1688` n `12`; crypto_alt avg `-2.1479` n `228`; crypto_major avg `-2.2397` n `8`; equity avg `-0.0373` n `86`; fx avg `-0.0205` n `6`; index avg `0.4522` n `23`; metal avg `-0.891` n `20`; unknown avg `-0.6794` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
