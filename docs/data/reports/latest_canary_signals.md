# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T04:52:27.319151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.0788` n `230`; crypto_major avg `0.0277` n `8`; equity avg `-0.0155` n `98`; fx avg `0.0009` n `6`; index avg `-0.0259` n `25`; metal avg `0.0026` n `20`; unknown avg `0.3457` n `771`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `0.0791` n `230`; crypto_major avg `0.0123` n `8`; equity avg `-0.0387` n `98`; fx avg `0.0129` n `6`; index avg `-0.0151` n `25`; metal avg `0.0221` n `20`; unknown avg `0.7765` n `771`
- 4h: commodity avg `-0.0745` n `12`; crypto_alt avg `0.3585` n `230`; crypto_major avg `0.2973` n `8`; equity avg `1.0632` n `98`; fx avg `-0.022` n `6`; index avg `0.2464` n `25`; metal avg `0.2447` n `20`; unknown avg `0.0795` n `771`
- 24h: commodity avg `-0.3578` n `12`; crypto_alt avg `2.2367` n `230`; crypto_major avg `1.8448` n `8`; equity avg `0.8282` n `98`; fx avg `-0.116` n `6`; index avg `0.1712` n `25`; metal avg `0.3308` n `20`; unknown avg `0.0626` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0901`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0737`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `666`, weak_sample_signal
