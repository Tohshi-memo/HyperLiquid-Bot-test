# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T15:22:29.193132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.3909` n `228`; crypto_major avg `0.2449` n `8`; equity avg `0.0755` n `74`; fx avg `0.0` n `6`; index avg `0.0198` n `23`; metal avg `-0.1003` n `18`; unknown avg `-2.0399` n `644`
- 1h: commodity avg `-0.0714` n `12`; crypto_alt avg `0.7005` n `228`; crypto_major avg `0.3912` n `8`; equity avg `0.2167` n `74`; fx avg `0.0014` n `6`; index avg `0.0406` n `23`; metal avg `-0.0335` n `18`; unknown avg `-1.89` n `644`
- 4h: commodity avg `-0.1387` n `12`; crypto_alt avg `0.7291` n `228`; crypto_major avg `0.9464` n `8`; equity avg `0.3401` n `74`; fx avg `-0.0085` n `6`; index avg `0.1709` n `23`; metal avg `0.2047` n `18`; unknown avg `-1.8904` n `644`
- 24h: commodity avg `-0.3616` n `12`; crypto_alt avg `1.4217` n `228`; crypto_major avg `-0.034` n `8`; equity avg `-0.3915` n `74`; fx avg `0.029` n `6`; index avg `0.402` n `23`; metal avg `0.4614` n `18`; unknown avg `-1.8493` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
