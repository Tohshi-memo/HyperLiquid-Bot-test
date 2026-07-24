# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T06:37:24.970153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `0.0829` n `230`; crypto_major avg `0.0848` n `8`; equity avg `-0.032` n `100`; fx avg `0.0091` n `6`; index avg `0.0045` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0342` n `772`
- 1h: commodity avg `-0.1442` n `12`; crypto_alt avg `0.3765` n `230`; crypto_major avg `0.3247` n `8`; equity avg `-0.1443` n `100`; fx avg `0.0269` n `6`; index avg `-0.0185` n `25`; metal avg `0.0485` n `20`; unknown avg `0.0161` n `756`
- 4h: commodity avg `-0.1524` n `12`; crypto_alt avg `0.7394` n `230`; crypto_major avg `0.7271` n `8`; equity avg `-0.0247` n `100`; fx avg `0.0451` n `6`; index avg `-0.0147` n `25`; metal avg `0.013` n `20`; unknown avg `0.2502` n `756`
- 24h: commodity avg `0.2825` n `12`; crypto_alt avg `-0.7711` n `230`; crypto_major avg `-1.4101` n `8`; equity avg `-2.0551` n `99`; fx avg `-0.0824` n `6`; index avg `-0.5546` n `25`; metal avg `-0.8905` n `20`; unknown avg `0.0066` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1077`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0936`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0887`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0878`, n `666`, weak_sample_signal
