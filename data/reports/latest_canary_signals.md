# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T21:37:22.085254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.9483` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.749` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.4405` n `12`; crypto_alt avg `0.3756` n `228`; crypto_major avg `0.3674` n `8`; equity avg `0.0445` n `74`; fx avg `0.0302` n `6`; index avg `0.0235` n `23`; metal avg `0.0457` n `18`; unknown avg `0.1936` n `425`
- 1h: commodity avg `-0.2003` n `12`; crypto_alt avg `1.082` n `228`; crypto_major avg `0.8761` n `8`; equity avg `0.6338` n `74`; fx avg `0.0172` n `6`; index avg `0.3951` n `23`; metal avg `0.1826` n `18`; unknown avg `1.0091` n `425`
- 4h: commodity avg `-0.1035` n `12`; crypto_alt avg `0.8613` n `228`; crypto_major avg `1.0954` n `8`; equity avg `-0.8529` n `74`; fx avg `-0.0033` n `6`; index avg `-0.9931` n `23`; metal avg `-0.6536` n `18`; unknown avg `0.3562` n `424`
- 24h: commodity avg `-1.9861` n `12`; crypto_alt avg `-5.0956` n `228`; crypto_major avg `-4.2683` n `8`; equity avg `-6.0195` n `74`; fx avg `-0.0462` n `6`; index avg `-4.2624` n `23`; metal avg `-4.454` n `18`; unknown avg `-1.6609` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
