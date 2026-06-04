# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T19:37:43.779501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1087` n `12`; crypto_alt avg `-0.1158` n `228`; crypto_major avg `-0.1252` n `8`; equity avg `0.1014` n `74`; fx avg `-0.0051` n `6`; index avg `0.0708` n `23`; metal avg `0.0148` n `18`; unknown avg `-0.1905` n `424`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `-0.0729` n `228`; crypto_major avg `-0.3043` n `8`; equity avg `-0.126` n `74`; fx avg `-0.0278` n `6`; index avg `0.0141` n `23`; metal avg `0.0827` n `18`; unknown avg `-0.0821` n `424`
- 4h: commodity avg `0.062` n `12`; crypto_alt avg `-0.1754` n `228`; crypto_major avg `-0.1242` n `8`; equity avg `-0.071` n `74`; fx avg `-0.048` n `6`; index avg `0.354` n `23`; metal avg `0.1235` n `18`; unknown avg `0.9696` n `424`
- 24h: commodity avg `-0.7293` n `12`; crypto_alt avg `-4.9429` n `228`; crypto_major avg `-3.4759` n `8`; equity avg `-1.0323` n `73`; fx avg `0.0042` n `6`; index avg `0.01` n `23`; metal avg `0.7531` n `18`; unknown avg `-0.0525` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
