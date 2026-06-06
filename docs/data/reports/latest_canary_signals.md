# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T07:37:24.046238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `12`; crypto_alt avg `0.0915` n `228`; crypto_major avg `0.1818` n `8`; equity avg `0.0194` n `74`; fx avg `-0.0007` n `6`; index avg `0.0333` n `23`; metal avg `-0.0008` n `18`; unknown avg `-0.0653` n `425`
- 1h: commodity avg `-0.0587` n `12`; crypto_alt avg `-0.1471` n `228`; crypto_major avg `-0.1991` n `8`; equity avg `-0.4121` n `74`; fx avg `-0.0117` n `6`; index avg `-0.0202` n `23`; metal avg `0.0613` n `18`; unknown avg `0.9734` n `425`
- 4h: commodity avg `-0.3987` n `12`; crypto_alt avg `0.0766` n `228`; crypto_major avg `0.4486` n `8`; equity avg `0.0002` n `74`; fx avg `-0.0008` n `6`; index avg `0.1804` n `23`; metal avg `0.0316` n `18`; unknown avg `-0.1923` n `415`
- 24h: commodity avg `-1.2276` n `12`; crypto_alt avg `-3.8319` n `228`; crypto_major avg `-3.2093` n `8`; equity avg `-6.4415` n `74`; fx avg `-0.2247` n `6`; index avg `-3.9738` n `23`; metal avg `-4.2077` n `18`; unknown avg `0.5377` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
