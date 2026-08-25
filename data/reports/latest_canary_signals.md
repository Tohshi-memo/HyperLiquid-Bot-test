# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T06:37:44.706313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0482` n `12`; crypto_alt avg `-0.3993` n `231`; crypto_major avg `-0.4363` n `8`; equity avg `-0.0535` n `122`; fx avg `0.0161` n `6`; index avg `0.0141` n `25`; metal avg `0.0223` n `20`; unknown avg `-0.0491` n `794`
- 1h: commodity avg `-0.1303` n `12`; crypto_alt avg `-0.6044` n `231`; crypto_major avg `-0.5915` n `8`; equity avg `0.0933` n `122`; fx avg `0.0332` n `6`; index avg `0.0557` n `25`; metal avg `0.0511` n `20`; unknown avg `-0.1518` n `778`
- 4h: commodity avg `-0.2993` n `12`; crypto_alt avg `-0.3174` n `231`; crypto_major avg `-0.4887` n `8`; equity avg `0.8992` n `122`; fx avg `0.0363` n `6`; index avg `0.1749` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.1729` n `778`
- 24h: commodity avg `-0.1194` n `12`; crypto_alt avg `1.7644` n `231`; crypto_major avg `2.5314` n `8`; equity avg `0.335` n `122`; fx avg `0.0507` n `6`; index avg `0.0762` n `25`; metal avg `-0.1715` n `20`; unknown avg `0.5018` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
