# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T20:37:20.609669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1052` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `-0.0751` n `8`; equity avg `0.0301` n `67`; fx avg `0.0056` n `6`; index avg `0.0071` n `23`; metal avg `-0.0389` n `18`; unknown avg `-0.0691` n `396`
- 1h: commodity avg `0.075` n `12`; crypto_alt avg `-0.2091` n `228`; crypto_major avg `-0.2806` n `8`; equity avg `0.1108` n `67`; fx avg `0.0462` n `6`; index avg `-0.0215` n `23`; metal avg `-0.0692` n `18`; unknown avg `0.0157` n `396`
- 4h: commodity avg `0.1951` n `12`; crypto_alt avg `-0.1254` n `228`; crypto_major avg `-0.1896` n `8`; equity avg `0.1952` n `67`; fx avg `0.0411` n `6`; index avg `0.0518` n `23`; metal avg `-0.1907` n `18`; unknown avg `-0.398` n `396`
- 24h: commodity avg `0.6569` n `12`; crypto_alt avg `-1.2812` n `228`; crypto_major avg `0.4866` n `8`; equity avg `0.9842` n `67`; fx avg `0.1298` n `6`; index avg `0.0427` n `23`; metal avg `0.0275` n `18`; unknown avg `0.0265` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
