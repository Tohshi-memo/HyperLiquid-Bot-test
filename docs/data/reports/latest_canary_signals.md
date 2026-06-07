# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T20:07:22.122458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1466` n `12`; crypto_alt avg `0.4362` n `228`; crypto_major avg `0.3589` n `8`; equity avg `0.0876` n `74`; fx avg `-0.0063` n `6`; index avg `0.054` n `23`; metal avg `-0.033` n `18`; unknown avg `0.0997` n `516`
- 1h: commodity avg `-0.1232` n `12`; crypto_alt avg `-0.2673` n `228`; crypto_major avg `-0.3076` n `8`; equity avg `-0.2845` n `74`; fx avg `0.0108` n `6`; index avg `-0.0718` n `23`; metal avg `-0.1248` n `18`; unknown avg `-0.0192` n `516`
- 4h: commodity avg `0.4377` n `12`; crypto_alt avg `-1.4075` n `228`; crypto_major avg `-0.6069` n `8`; equity avg `-0.5806` n `74`; fx avg `0.0133` n `6`; index avg `-0.2268` n `23`; metal avg `-0.2185` n `18`; unknown avg `0.2538` n `516`
- 24h: commodity avg `0.5882` n `12`; crypto_alt avg `1.9333` n `228`; crypto_major avg `3.1199` n `8`; equity avg `1.0442` n `74`; fx avg `-0.0541` n `6`; index avg `0.1758` n `23`; metal avg `0.2901` n `18`; unknown avg `-4.9681` n `505`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
