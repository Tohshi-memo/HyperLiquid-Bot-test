# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T12:54:16.268318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2154` n `12`; crypto_alt avg `-0.1125` n `228`; crypto_major avg `-0.2279` n `8`; equity avg `-0.2418` n `67`; fx avg `-0.0027` n `6`; index avg `-0.1309` n `23`; metal avg `-0.0462` n `18`; unknown avg `0.8536` n `418`
- 1h: commodity avg `-0.566` n `12`; crypto_alt avg `0.194` n `228`; crypto_major avg `-0.1848` n `8`; equity avg `-0.2703` n `67`; fx avg `0.0202` n `6`; index avg `-0.0689` n `23`; metal avg `0.1805` n `18`; unknown avg `0.8` n `418`
- 4h: commodity avg `0.0307` n `12`; crypto_alt avg `0.3777` n `228`; crypto_major avg `-0.0046` n `8`; equity avg `-0.0048` n `67`; fx avg `0.001` n `6`; index avg `-0.0442` n `23`; metal avg `-0.5039` n `18`; unknown avg `-0.2533` n `418`
- 24h: commodity avg `-1.6026` n `12`; crypto_alt avg `-1.6575` n `228`; crypto_major avg `-0.9645` n `8`; equity avg `0.5099` n `67`; fx avg `-0.0295` n `6`; index avg `0.6999` n `23`; metal avg `-1.0035` n `18`; unknown avg `1.5623` n `398`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
