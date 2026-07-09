# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T22:52:31.534797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.0603` n `229`; crypto_major avg `-0.0039` n `8`; equity avg `0.0381` n `91`; fx avg `0.0057` n `6`; index avg `0.0175` n `25`; metal avg `-0.0032` n `20`; unknown avg `-0.0475` n `765`
- 1h: commodity avg `-0.0568` n `12`; crypto_alt avg `0.0168` n `229`; crypto_major avg `-0.0093` n `8`; equity avg `0.0908` n `91`; fx avg `-0.0047` n `6`; index avg `0.0248` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.1498` n `765`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.2336` n `229`; crypto_major avg `-0.0386` n `8`; equity avg `-0.2352` n `91`; fx avg `0.0016` n `6`; index avg `0.0098` n `25`; metal avg `-0.143` n `20`; unknown avg `-0.421` n `765`
- 24h: commodity avg `-1.1574` n `12`; crypto_alt avg `1.0219` n `229`; crypto_major avg `0.6421` n `8`; equity avg `1.6063` n `91`; fx avg `0.0424` n `6`; index avg `0.3498` n `25`; metal avg `0.6006` n `20`; unknown avg `-0.1716` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
