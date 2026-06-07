# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T21:52:20.388066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1605` n `12`; crypto_alt avg `-0.0623` n `228`; crypto_major avg `-0.0605` n `8`; equity avg `-0.052` n `74`; fx avg `-0.0057` n `6`; index avg `-0.0098` n `23`; metal avg `-0.0072` n `18`; unknown avg `0.0002` n `516`
- 1h: commodity avg `0.4175` n `12`; crypto_alt avg `-0.5153` n `228`; crypto_major avg `-0.3761` n `8`; equity avg `0.116` n `74`; fx avg `0.0061` n `6`; index avg `0.1098` n `23`; metal avg `0.02` n `18`; unknown avg `0.0243` n `516`
- 4h: commodity avg `0.5431` n `12`; crypto_alt avg `-1.3959` n `228`; crypto_major avg `-0.838` n `8`; equity avg `-0.505` n `74`; fx avg `-0.0237` n `6`; index avg `-0.073` n `23`; metal avg `-0.3097` n `18`; unknown avg `0.1964` n `516`
- 24h: commodity avg `0.6627` n `12`; crypto_alt avg `1.2329` n `228`; crypto_major avg `2.616` n `8`; equity avg `1.2038` n `74`; fx avg `-0.0625` n `6`; index avg `0.2545` n `23`; metal avg `0.3108` n `18`; unknown avg `-4.822` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
