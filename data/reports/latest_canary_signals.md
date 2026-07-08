# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T02:52:26.195734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1442` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5672` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5071` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0207` n `12`; crypto_alt avg `0.3713` n `229`; crypto_major avg `0.4697` n `8`; equity avg `0.0813` n `91`; fx avg `-0.0351` n `6`; index avg `0.0161` n `25`; metal avg `-0.0226` n `20`; unknown avg `0.7746` n `763`
- 1h: commodity avg `0.0598` n `12`; crypto_alt avg `-0.2507` n `229`; crypto_major avg `-0.2961` n `8`; equity avg `0.0395` n `91`; fx avg `-0.0054` n `6`; index avg `-0.0795` n `25`; metal avg `0.1105` n `20`; unknown avg `0.0404` n `763`
- 4h: commodity avg `-0.0335` n `12`; crypto_alt avg `-1.1944` n `229`; crypto_major avg `-1.4538` n `8`; equity avg `0.6904` n `91`; fx avg `-0.0172` n `6`; index avg `0.0533` n `25`; metal avg `0.1134` n `20`; unknown avg `1.3006` n `763`
- 24h: commodity avg `0.8745` n `12`; crypto_alt avg `-2.6935` n `229`; crypto_major avg `-1.948` n `8`; equity avg `-1.5064` n `91`; fx avg `-0.2169` n `6`; index avg `-0.2083` n `25`; metal avg `-0.2911` n `20`; unknown avg `-0.3461` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
