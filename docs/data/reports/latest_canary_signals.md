# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T20:52:23.964540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0881` n `12`; crypto_alt avg `-0.3204` n `228`; crypto_major avg `-0.1798` n `8`; equity avg `-0.221` n `74`; fx avg `0.0111` n `6`; index avg `-0.0699` n `23`; metal avg `-0.1525` n `18`; unknown avg `-0.0069` n `550`
- 1h: commodity avg `0.3118` n `12`; crypto_alt avg `-0.3898` n `228`; crypto_major avg `-0.2619` n `8`; equity avg `-0.6514` n `74`; fx avg `-0.0129` n `6`; index avg `-0.2212` n `23`; metal avg `-0.4095` n `18`; unknown avg `-0.0258` n `550`
- 4h: commodity avg `-0.0389` n `12`; crypto_alt avg `-1.5925` n `228`; crypto_major avg `-1.2905` n `8`; equity avg `-1.5202` n `74`; fx avg `-0.0414` n `6`; index avg `-0.8563` n `23`; metal avg `-1.3554` n `18`; unknown avg `-0.0762` n `548`
- 24h: commodity avg `1.1727` n `12`; crypto_alt avg `-2.5904` n `228`; crypto_major avg `-2.9127` n `8`; equity avg `-2.5144` n `74`; fx avg `-0.0168` n `6`; index avg `-1.8338` n `23`; metal avg `-2.6862` n `18`; unknown avg `-0.5174` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
