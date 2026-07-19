# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T22:37:30.384900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.1111` n `230`; crypto_major avg `-0.2027` n `8`; equity avg `-0.0598` n `98`; fx avg `0.0042` n `6`; index avg `-0.0177` n `25`; metal avg `-0.0125` n `20`; unknown avg `1.045` n `769`
- 1h: commodity avg `0.0436` n `12`; crypto_alt avg `0.2017` n `230`; crypto_major avg `0.1977` n `8`; equity avg `0.0806` n `98`; fx avg `-0.0485` n `6`; index avg `0.0262` n `25`; metal avg `-0.1094` n `20`; unknown avg `0.5918` n `769`
- 4h: commodity avg `0.0617` n `12`; crypto_alt avg `0.4348` n `230`; crypto_major avg `0.3797` n `8`; equity avg `0.2461` n `98`; fx avg `0.0183` n `6`; index avg `0.0671` n `25`; metal avg `-0.125` n `20`; unknown avg `0.3535` n `769`
- 24h: commodity avg `0.0141` n `12`; crypto_alt avg `0.0616` n `230`; crypto_major avg `0.3604` n `8`; equity avg `0.5755` n `97`; fx avg `0.0799` n `6`; index avg `0.0072` n `25`; metal avg `-0.1069` n `20`; unknown avg `-0.0894` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1419`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1387`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0968`, n `666`, weak_sample_signal
