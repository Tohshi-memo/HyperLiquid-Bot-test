# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T05:37:30.536656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0211` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `-0.0293` n `98`; fx avg `-0.0018` n `6`; index avg `0.0009` n `25`; metal avg `-0.0554` n `20`; unknown avg `-0.1487` n `769`
- 1h: commodity avg `0.0024` n `12`; crypto_alt avg `-0.682` n `230`; crypto_major avg `-0.716` n `8`; equity avg `-0.388` n `98`; fx avg `-0.0067` n `6`; index avg `-0.0821` n `25`; metal avg `-0.149` n `20`; unknown avg `0.9169` n `769`
- 4h: commodity avg `-0.0125` n `12`; crypto_alt avg `-1.0977` n `230`; crypto_major avg `-0.9878` n `8`; equity avg `-0.1216` n `98`; fx avg `-0.0157` n `6`; index avg `-0.0552` n `25`; metal avg `0.0123` n `20`; unknown avg `0.2533` n `769`
- 24h: commodity avg `-0.0441` n `12`; crypto_alt avg `-0.708` n `230`; crypto_major avg `-0.4925` n `8`; equity avg `0.0316` n `97`; fx avg `-0.0306` n `6`; index avg `0.0127` n `25`; metal avg `-0.039` n `20`; unknown avg `-0.0794` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0939`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0874`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0774`, n `666`, weak_sample_signal
