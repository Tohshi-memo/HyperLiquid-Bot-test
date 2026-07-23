# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T20:33:34.183258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.007` n `230`; crypto_major avg `-0.0495` n `8`; equity avg `-0.0423` n `100`; fx avg `0.0103` n `6`; index avg `-0.0012` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.0857` n `772`
- 1h: commodity avg `0.0221` n `12`; crypto_alt avg `0.3016` n `230`; crypto_major avg `0.2521` n `8`; equity avg `0.4808` n `100`; fx avg `0.0049` n `6`; index avg `0.112` n `25`; metal avg `0.0305` n `20`; unknown avg `0.2225` n `772`
- 4h: commodity avg `-0.1002` n `12`; crypto_alt avg `-0.1522` n `230`; crypto_major avg `0.0298` n `8`; equity avg `-0.0666` n `100`; fx avg `0.0246` n `6`; index avg `0.0417` n `25`; metal avg `-0.0167` n `20`; unknown avg `-0.3521` n `772`
- 24h: commodity avg `0.858` n `12`; crypto_alt avg `-1.2791` n `230`; crypto_major avg `-1.8163` n `8`; equity avg `-0.9511` n `99`; fx avg `-0.0623` n `6`; index avg `-0.2428` n `25`; metal avg `-0.7969` n `20`; unknown avg `-0.3226` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
