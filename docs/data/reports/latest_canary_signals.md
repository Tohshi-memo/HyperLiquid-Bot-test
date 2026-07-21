# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T09:07:30.958119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.1696` n `230`; crypto_major avg `-0.1538` n `8`; equity avg `0.055` n `98`; fx avg `-0.0123` n `6`; index avg `0.0253` n `25`; metal avg `0.0374` n `20`; unknown avg `0.0153` n `771`
- 1h: commodity avg `0.1062` n `12`; crypto_alt avg `-0.1155` n `230`; crypto_major avg `-0.0495` n `8`; equity avg `0.2719` n `98`; fx avg `-0.0253` n `6`; index avg `0.0413` n `25`; metal avg `0.0181` n `20`; unknown avg `0.034` n `771`
- 4h: commodity avg `0.047` n `12`; crypto_alt avg `0.2211` n `230`; crypto_major avg `0.5016` n `8`; equity avg `0.914` n `98`; fx avg `0.0315` n `6`; index avg `0.0837` n `25`; metal avg `0.3717` n `20`; unknown avg `0.0694` n `755`
- 24h: commodity avg `0.1467` n `12`; crypto_alt avg `2.5286` n `230`; crypto_major avg `2.9035` n `8`; equity avg `2.1552` n `98`; fx avg `-0.0843` n `6`; index avg `0.321` n `25`; metal avg `0.6933` n `20`; unknown avg `0.2063` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0792`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
