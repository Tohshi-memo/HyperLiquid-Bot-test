# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T13:07:34.182900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `-0.1818` n `229`; crypto_major avg `-0.2597` n `8`; equity avg `-0.0549` n `91`; fx avg `-0.0065` n `6`; index avg `-0.0` n `25`; metal avg `-0.0377` n `20`; unknown avg `-0.0315` n `763`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.5295` n `229`; crypto_major avg `-0.5402` n `8`; equity avg `-0.3282` n `91`; fx avg `-0.0086` n `6`; index avg `-0.0247` n `25`; metal avg `-0.0409` n `20`; unknown avg `-0.0354` n `763`
- 4h: commodity avg `-0.3017` n `12`; crypto_alt avg `0.2402` n `229`; crypto_major avg `0.0947` n `8`; equity avg `-0.2745` n `91`; fx avg `-0.087` n `6`; index avg `-0.001` n `25`; metal avg `0.324` n `20`; unknown avg `-0.1376` n `761`
- 24h: commodity avg `0.255` n `12`; crypto_alt avg `1.9394` n `229`; crypto_major avg `1.7385` n `8`; equity avg `-1.3538` n `90`; fx avg `-0.1739` n `6`; index avg `-0.3693` n `25`; metal avg `0.2238` n `20`; unknown avg `-0.2927` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
