# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T19:37:27.447541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.083` n `12`; crypto_alt avg `-0.1602` n `228`; crypto_major avg `-0.1464` n `8`; equity avg `0.0218` n `74`; fx avg `-0.0077` n `6`; index avg `-0.0158` n `23`; metal avg `-0.017` n `18`; unknown avg `3.7472` n `515`
- 1h: commodity avg `-0.1876` n `12`; crypto_alt avg `-0.1309` n `228`; crypto_major avg `-0.2826` n `8`; equity avg `0.1031` n `74`; fx avg `-0.1141` n `6`; index avg `-0.0584` n `23`; metal avg `-0.0062` n `18`; unknown avg `-0.3462` n `515`
- 4h: commodity avg `-0.0566` n `12`; crypto_alt avg `-0.5719` n `228`; crypto_major avg `-0.8639` n `8`; equity avg `0.1588` n `74`; fx avg `0.1049` n `6`; index avg `-0.1159` n `23`; metal avg `0.1139` n `18`; unknown avg `-3.2602` n `515`
- 24h: commodity avg `0.2939` n `12`; crypto_alt avg `0.3952` n `228`; crypto_major avg `0.1044` n `8`; equity avg `-1.1542` n `74`; fx avg `0.0751` n `6`; index avg `-0.2704` n `23`; metal avg `-0.6247` n `18`; unknown avg `0.9662` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
