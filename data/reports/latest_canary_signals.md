# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T07:07:26.181737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `12`; crypto_alt avg `0.0889` n `230`; crypto_major avg `0.2021` n `8`; equity avg `0.2194` n `100`; fx avg `0.0123` n `6`; index avg `0.0604` n `25`; metal avg `0.0816` n `20`; unknown avg `-0.0059` n `772`
- 1h: commodity avg `-0.1193` n `12`; crypto_alt avg `0.2799` n `230`; crypto_major avg `0.3816` n `8`; equity avg `0.213` n `100`; fx avg `0.0362` n `6`; index avg `0.0601` n `25`; metal avg `0.1762` n `20`; unknown avg `0.1211` n `772`
- 4h: commodity avg `-0.2904` n `12`; crypto_alt avg `0.5804` n `230`; crypto_major avg `0.6041` n `8`; equity avg `0.2261` n `100`; fx avg `0.047` n `6`; index avg `0.0702` n `25`; metal avg `0.1565` n `20`; unknown avg `0.2446` n `756`
- 24h: commodity avg `0.0759` n `12`; crypto_alt avg `-0.7976` n `230`; crypto_major avg `-1.1811` n `8`; equity avg `-1.7579` n `99`; fx avg `-0.0908` n `6`; index avg `-0.5004` n `25`; metal avg `-0.6766` n `20`; unknown avg `0.0344` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1074`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0935`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.089`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0872`, n `666`, weak_sample_signal
