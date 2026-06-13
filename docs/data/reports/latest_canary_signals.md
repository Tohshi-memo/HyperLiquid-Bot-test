# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T06:01:34.995712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.26` n `228`; crypto_major avg `0.217` n `8`; equity avg `0.0255` n `74`; fx avg `0.0` n `6`; index avg `-0.0399` n `23`; metal avg `0.0179` n `18`; unknown avg `0.1069` n `627`
- 1h: commodity avg `-0.0435` n `12`; crypto_alt avg `0.0161` n `228`; crypto_major avg `0.1263` n `8`; equity avg `-0.0618` n `74`; fx avg `0.0003` n `6`; index avg `0.0521` n `23`; metal avg `0.0227` n `18`; unknown avg `-0.0995` n `627`
- 4h: commodity avg `-0.1257` n `12`; crypto_alt avg `-0.651` n `228`; crypto_major avg `-0.72` n `8`; equity avg `-0.406` n `74`; fx avg `0.0291` n `6`; index avg `0.0016` n `23`; metal avg `-0.0616` n `18`; unknown avg `-0.4822` n `619`
- 24h: commodity avg `-0.5741` n `12`; crypto_alt avg `0.2921` n `228`; crypto_major avg `-0.2007` n `8`; equity avg `-0.4296` n `74`; fx avg `0.0372` n `6`; index avg `0.8962` n `23`; metal avg `0.6837` n `18`; unknown avg `36.3426` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
