# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T01:22:15.878077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0641` n `12`; crypto_alt avg `0.1056` n `228`; crypto_major avg `0.0706` n `8`; equity avg `-0.0023` n `67`; fx avg `-0.0149` n `6`; index avg `-0.0024` n `23`; metal avg `0.0154` n `18`; unknown avg `-0.2284` n `407`
- 1h: commodity avg `0.1161` n `12`; crypto_alt avg `-0.7466` n `228`; crypto_major avg `-0.4881` n `8`; equity avg `-0.0834` n `67`; fx avg `-0.0677` n `6`; index avg `0.0405` n `23`; metal avg `0.0298` n `18`; unknown avg `1.7422` n `407`
- 4h: commodity avg `0.4807` n `12`; crypto_alt avg `-1.3793` n `228`; crypto_major avg `-0.9272` n `8`; equity avg `-0.8609` n `67`; fx avg `-0.1075` n `6`; index avg `-0.3941` n `23`; metal avg `-0.6372` n `18`; unknown avg `1.4564` n `405`
- 24h: commodity avg `-0.0116` n `12`; crypto_alt avg `0.0998` n `228`; crypto_major avg `-0.9278` n `8`; equity avg `-0.1514` n `67`; fx avg `-0.0186` n `6`; index avg `0.1247` n `23`; metal avg `-0.1231` n `18`; unknown avg `0.5656` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
