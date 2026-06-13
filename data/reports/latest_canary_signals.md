# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T07:07:28.985139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0724` n `12`; crypto_alt avg `-0.22` n `228`; crypto_major avg `-0.1856` n `8`; equity avg `-0.0091` n `74`; fx avg `0.0006` n `6`; index avg `-0.0041` n `23`; metal avg `0.0213` n `18`; unknown avg `-0.2418` n `643`
- 1h: commodity avg `0.0719` n `12`; crypto_alt avg `0.4366` n `228`; crypto_major avg `0.2861` n `8`; equity avg `0.1013` n `74`; fx avg `-0.0214` n `6`; index avg `0.0289` n `23`; metal avg `0.0242` n `18`; unknown avg `-0.3674` n `643`
- 4h: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.0075` n `228`; crypto_major avg `-0.2157` n `8`; equity avg `-0.3452` n `74`; fx avg `0.0015` n `6`; index avg `-0.0323` n `23`; metal avg `-0.0077` n `18`; unknown avg `-0.4902` n `619`
- 24h: commodity avg `-0.7465` n `12`; crypto_alt avg `1.2008` n `228`; crypto_major avg `0.8026` n `8`; equity avg `0.2221` n `74`; fx avg `-0.002` n `6`; index avg `1.112` n `23`; metal avg `0.8208` n `18`; unknown avg `36.6583` n `507`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
