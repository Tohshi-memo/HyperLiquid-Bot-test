# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T05:07:18.507812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.1063` n `228`; crypto_major avg `-0.0684` n `8`; equity avg `-0.0073` n `65`; fx avg `0.0` n `5`; index avg `-0.0049` n `23`; metal avg `-0.0117` n `18`; unknown avg `-0.2836` n `376`
- 1h: commodity avg `0.0168` n `12`; crypto_alt avg `-0.0158` n `228`; crypto_major avg `-0.0226` n `8`; equity avg `0.0688` n `65`; fx avg `0.0006` n `5`; index avg `0.0122` n `23`; metal avg `0.0483` n `18`; unknown avg `-0.3131` n `376`
- 4h: commodity avg `-0.128` n `12`; crypto_alt avg `0.2897` n `228`; crypto_major avg `0.2628` n `8`; equity avg `0.4178` n `65`; fx avg `0.0032` n `5`; index avg `0.0758` n `23`; metal avg `0.2159` n `18`; unknown avg `-0.4766` n `376`
- 24h: commodity avg `0.2319` n `12`; crypto_alt avg `-1.5312` n `228`; crypto_major avg `-0.5476` n `8`; equity avg `1.0453` n `65`; fx avg `-0.0055` n `5`; index avg `0.3248` n `23`; metal avg `0.3824` n `18`; unknown avg `-0.4601` n `356`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
