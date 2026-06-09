# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T14:07:27.428400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1392` n `12`; crypto_alt avg `-0.5503` n `228`; crypto_major avg `-0.5907` n `8`; equity avg `-0.5` n `74`; fx avg `0.0094` n `6`; index avg `-0.2979` n `23`; metal avg `-0.3022` n `18`; unknown avg `-0.2339` n `547`
- 1h: commodity avg `-0.4698` n `12`; crypto_alt avg `-0.696` n `228`; crypto_major avg `-0.9658` n `8`; equity avg `-0.3153` n `74`; fx avg `-0.0142` n `6`; index avg `-0.331` n `23`; metal avg `-0.5495` n `18`; unknown avg `-0.3302` n `547`
- 4h: commodity avg `-0.5243` n `12`; crypto_alt avg `0.3059` n `228`; crypto_major avg `-0.7361` n `8`; equity avg `-0.1475` n `74`; fx avg `0.0728` n `6`; index avg `-0.2555` n `23`; metal avg `0.0158` n `18`; unknown avg `-0.2352` n `547`
- 24h: commodity avg `-0.8567` n `12`; crypto_alt avg `-1.3542` n `228`; crypto_major avg `-1.7688` n `8`; equity avg `1.0707` n `74`; fx avg `0.1105` n `6`; index avg `0.3362` n `23`; metal avg `0.6662` n `18`; unknown avg `-1.4024` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
