# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T08:52:44.441009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `0.1468` n `228`; crypto_major avg `0.228` n `8`; equity avg `0.1062` n `74`; fx avg `-0.006` n `6`; index avg `0.0264` n `23`; metal avg `-0.0885` n `18`; unknown avg `-0.1055` n `547`
- 1h: commodity avg `-0.264` n `12`; crypto_alt avg `0.0877` n `228`; crypto_major avg `0.0992` n `8`; equity avg `0.1696` n `74`; fx avg `0.0487` n `6`; index avg `0.2726` n `23`; metal avg `0.1056` n `18`; unknown avg `0.0125` n `547`
- 4h: commodity avg `-0.148` n `12`; crypto_alt avg `0.3296` n `228`; crypto_major avg `0.0123` n `8`; equity avg `0.2377` n `74`; fx avg `0.0807` n `6`; index avg `0.2662` n `23`; metal avg `0.4635` n `18`; unknown avg `0.1994` n `503`
- 24h: commodity avg `-1.3263` n `12`; crypto_alt avg `0.8631` n `228`; crypto_major avg `1.3571` n `8`; equity avg `2.6115` n `74`; fx avg `0.0573` n `6`; index avg `1.2219` n `23`; metal avg `0.9581` n `18`; unknown avg `-2.6032` n `503`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
