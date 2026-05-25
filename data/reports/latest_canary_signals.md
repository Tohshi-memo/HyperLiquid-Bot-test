# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T08:07:21.236990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `0.1279` n `228`; crypto_major avg `0.1401` n `8`; equity avg `0.0491` n `67`; fx avg `0.0164` n `6`; index avg `-0.0174` n `23`; metal avg `-0.0543` n `18`; unknown avg `0.8925` n `397`
- 1h: commodity avg `0.0813` n `12`; crypto_alt avg `0.0072` n `228`; crypto_major avg `0.2383` n `8`; equity avg `0.0713` n `67`; fx avg `0.0407` n `6`; index avg `-0.0461` n `23`; metal avg `0.0344` n `18`; unknown avg `0.9295` n `397`
- 4h: commodity avg `0.2993` n `12`; crypto_alt avg `1.2374` n `228`; crypto_major avg `1.0094` n `8`; equity avg `0.1454` n `67`; fx avg `0.0735` n `6`; index avg `0.0004` n `23`; metal avg `0.0791` n `18`; unknown avg `1.2799` n `387`
- 24h: commodity avg `0.1478` n `12`; crypto_alt avg `0.4604` n `228`; crypto_major avg `0.5253` n `8`; equity avg `0.5501` n `67`; fx avg `0.0099` n `6`; index avg `-0.0773` n `23`; metal avg `0.4338` n `18`; unknown avg `1.1589` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
