# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T05:07:26.470328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2609` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.0626` n `229`; crypto_major avg `-0.0354` n `8`; equity avg `-0.1495` n `91`; fx avg `0.0242` n `6`; index avg `-0.0224` n `25`; metal avg `-0.0495` n `20`; unknown avg `-0.2276` n `763`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.2924` n `229`; crypto_major avg `-0.2467` n `8`; equity avg `-0.3905` n `91`; fx avg `0.0317` n `6`; index avg `-0.0808` n `25`; metal avg `-0.1633` n `20`; unknown avg `12.6624` n `763`
- 4h: commodity avg `-0.0405` n `12`; crypto_alt avg `-1.2663` n `229`; crypto_major avg `-1.5519` n `8`; equity avg `-1.3399` n `91`; fx avg `-0.0734` n `6`; index avg `-0.291` n `25`; metal avg `-0.1608` n `20`; unknown avg `14.606` n `761`
- 24h: commodity avg `0.219` n `12`; crypto_alt avg `-0.2633` n `229`; crypto_major avg `-1.1158` n `8`; equity avg `-2.1062` n `90`; fx avg `0.0006` n `6`; index avg `-0.4207` n `25`; metal avg `-0.3589` n `20`; unknown avg `-0.6695` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
