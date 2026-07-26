# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T04:47:42.973708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.0465` n `230`; crypto_major avg `0.0181` n `8`; equity avg `0.0202` n `100`; fx avg `0.0` n `6`; index avg `-0.0006` n `25`; metal avg `0.0018` n `20`; unknown avg `0.0041` n `775`
- 1h: commodity avg `-0.055` n `12`; crypto_alt avg `0.1307` n `230`; crypto_major avg `0.1362` n `8`; equity avg `0.0467` n `100`; fx avg `0.0642` n `6`; index avg `0.0004` n `25`; metal avg `0.0117` n `20`; unknown avg `-0.0571` n `775`
- 4h: commodity avg `-0.0386` n `12`; crypto_alt avg `0.473` n `230`; crypto_major avg `0.4934` n `8`; equity avg `0.2619` n `100`; fx avg `0.0709` n `6`; index avg `0.0476` n `25`; metal avg `0.0253` n `20`; unknown avg `-0.084` n `774`
- 24h: commodity avg `-0.5273` n `12`; crypto_alt avg `0.8731` n `230`; crypto_major avg `1.4765` n `8`; equity avg `0.4755` n `100`; fx avg `0.0654` n `6`; index avg `0.132` n `25`; metal avg `0.056` n `20`; unknown avg `-0.1851` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1241`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1181`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
