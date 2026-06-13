# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T19:22:28.847475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1162` n `12`; crypto_alt avg `0.0399` n `228`; crypto_major avg `0.0063` n `8`; equity avg `0.0464` n `74`; fx avg `-0.0008` n `6`; index avg `0.0025` n `23`; metal avg `-0.004` n `18`; unknown avg `-0.3313` n `644`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.1435` n `228`; crypto_major avg `0.0521` n `8`; equity avg `0.078` n `74`; fx avg `-0.011` n `6`; index avg `0.0514` n `23`; metal avg `0.2457` n `18`; unknown avg `-0.3891` n `644`
- 4h: commodity avg `-0.2428` n `12`; crypto_alt avg `-0.66` n `228`; crypto_major avg `-0.5933` n `8`; equity avg `0.002` n `74`; fx avg `0.0268` n `6`; index avg `-0.0447` n `23`; metal avg `0.0764` n `18`; unknown avg `-0.425` n `644`
- 24h: commodity avg `-0.5844` n `12`; crypto_alt avg `1.7023` n `228`; crypto_major avg `0.1795` n `8`; equity avg `0.2688` n `74`; fx avg `0.0444` n `6`; index avg `0.5124` n `23`; metal avg `0.3712` n `18`; unknown avg `-1.9717` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
