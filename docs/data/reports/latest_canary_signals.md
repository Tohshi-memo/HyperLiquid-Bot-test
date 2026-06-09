# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T19:07:42.282354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0603` n `12`; crypto_alt avg `0.1753` n `228`; crypto_major avg `0.0734` n `8`; equity avg `0.1618` n `74`; fx avg `-0.0034` n `6`; index avg `0.1826` n `23`; metal avg `0.0658` n `18`; unknown avg `0.059` n `547`
- 1h: commodity avg `-0.1533` n `12`; crypto_alt avg `0.4844` n `228`; crypto_major avg `0.2388` n `8`; equity avg `0.7269` n `74`; fx avg `-0.0209` n `6`; index avg `0.6623` n `23`; metal avg `0.3192` n `18`; unknown avg `0.0272` n `547`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `0.3708` n `228`; crypto_major avg `0.0104` n `8`; equity avg `-0.611` n `74`; fx avg `-0.0542` n `6`; index avg `-0.5179` n `23`; metal avg `-0.3517` n `18`; unknown avg `1.6931` n `547`
- 24h: commodity avg `-0.8934` n `12`; crypto_alt avg `-2.2946` n `228`; crypto_major avg `-2.9927` n `8`; equity avg `-2.0162` n `74`; fx avg `0.099` n `6`; index avg `-1.2797` n `23`; metal avg `-1.2535` n `18`; unknown avg `-1.4314` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0421`, n `668`, weak_sample_signal
