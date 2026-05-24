# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T19:22:15.327522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `12`; crypto_alt avg `-0.0486` n `228`; crypto_major avg `0.0047` n `8`; equity avg `0.0103` n `67`; fx avg `0.01` n `6`; index avg `0.0228` n `23`; metal avg `-0.052` n `18`; unknown avg `-0.0086` n `396`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.1843` n `228`; crypto_major avg `0.0982` n `8`; equity avg `-0.0308` n `67`; fx avg `0.0157` n `6`; index avg `0.0161` n `23`; metal avg `-0.0622` n `18`; unknown avg `-0.2672` n `396`
- 4h: commodity avg `0.3358` n `12`; crypto_alt avg `0.2782` n `228`; crypto_major avg `0.2105` n `8`; equity avg `0.0116` n `67`; fx avg `0.0219` n `6`; index avg `0.082` n `23`; metal avg `-0.0644` n `18`; unknown avg `-0.5428` n `396`
- 24h: commodity avg `-0.235` n `12`; crypto_alt avg `-0.5751` n `228`; crypto_major avg `1.513` n `8`; equity avg `1.1052` n `67`; fx avg `0.0995` n `6`; index avg `0.3351` n `23`; metal avg `0.3686` n `18`; unknown avg `0.5402` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
