# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T02:22:29.531095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2069` n `12`; crypto_alt avg `-0.3215` n `228`; crypto_major avg `-0.3974` n `8`; equity avg `-0.109` n `74`; fx avg `0.0013` n `6`; index avg `0.0016` n `23`; metal avg `0.0701` n `18`; unknown avg `-0.2492` n `547`
- 1h: commodity avg `-0.0338` n `12`; crypto_alt avg `-0.4779` n `228`; crypto_major avg `-0.6404` n `8`; equity avg `-0.4829` n `74`; fx avg `0.0506` n `6`; index avg `-0.1195` n `23`; metal avg `-0.378` n `18`; unknown avg `-0.2966` n `547`
- 4h: commodity avg `-0.0843` n `12`; crypto_alt avg `-0.5562` n `228`; crypto_major avg `-1.0732` n `8`; equity avg `-0.4132` n `74`; fx avg `-0.0313` n `6`; index avg `-0.1412` n `23`; metal avg `-1.2911` n `18`; unknown avg `-0.4665` n `547`
- 24h: commodity avg `-0.7355` n `12`; crypto_alt avg `0.2122` n `228`; crypto_major avg `-2.323` n `8`; equity avg `-2.3108` n `74`; fx avg `0.121` n `6`; index avg `-0.9219` n `23`; metal avg `-2.5751` n `18`; unknown avg `-0.3238` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0394`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0349`, n `668`, weak_sample_signal
