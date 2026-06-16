# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T07:52:34.663484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.0029` n `228`; crypto_major avg `0.11` n `8`; equity avg `-0.0149` n `77`; fx avg `0.0061` n `6`; index avg `-0.0045` n `23`; metal avg `0.0995` n `18`; unknown avg `-0.1219` n `687`
- 1h: commodity avg `-0.5212` n `12`; crypto_alt avg `0.2913` n `228`; crypto_major avg `0.1029` n `8`; equity avg `0.0106` n `77`; fx avg `0.055` n `6`; index avg `0.0422` n `23`; metal avg `0.3513` n `18`; unknown avg `-0.1019` n `687`
- 4h: commodity avg `-0.3071` n `12`; crypto_alt avg `0.5303` n `228`; crypto_major avg `0.9133` n `8`; equity avg `0.2138` n `77`; fx avg `-0.0199` n `6`; index avg `-0.0614` n `23`; metal avg `0.1688` n `18`; unknown avg `0.6997` n `647`
- 24h: commodity avg `0.3531` n `12`; crypto_alt avg `1.0344` n `228`; crypto_major avg `3.0261` n `8`; equity avg `1.2834` n `76`; fx avg `-0.1166` n `6`; index avg `0.4102` n `23`; metal avg `0.0843` n `18`; unknown avg `1.3438` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
