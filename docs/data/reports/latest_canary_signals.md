# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T22:52:24.125986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.076` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `-0.0519` n `8`; equity avg `-0.0335` n `92`; fx avg `0.0095` n `6`; index avg `-0.0411` n `25`; metal avg `-0.0086` n `20`; unknown avg `-0.0869` n `766`
- 1h: commodity avg `0.114` n `12`; crypto_alt avg `0.3356` n `230`; crypto_major avg `0.2117` n `8`; equity avg `-0.033` n `92`; fx avg `-0.0227` n `6`; index avg `-0.0216` n `25`; metal avg `0.0038` n `20`; unknown avg `-0.1816` n `766`
- 4h: commodity avg `0.2298` n `12`; crypto_alt avg `-0.5168` n `230`; crypto_major avg `-0.2724` n `8`; equity avg `-0.1213` n `92`; fx avg `-0.0269` n `6`; index avg `-0.0965` n `25`; metal avg `0.0004` n `20`; unknown avg `-0.4181` n `766`
- 24h: commodity avg `0.9764` n `12`; crypto_alt avg `-1.7921` n `230`; crypto_major avg `-2.3481` n `8`; equity avg `-3.0171` n `92`; fx avg `-0.0463` n `6`; index avg `-0.61` n `25`; metal avg `-0.3023` n `20`; unknown avg `-0.3923` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
