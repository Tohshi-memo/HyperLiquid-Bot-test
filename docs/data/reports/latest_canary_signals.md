# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T07:07:45.366487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1236` n `12`; crypto_alt avg `-0.2172` n `228`; crypto_major avg `-0.1817` n `8`; equity avg `0.019` n `74`; fx avg `0.0047` n `6`; index avg `-0.0024` n `23`; metal avg `-0.0177` n `18`; unknown avg `-0.0824` n `556`
- 1h: commodity avg `-0.2564` n `12`; crypto_alt avg `0.0664` n `228`; crypto_major avg `0.123` n `8`; equity avg `0.3466` n `74`; fx avg `0.0454` n `6`; index avg `0.172` n `23`; metal avg `0.382` n `18`; unknown avg `-0.276` n `554`
- 4h: commodity avg `-0.6303` n `12`; crypto_alt avg `1.1282` n `228`; crypto_major avg `0.8306` n `8`; equity avg `0.7684` n `74`; fx avg `0.069` n `6`; index avg `0.3203` n `23`; metal avg `0.5581` n `18`; unknown avg `-0.0052` n `538`
- 24h: commodity avg `0.6528` n `12`; crypto_alt avg `0.6533` n `228`; crypto_major avg `0.837` n `8`; equity avg `-0.3396` n `74`; fx avg `0.0447` n `6`; index avg `-0.5376` n `23`; metal avg `-0.8381` n `18`; unknown avg `3.3414` n `535`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
