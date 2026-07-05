# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T02:52:25.567090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5911` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5592` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5589` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.2508` n `229`; crypto_major avg `-0.279` n `8`; equity avg `-0.0461` n `88`; fx avg `0.0026` n `6`; index avg `0.0139` n `25`; metal avg `-0.0148` n `20`; unknown avg `0.0004` n `765`
- 1h: commodity avg `0.039` n `12`; crypto_alt avg `-0.5379` n `229`; crypto_major avg `-0.5966` n `8`; equity avg `-0.0222` n `88`; fx avg `-0.0015` n `6`; index avg `0.0153` n `25`; metal avg `-0.0353` n `20`; unknown avg `-0.1699` n `765`
- 4h: commodity avg `0.0173` n `12`; crypto_alt avg `-1.3111` n `229`; crypto_major avg `-1.5887` n `8`; equity avg `-0.0298` n `88`; fx avg `0.0046` n `6`; index avg `0.0024` n `25`; metal avg `-0.0295` n `20`; unknown avg `-0.2359` n `763`
- 24h: commodity avg `0.0633` n `12`; crypto_alt avg `-0.9119` n `229`; crypto_major avg `-1.0055` n `8`; equity avg `0.1473` n `88`; fx avg `0.0274` n `6`; index avg `0.043` n `25`; metal avg `0.0775` n `20`; unknown avg `-0.9586` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
