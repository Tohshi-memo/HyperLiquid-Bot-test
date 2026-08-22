# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T09:37:29.404724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.1154` n `230`; crypto_major avg `-0.2842` n `8`; equity avg `-0.0055` n `121`; fx avg `-0.0033` n `6`; index avg `0.0033` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0778` n `794`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.5333` n `230`; crypto_major avg `0.61` n `8`; equity avg `0.0579` n `121`; fx avg `0.0056` n `6`; index avg `-0.0007` n `25`; metal avg `0.0191` n `20`; unknown avg `0.2613` n `794`
- 4h: commodity avg `-0.029` n `12`; crypto_alt avg `-0.2905` n `230`; crypto_major avg `-0.138` n `8`; equity avg `-0.0048` n `121`; fx avg `-0.0083` n `6`; index avg `-0.0279` n `25`; metal avg `0.0252` n `20`; unknown avg `0.2456` n `778`
- 24h: commodity avg `0.0809` n `12`; crypto_alt avg `3.4754` n `230`; crypto_major avg `3.5382` n `8`; equity avg `-0.8461` n `121`; fx avg `0.0519` n `6`; index avg `-0.0953` n `25`; metal avg `-0.1545` n `20`; unknown avg `1.5475` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
