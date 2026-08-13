# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T10:22:26.804007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0396` n `12`; crypto_alt avg `-0.0074` n `230`; crypto_major avg `-0.0503` n `8`; equity avg `-0.0232` n `113`; fx avg `-0.0007` n `6`; index avg `0.002` n `25`; metal avg `0.0465` n `20`; unknown avg `-0.0228` n `787`
- 1h: commodity avg `0.0755` n `12`; crypto_alt avg `0.0268` n `230`; crypto_major avg `-0.0174` n `8`; equity avg `0.2175` n `113`; fx avg `0.0154` n `6`; index avg `0.0362` n `25`; metal avg `0.0882` n `20`; unknown avg `-0.0807` n `787`
- 4h: commodity avg `-0.2581` n `12`; crypto_alt avg `0.0291` n `230`; crypto_major avg `-0.2968` n `8`; equity avg `-0.4079` n `113`; fx avg `0.0611` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0135` n `20`; unknown avg `-0.1026` n `787`
- 24h: commodity avg `-0.264` n `12`; crypto_alt avg `-0.6001` n `230`; crypto_major avg `-0.4232` n `8`; equity avg `1.2541` n `113`; fx avg `0.0508` n `6`; index avg `0.1487` n `25`; metal avg `-0.5335` n `20`; unknown avg `0.0922` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2334`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
