# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T16:59:49.548625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0621` n `12`; crypto_alt avg `-0.0286` n `228`; crypto_major avg `-0.2425` n `8`; equity avg `-0.1686` n `67`; fx avg `0.0028` n `6`; index avg `-0.09` n `23`; metal avg `-0.1205` n `18`; unknown avg `-0.0708` n `418`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0317` n `228`; crypto_major avg `-0.0125` n `8`; equity avg `0.1576` n `67`; fx avg `0.025` n `6`; index avg `0.1388` n `23`; metal avg `0.0024` n `18`; unknown avg `0.2975` n `418`
- 4h: commodity avg `0.4077` n `12`; crypto_alt avg `-0.7084` n `228`; crypto_major avg `-0.6117` n `8`; equity avg `-0.0571` n `67`; fx avg `-0.0052` n `6`; index avg `0.3367` n `23`; metal avg `-0.1202` n `18`; unknown avg `1.1617` n `416`
- 24h: commodity avg `1.2796` n `12`; crypto_alt avg `-1.5299` n `228`; crypto_major avg `-1.3381` n `8`; equity avg `-0.4401` n `67`; fx avg `-0.1071` n `6`; index avg `0.3868` n `23`; metal avg `-1.3244` n `18`; unknown avg `0.1237` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
