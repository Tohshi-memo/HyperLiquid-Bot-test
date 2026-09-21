# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T03:22:30.732518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0347` n `12`; crypto_alt avg `0.3326` n `234`; crypto_major avg `0.1339` n `8`; equity avg `0.0241` n `140`; fx avg `0.0024` n `6`; index avg `0.0086` n `26`; metal avg `0.0118` n `20`; unknown avg `-0.2061` n `944`
- 1h: commodity avg `-0.0366` n `12`; crypto_alt avg `0.8428` n `234`; crypto_major avg `0.074` n `8`; equity avg `0.083` n `140`; fx avg `-0.0313` n `6`; index avg `0.031` n `26`; metal avg `-0.0137` n `20`; unknown avg `-0.2861` n `942`
- 4h: commodity avg `-0.4149` n `12`; crypto_alt avg `0.8544` n `234`; crypto_major avg `0.6258` n `8`; equity avg `0.3728` n `140`; fx avg `-0.0932` n `6`; index avg `0.0741` n `26`; metal avg `-0.0092` n `20`; unknown avg `16.7252` n `935`
- 24h: commodity avg `-0.6543` n `12`; crypto_alt avg `2.9647` n `234`; crypto_major avg `2.4125` n `8`; equity avg `1.069` n `140`; fx avg `-0.0457` n `6`; index avg `0.2086` n `26`; metal avg `0.0407` n `20`; unknown avg `3.5708` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
