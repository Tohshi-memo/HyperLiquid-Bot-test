# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T19:07:29.198889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.8945` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8155` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6733` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `0.1096` n `233`; crypto_major avg `0.1525` n `8`; equity avg `0.012` n `136`; fx avg `0.0122` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.0289` n `804`
- 1h: commodity avg `0.1304` n `12`; crypto_alt avg `-0.4287` n `233`; crypto_major avg `-0.1782` n `8`; equity avg `-0.2614` n `136`; fx avg `0.0181` n `6`; index avg `-0.0501` n `26`; metal avg `-0.0626` n `20`; unknown avg `-0.2102` n `804`
- 4h: commodity avg `0.0684` n `12`; crypto_alt avg `-2.1398` n `233`; crypto_major avg `-1.901` n `8`; equity avg `-0.2277` n `136`; fx avg `0.0014` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0855` n `20`; unknown avg `1.6945` n `752`
- 24h: commodity avg `-0.4081` n `12`; crypto_alt avg `-0.1548` n `233`; crypto_major avg `0.7178` n `8`; equity avg `0.5205` n `136`; fx avg `-0.1321` n `6`; index avg `0.3293` n `26`; metal avg `0.2608` n `20`; unknown avg `1.4621` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
