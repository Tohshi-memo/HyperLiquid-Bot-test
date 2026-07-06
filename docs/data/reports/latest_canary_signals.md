# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T19:52:25.965957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.1146` n `229`; crypto_major avg `-0.0769` n `8`; equity avg `-0.0327` n `91`; fx avg `0.0039` n `6`; index avg `-0.0125` n `25`; metal avg `0.0424` n `20`; unknown avg `-0.0717` n `763`
- 1h: commodity avg `0.0384` n `12`; crypto_alt avg `-0.0687` n `229`; crypto_major avg `0.0001` n `8`; equity avg `0.1486` n `91`; fx avg `-0.0015` n `6`; index avg `0.0093` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.1335` n `763`
- 4h: commodity avg `0.0371` n `12`; crypto_alt avg `0.3991` n `229`; crypto_major avg `0.7198` n `8`; equity avg `-0.4139` n `90`; fx avg `0.0054` n `6`; index avg `-0.0384` n `25`; metal avg `0.1699` n `20`; unknown avg `0.1553` n `763`
- 24h: commodity avg `0.0634` n `12`; crypto_alt avg `0.8908` n `229`; crypto_major avg `0.7845` n `8`; equity avg `-0.6187` n `90`; fx avg `0.1975` n `6`; index avg `0.0291` n `25`; metal avg `-0.1498` n `20`; unknown avg `0.2117` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
