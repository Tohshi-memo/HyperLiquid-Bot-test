# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T04:27:46.798065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8373` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6862` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3707` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.1052` n `229`; crypto_major avg `0.1097` n `8`; equity avg `-0.1117` n `91`; fx avg `-0.0083` n `6`; index avg `-0.0263` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.1432` n `763`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.3051` n `229`; crypto_major avg `-0.3693` n `8`; equity avg `-0.2617` n `91`; fx avg `0.0119` n `6`; index avg `-0.1297` n `25`; metal avg `-0.0462` n `20`; unknown avg `0.1528` n `763`
- 4h: commodity avg `-0.0962` n `12`; crypto_alt avg `-1.0853` n `229`; crypto_major avg `-1.4053` n `8`; equity avg `0.432` n `91`; fx avg `-0.0703` n `6`; index avg `-0.0346` n `25`; metal avg `0.2809` n `20`; unknown avg `0.0721` n `763`
- 24h: commodity avg `0.91` n `12`; crypto_alt avg `-2.4115` n `229`; crypto_major avg `-1.6514` n `8`; equity avg `-0.8036` n `91`; fx avg `-0.1689` n `6`; index avg `-0.1388` n `25`; metal avg `-0.0452` n `20`; unknown avg `-0.4612` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
