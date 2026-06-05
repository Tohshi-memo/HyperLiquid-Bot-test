# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T18:26:12.118882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1226` n `12`; crypto_alt avg `-1.5201` n `228`; crypto_major avg `-1.3131` n `8`; equity avg `-0.6375` n `74`; fx avg `0.016` n `6`; index avg `-0.3226` n `23`; metal avg `-0.3414` n `18`; unknown avg `-0.7027` n `424`
- 1h: commodity avg `0.2433` n `12`; crypto_alt avg `-1.289` n `228`; crypto_major avg `-1.2187` n `8`; equity avg `-0.9616` n `74`; fx avg `-0.0175` n `6`; index avg `-0.4273` n `23`; metal avg `-0.5975` n `18`; unknown avg `-0.8045` n `424`
- 4h: commodity avg `-0.6941` n `12`; crypto_alt avg `-2.2373` n `228`; crypto_major avg `-2.324` n `8`; equity avg `-3.1475` n `74`; fx avg `-0.1204` n `6`; index avg `-1.6772` n `23`; metal avg `-1.3745` n `18`; unknown avg `-1.4223` n `424`
- 24h: commodity avg `-1.1659` n `12`; crypto_alt avg `-8.5945` n `228`; crypto_major avg `-7.1227` n `8`; equity avg `-6.9448` n `74`; fx avg `-0.0547` n `6`; index avg `-3.947` n `23`; metal avg `-4.585` n `18`; unknown avg `-2.0032` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
