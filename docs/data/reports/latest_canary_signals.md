# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T15:07:39.552170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0588` n `12`; crypto_alt avg `-0.3829` n `230`; crypto_major avg `-0.4625` n `8`; equity avg `-0.1239` n `94`; fx avg `-0.0055` n `6`; index avg `-0.0231` n `25`; metal avg `-0.046` n `20`; unknown avg `-0.039` n `768`
- 1h: commodity avg `-0.2823` n `12`; crypto_alt avg `-0.2546` n `230`; crypto_major avg `-0.322` n `8`; equity avg `-0.6075` n `94`; fx avg `-0.0437` n `6`; index avg `-0.0465` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.062` n `768`
- 4h: commodity avg `-0.134` n `12`; crypto_alt avg `0.2505` n `230`; crypto_major avg `0.0094` n `8`; equity avg `-1.3054` n `94`; fx avg `0.0132` n `6`; index avg `-0.0836` n `25`; metal avg `-0.2582` n `20`; unknown avg `0.1238` n `768`
- 24h: commodity avg `0.0146` n `12`; crypto_alt avg `-1.1396` n `230`; crypto_major avg `-1.9924` n `8`; equity avg `-2.904` n `94`; fx avg `-0.0793` n `6`; index avg `-0.2617` n `25`; metal avg `-0.4312` n `20`; unknown avg `-0.3154` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
