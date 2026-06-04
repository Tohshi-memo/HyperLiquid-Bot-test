# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T22:22:21.513220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `0.2299` n `228`; crypto_major avg `0.2336` n `8`; equity avg `-0.1143` n `74`; fx avg `0.0005` n `6`; index avg `-0.0499` n `23`; metal avg `0.0622` n `18`; unknown avg `0.9824` n `424`
- 1h: commodity avg `-0.1542` n `12`; crypto_alt avg `-1.2509` n `228`; crypto_major avg `-0.5987` n `8`; equity avg `-0.2744` n `74`; fx avg `-0.0147` n `6`; index avg `-0.0236` n `23`; metal avg `0.0638` n `18`; unknown avg `0.3963` n `424`
- 4h: commodity avg `0.3293` n `12`; crypto_alt avg `-1.9812` n `228`; crypto_major avg `-0.8884` n `8`; equity avg `-0.9954` n `74`; fx avg `-0.0235` n `6`; index avg `-0.2953` n `23`; metal avg `-0.1774` n `18`; unknown avg `0.3551` n `424`
- 24h: commodity avg `-0.6434` n `12`; crypto_alt avg `-7.397` n `228`; crypto_major avg `-4.842` n `8`; equity avg `-0.605` n `73`; fx avg `0.059` n `6`; index avg `0.1918` n `23`; metal avg `1.1094` n `18`; unknown avg `-0.7271` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
