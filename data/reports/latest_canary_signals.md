# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T03:52:23.672152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5468` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2958` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1591` n `231`; crypto_major avg `0.1346` n `8`; equity avg `0.012` n `122`; fx avg `0.0045` n `6`; index avg `-0.0003` n `25`; metal avg `-0.048` n `20`; unknown avg `-0.1402` n `793`
- 1h: commodity avg `0.0418` n `12`; crypto_alt avg `-0.3114` n `231`; crypto_major avg `-0.3732` n `8`; equity avg `-0.4589` n `122`; fx avg `0.0143` n `6`; index avg `-0.0798` n `25`; metal avg `0.0707` n `20`; unknown avg `-0.0374` n `793`
- 4h: commodity avg `-0.0741` n `12`; crypto_alt avg `-2.0626` n `231`; crypto_major avg `-1.4995` n `8`; equity avg `-1.8587` n `122`; fx avg `-0.0594` n `6`; index avg `-0.2037` n `25`; metal avg `0.0473` n `20`; unknown avg `0.5253` n `793`
- 24h: commodity avg `-0.2799` n `12`; crypto_alt avg `3.3299` n `231`; crypto_major avg `0.6346` n `8`; equity avg `-1.1495` n `122`; fx avg `-0.1881` n `6`; index avg `-0.1066` n `25`; metal avg `0.1439` n `20`; unknown avg `5.9693` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
