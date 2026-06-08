# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T18:52:28.891322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0265` n `12`; crypto_alt avg `-0.0424` n `228`; crypto_major avg `0.1047` n `8`; equity avg `-0.0083` n `74`; fx avg `-0.0054` n `6`; index avg `-0.0001` n `23`; metal avg `-0.0243` n `18`; unknown avg `0.0013` n `517`
- 1h: commodity avg `-0.0721` n `12`; crypto_alt avg `-0.0468` n `228`; crypto_major avg `0.2257` n `8`; equity avg `-0.0371` n `74`; fx avg `-0.0058` n `6`; index avg `0.0031` n `23`; metal avg `0.0248` n `18`; unknown avg `0.0419` n `517`
- 4h: commodity avg `-0.2623` n `12`; crypto_alt avg `0.2495` n `228`; crypto_major avg `0.0758` n `8`; equity avg `-0.311` n `74`; fx avg `-0.0084` n `6`; index avg `-0.1664` n `23`; metal avg `0.1349` n `18`; unknown avg `-0.1695` n `517`
- 24h: commodity avg `-0.8124` n `12`; crypto_alt avg `2.7286` n `228`; crypto_major avg `3.2484` n `8`; equity avg `2.4093` n `74`; fx avg `-0.2815` n `6`; index avg `1.1687` n `23`; metal avg `-0.0428` n `18`; unknown avg `-1.955` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
