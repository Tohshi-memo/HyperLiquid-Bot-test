# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T01:52:16.501755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3419` n `12`; crypto_alt avg `0.3583` n `228`; crypto_major avg `0.2894` n `8`; equity avg `0.2202` n `66`; fx avg `-0.0388` n `6`; index avg `0.1998` n `23`; metal avg `0.3483` n `18`; unknown avg `0.2912` n `384`
- 1h: commodity avg `-0.1589` n `12`; crypto_alt avg `0.1968` n `228`; crypto_major avg `-0.0221` n `8`; equity avg `0.1094` n `66`; fx avg `-0.052` n `6`; index avg `-0.0174` n `23`; metal avg `-0.4664` n `18`; unknown avg `0.1126` n `384`
- 4h: commodity avg `-0.2748` n `12`; crypto_alt avg `-0.3066` n `228`; crypto_major avg `-0.4322` n `8`; equity avg `-0.2119` n `66`; fx avg `-0.0418` n `6`; index avg `-0.169` n `23`; metal avg `-0.0938` n `18`; unknown avg `-0.2842` n `383`
- 24h: commodity avg `0.5992` n `12`; crypto_alt avg `-0.9845` n `228`; crypto_major avg `-0.746` n `8`; equity avg `0.0583` n `66`; fx avg `-0.105` n `6`; index avg `-0.5591` n `23`; metal avg `-2.5824` n `18`; unknown avg `0.9637` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
