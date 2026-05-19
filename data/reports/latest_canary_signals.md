# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T01:37:13.972272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1143` n `12`; crypto_alt avg `0.0614` n `228`; crypto_major avg `0.0816` n `8`; equity avg `0.3042` n `66`; fx avg `-0.0017` n `6`; index avg `0.072` n `23`; metal avg `0.0922` n `18`; unknown avg `-0.1981` n `383`
- 1h: commodity avg `0.088` n `12`; crypto_alt avg `-0.443` n `228`; crypto_major avg `-0.39` n `8`; equity avg `-0.5869` n `66`; fx avg `0.0361` n `6`; index avg `-0.3468` n `23`; metal avg `-0.5396` n `18`; unknown avg `-0.1366` n `383`
- 4h: commodity avg `0.1953` n `12`; crypto_alt avg `0.2557` n `228`; crypto_major avg `-0.1222` n `8`; equity avg `-0.2118` n `66`; fx avg `0.1392` n `6`; index avg `-0.283` n `23`; metal avg `-0.2578` n `18`; unknown avg `-0.5024` n `383`
- 24h: commodity avg `-0.0763` n `12`; crypto_alt avg `1.4724` n `228`; crypto_major avg `0.5578` n `8`; equity avg `-0.0913` n `66`; fx avg `0.2374` n `6`; index avg `0.0248` n `23`; metal avg `1.7687` n `18`; unknown avg `0.39` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
