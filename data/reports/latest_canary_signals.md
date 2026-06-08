# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T15:52:35.195261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.0352` n `228`; crypto_major avg `0.1459` n `8`; equity avg `0.2251` n `74`; fx avg `0.0064` n `6`; index avg `0.0865` n `23`; metal avg `0.1925` n `18`; unknown avg `-0.0276` n `517`
- 1h: commodity avg `-0.1585` n `12`; crypto_alt avg `0.1361` n `228`; crypto_major avg `0.4183` n `8`; equity avg `0.0782` n `74`; fx avg `0.0162` n `6`; index avg `0.1198` n `23`; metal avg `0.4103` n `18`; unknown avg `-0.1152` n `517`
- 4h: commodity avg `0.2209` n `12`; crypto_alt avg `0.6544` n `228`; crypto_major avg `1.2668` n `8`; equity avg `1.0555` n `74`; fx avg `0.0174` n `6`; index avg `0.494` n `23`; metal avg `-0.0507` n `18`; unknown avg `-2.0699` n `517`
- 24h: commodity avg `-0.5027` n `12`; crypto_alt avg `2.3787` n `228`; crypto_major avg `3.9804` n `8`; equity avg `2.7146` n `74`; fx avg `-0.2317` n `6`; index avg `1.2374` n `23`; metal avg `0.2408` n `18`; unknown avg `-3.0671` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
