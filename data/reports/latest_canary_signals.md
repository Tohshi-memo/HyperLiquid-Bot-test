# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T16:37:14.303057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2565` n `12`; crypto_alt avg `-0.3409` n `228`; crypto_major avg `-0.2628` n `8`; equity avg `0.0033` n `67`; fx avg `0.0098` n `6`; index avg `-0.0069` n `23`; metal avg `-0.039` n `18`; unknown avg `-0.0169` n `396`
- 1h: commodity avg `0.1075` n `12`; crypto_alt avg `-0.0419` n `228`; crypto_major avg `-0.0709` n `8`; equity avg `0.0265` n `67`; fx avg `0.0234` n `6`; index avg `0.0184` n `23`; metal avg `0.0586` n `18`; unknown avg `-0.2809` n `396`
- 4h: commodity avg `0.7211` n `12`; crypto_alt avg `-0.5604` n `228`; crypto_major avg `-0.6357` n `8`; equity avg `-0.3951` n `67`; fx avg `0.0434` n `6`; index avg `-0.3599` n `23`; metal avg `-0.4063` n `18`; unknown avg `0.3472` n `396`
- 24h: commodity avg `-1.2132` n `12`; crypto_alt avg `0.4257` n `228`; crypto_major avg `2.2365` n `8`; equity avg `1.5773` n `67`; fx avg `0.0943` n `6`; index avg `0.5883` n `23`; metal avg `0.6478` n `18`; unknown avg `0.9245` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
