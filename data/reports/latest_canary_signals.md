# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T07:22:28.295762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.034` n `12`; crypto_alt avg `-0.1035` n `230`; crypto_major avg `0.0011` n `8`; equity avg `-0.061` n `98`; fx avg `-0.0115` n `6`; index avg `-0.0163` n `25`; metal avg `-0.0144` n `20`; unknown avg `-0.0115` n `771`
- 1h: commodity avg `0.1233` n `12`; crypto_alt avg `-0.0005` n `230`; crypto_major avg `0.14` n `8`; equity avg `0.0871` n `98`; fx avg `0.023` n `6`; index avg `0.005` n `25`; metal avg `0.1146` n `20`; unknown avg `0.0391` n `771`
- 4h: commodity avg `0.1576` n `12`; crypto_alt avg `0.4763` n `230`; crypto_major avg `0.5535` n `8`; equity avg `0.8744` n `98`; fx avg `0.0217` n `6`; index avg `0.0878` n `25`; metal avg `0.4391` n `20`; unknown avg `0.0623` n `755`
- 24h: commodity avg `-0.1229` n `12`; crypto_alt avg `2.8729` n `230`; crypto_major avg `2.9499` n `8`; equity avg `1.8418` n `98`; fx avg `-0.1082` n `6`; index avg `0.3378` n `25`; metal avg `0.83` n `20`; unknown avg `0.2379` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0778`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
