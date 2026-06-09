# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T09:22:29.926310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0704` n `12`; crypto_alt avg `0.2056` n `228`; crypto_major avg `0.2456` n `8`; equity avg `0.1069` n `74`; fx avg `0.0218` n `6`; index avg `0.0569` n `23`; metal avg `0.0675` n `18`; unknown avg `0.0318` n `547`
- 1h: commodity avg `-0.4323` n `12`; crypto_alt avg `-0.0187` n `228`; crypto_major avg `0.214` n `8`; equity avg `0.1405` n `74`; fx avg `0.0313` n `6`; index avg `0.154` n `23`; metal avg `-0.1134` n `18`; unknown avg `-0.1557` n `547`
- 4h: commodity avg `-0.3489` n `12`; crypto_alt avg `-0.14` n `228`; crypto_major avg `-0.1398` n `8`; equity avg `0.2528` n `74`; fx avg `0.1311` n `6`; index avg `0.333` n `23`; metal avg `0.4615` n `18`; unknown avg `0.1148` n `503`
- 24h: commodity avg `-1.5` n `12`; crypto_alt avg `-0.0452` n `228`; crypto_major avg `0.7084` n `8`; equity avg `2.3285` n `74`; fx avg `0.0731` n `6`; index avg `1.2327` n `23`; metal avg `0.979` n `18`; unknown avg `-2.7752` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
