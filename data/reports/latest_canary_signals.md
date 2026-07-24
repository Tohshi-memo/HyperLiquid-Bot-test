# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T15:22:31.144617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2813` n `12`; crypto_alt avg `0.3023` n `230`; crypto_major avg `0.3359` n `8`; equity avg `0.4292` n `100`; fx avg `0.0055` n `6`; index avg `0.1295` n `25`; metal avg `0.1433` n `20`; unknown avg `0.1395` n `773`
- 1h: commodity avg `-0.2032` n `12`; crypto_alt avg `0.4143` n `230`; crypto_major avg `0.6274` n `8`; equity avg `0.3756` n `100`; fx avg `0.0085` n `6`; index avg `0.1483` n `25`; metal avg `0.201` n `20`; unknown avg `13.6675` n `773`
- 4h: commodity avg `-0.1096` n `12`; crypto_alt avg `-0.8991` n `230`; crypto_major avg `-0.8251` n `8`; equity avg `-1.8102` n `100`; fx avg `0.0023` n `6`; index avg `-0.0873` n `25`; metal avg `0.0715` n `20`; unknown avg `13.2233` n `773`
- 24h: commodity avg `-0.6442` n `12`; crypto_alt avg `-1.3128` n `230`; crypto_major avg `-1.0607` n `8`; equity avg `-1.5364` n `100`; fx avg `-0.1117` n `6`; index avg `-0.0677` n `25`; metal avg `0.2365` n `20`; unknown avg `13.979` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1206`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1202`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1045`, n `666`, weak_sample_signal
