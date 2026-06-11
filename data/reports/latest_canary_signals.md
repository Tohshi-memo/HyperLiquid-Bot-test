# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T07:37:31.151411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3114` n `12`; crypto_alt avg `-0.1823` n `228`; crypto_major avg `-0.1416` n `8`; equity avg `0.058` n `74`; fx avg `-0.019` n `6`; index avg `-0.0539` n `23`; metal avg `0.012` n `18`; unknown avg `-0.013` n `556`
- 1h: commodity avg `-0.4158` n `12`; crypto_alt avg `-0.318` n `228`; crypto_major avg `-0.3463` n `8`; equity avg `0.3346` n `74`; fx avg `0.002` n `6`; index avg `0.1269` n `23`; metal avg `0.3637` n `18`; unknown avg `-0.0575` n `548`
- 4h: commodity avg `-1.0553` n `12`; crypto_alt avg `0.8892` n `228`; crypto_major avg `0.5775` n `8`; equity avg `0.8548` n `74`; fx avg `0.0568` n `6`; index avg `0.3962` n `23`; metal avg `0.8133` n `18`; unknown avg `0.1863` n `530`
- 24h: commodity avg `0.3597` n `12`; crypto_alt avg `0.4757` n `228`; crypto_major avg `0.487` n `8`; equity avg `-0.105` n `74`; fx avg `-0.0062` n `6`; index avg `-0.4734` n `23`; metal avg `-0.3631` n `18`; unknown avg `3.7182` n `527`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
