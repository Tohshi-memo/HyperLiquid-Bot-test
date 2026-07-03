# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T05:37:26.825509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `0.4086` n `229`; crypto_major avg `0.4877` n `8`; equity avg `0.082` n `88`; fx avg `-0.0277` n `6`; index avg `0.0233` n `25`; metal avg `0.0665` n `20`; unknown avg `0.2534` n `765`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `0.3271` n `229`; crypto_major avg `0.6364` n `8`; equity avg `0.0367` n `88`; fx avg `0.0263` n `6`; index avg `0.016` n `25`; metal avg `0.0151` n `20`; unknown avg `-0.2186` n `765`
- 4h: commodity avg `0.1841` n `12`; crypto_alt avg `0.0405` n `229`; crypto_major avg `0.3052` n `8`; equity avg `0.6824` n `88`; fx avg `0.0627` n `6`; index avg `0.1835` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.4746` n `761`
- 24h: commodity avg `0.4448` n `12`; crypto_alt avg `1.9955` n `228`; crypto_major avg `3.2384` n `8`; equity avg `-0.3679` n `88`; fx avg `-0.0555` n `6`; index avg `0.0452` n `25`; metal avg `1.3312` n `20`; unknown avg `6.0621` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
