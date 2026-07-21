# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T07:07:32.857648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0963` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `-0.0329` n `8`; equity avg `0.0701` n `98`; fx avg `0.0176` n `6`; index avg `0.0008` n `25`; metal avg `0.0343` n `20`; unknown avg `-0.022` n `771`
- 1h: commodity avg `0.0932` n `12`; crypto_alt avg `0.1176` n `230`; crypto_major avg `0.2015` n `8`; equity avg `0.1533` n `98`; fx avg `0.0464` n `6`; index avg `0.0067` n `25`; metal avg `0.2134` n `20`; unknown avg `0.0748` n `771`
- 4h: commodity avg `0.1106` n `12`; crypto_alt avg `0.5726` n `230`; crypto_major avg `0.387` n `8`; equity avg `1.148` n `98`; fx avg `0.0396` n `6`; index avg `0.1317` n `25`; metal avg `0.4453` n `20`; unknown avg `0.0675` n `755`
- 24h: commodity avg `-0.2745` n `12`; crypto_alt avg `3.2203` n `230`; crypto_major avg `3.113` n `8`; equity avg `1.923` n `98`; fx avg `-0.0796` n `6`; index avg `0.3602` n `25`; metal avg `0.8681` n `20`; unknown avg `0.2374` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
