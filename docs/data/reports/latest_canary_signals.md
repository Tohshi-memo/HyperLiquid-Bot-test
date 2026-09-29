# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T19:22:30.666506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.2256` n `234`; crypto_major avg `-0.1493` n `8`; equity avg `-0.0542` n `142`; fx avg `0.0096` n `6`; index avg `-0.0038` n `26`; metal avg `-0.01` n `20`; unknown avg `-0.2232` n `962`
- 1h: commodity avg `-0.0314` n `12`; crypto_alt avg `0.3231` n `234`; crypto_major avg `0.2558` n `8`; equity avg `0.0807` n `142`; fx avg `0.002` n `6`; index avg `0.0361` n `26`; metal avg `0.062` n `20`; unknown avg `2.0897` n `960`
- 4h: commodity avg `-0.3468` n `12`; crypto_alt avg `-0.4523` n `234`; crypto_major avg `-0.0839` n `8`; equity avg `-0.0254` n `142`; fx avg `-0.0398` n `6`; index avg `0.0891` n `26`; metal avg `0.2313` n `20`; unknown avg `9.5769` n `954`
- 24h: commodity avg `-0.923` n `12`; crypto_alt avg `1.0722` n `234`; crypto_major avg `-0.1995` n `8`; equity avg `0.4918` n `142`; fx avg `-0.1629` n `6`; index avg `0.057` n `26`; metal avg `0.0813` n `20`; unknown avg `2.0769` n `826`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
