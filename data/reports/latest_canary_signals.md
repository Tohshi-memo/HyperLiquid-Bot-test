# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T00:07:30.131249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `0.24` n `230`; crypto_major avg `0.2318` n `8`; equity avg `0.5154` n `98`; fx avg `0.0269` n `6`; index avg `0.1322` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0355` n `769`
- 1h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.1842` n `230`; crypto_major avg `0.31` n `8`; equity avg `0.5145` n `98`; fx avg `0.0279` n `6`; index avg `0.0902` n `25`; metal avg `0.0251` n `20`; unknown avg `0.131` n `767`
- 4h: commodity avg `-0.0551` n `12`; crypto_alt avg `0.3239` n `230`; crypto_major avg `0.4426` n `8`; equity avg `0.6566` n `98`; fx avg `-0.0102` n `6`; index avg `0.144` n `25`; metal avg `-0.1076` n `20`; unknown avg `0.0687` n `767`
- 24h: commodity avg `-0.0568` n `12`; crypto_alt avg `0.0978` n `230`; crypto_major avg `0.5431` n `8`; equity avg `0.9984` n `97`; fx avg `0.1118` n `6`; index avg `0.1132` n `25`; metal avg `-0.0869` n `20`; unknown avg `0.1302` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1452`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1328`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `666`, weak_sample_signal
