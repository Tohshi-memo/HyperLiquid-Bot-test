# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T00:07:31.006350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `13`; crypto_alt avg `-0.0497` n `235`; crypto_major avg `-0.0343` n `8`; equity avg `-0.0052` n `150`; fx avg `0.0016` n `6`; index avg `0.0006` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.798` n `1109`
- 1h: commodity avg `0.0655` n `13`; crypto_alt avg `-0.0112` n `235`; crypto_major avg `-0.0789` n `8`; equity avg `-0.0227` n `150`; fx avg `0.0073` n `6`; index avg `0.0018` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.9476` n `1109`
- 4h: commodity avg `0.2274` n `13`; crypto_alt avg `-0.0435` n `235`; crypto_major avg `-0.1496` n `8`; equity avg `0.0026` n `150`; fx avg `0.0023` n `6`; index avg `0.0034` n `26`; metal avg `0.0124` n `20`; unknown avg `1.2493` n `1079`
- 24h: commodity avg `0.0964` n `13`; crypto_alt avg `1.7656` n `235`; crypto_major avg `0.7842` n `8`; equity avg `0.1756` n `150`; fx avg `-0.0069` n `6`; index avg `0.0142` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.3437` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
