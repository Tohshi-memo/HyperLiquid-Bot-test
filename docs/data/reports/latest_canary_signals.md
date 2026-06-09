# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T07:07:26.531229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0712` n `12`; crypto_alt avg `0.1368` n `228`; crypto_major avg `0.2504` n `8`; equity avg `0.162` n `74`; fx avg `-0.0034` n `6`; index avg `0.0729` n `23`; metal avg `-0.1263` n `18`; unknown avg `0.0528` n `547`
- 1h: commodity avg `0.1015` n `12`; crypto_alt avg `0.0479` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `0.0272` n `74`; fx avg `0.0786` n `6`; index avg `0.0156` n `23`; metal avg `-0.1053` n `18`; unknown avg `0.0761` n `545`
- 4h: commodity avg `0.0017` n `12`; crypto_alt avg `1.4702` n `228`; crypto_major avg `0.9277` n `8`; equity avg `1.0501` n `74`; fx avg `0.0037` n `6`; index avg `0.465` n `23`; metal avg `0.2867` n `18`; unknown avg `0.3154` n `503`
- 24h: commodity avg `-1.3991` n `12`; crypto_alt avg `0.9478` n `228`; crypto_major avg `1.3022` n `8`; equity avg `3.2011` n `74`; fx avg `-0.0636` n `6`; index avg `1.3317` n `23`; metal avg `0.9096` n `18`; unknown avg `-2.7817` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
