# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T17:37:17.708610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0599` n `12`; crypto_alt avg `0.1589` n `228`; crypto_major avg `0.128` n `8`; equity avg `0.0358` n `67`; fx avg `-0.0006` n `6`; index avg `-0.0004` n `23`; metal avg `0.0207` n `18`; unknown avg `0.1417` n `396`
- 1h: commodity avg `0.1062` n `12`; crypto_alt avg `0.4362` n `228`; crypto_major avg `0.2208` n `8`; equity avg `0.0893` n `67`; fx avg `-0.0053` n `6`; index avg `-0.0173` n `23`; metal avg `-0.0568` n `18`; unknown avg `-0.0219` n `396`
- 4h: commodity avg `0.6169` n `12`; crypto_alt avg `-0.0799` n `228`; crypto_major avg `-0.5133` n `8`; equity avg `-0.2868` n `67`; fx avg `0.0126` n `6`; index avg `-0.3136` n `23`; metal avg `-0.2784` n `18`; unknown avg `-0.2133` n `396`
- 24h: commodity avg `-1.2477` n `12`; crypto_alt avg `0.5979` n `228`; crypto_major avg `2.4231` n `8`; equity avg `1.6127` n `67`; fx avg `0.0919` n `6`; index avg `0.5429` n `23`; metal avg `0.548` n `18`; unknown avg `1.001` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
