# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T03:37:27.010161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.7837` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6953` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5293` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.1404` n `229`; crypto_major avg `-0.218` n `8`; equity avg `0.1564` n `91`; fx avg `0.013` n `6`; index avg `-0.0007` n `25`; metal avg `0.0217` n `20`; unknown avg `0.5048` n `763`
- 1h: commodity avg `0.0343` n `12`; crypto_alt avg `0.5189` n `229`; crypto_major avg `0.4694` n `8`; equity avg `0.5834` n `91`; fx avg `-0.0304` n `6`; index avg `0.1071` n `25`; metal avg `0.1906` n `20`; unknown avg `0.5157` n `763`
- 4h: commodity avg `-0.0149` n `12`; crypto_alt avg `-0.9862` n `229`; crypto_major avg `-1.391` n `8`; equity avg `1.3927` n `91`; fx avg `-0.0336` n `6`; index avg `0.1383` n `25`; metal avg `0.3043` n `20`; unknown avg `0.6421` n `763`
- 24h: commodity avg `0.935` n `12`; crypto_alt avg `-2.4535` n `229`; crypto_major avg `-1.8785` n `8`; equity avg `-0.8293` n `91`; fx avg `-0.17` n `6`; index avg `-0.0773` n `25`; metal avg `-0.0218` n `20`; unknown avg `-0.3381` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
