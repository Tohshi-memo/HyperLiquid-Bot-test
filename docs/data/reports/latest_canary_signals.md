# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T08:37:28.756207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `-0.52` n `234`; crypto_major avg `-0.3947` n `8`; equity avg `-0.2829` n `141`; fx avg `0.0057` n `6`; index avg `-0.0195` n `26`; metal avg `-0.0041` n `20`; unknown avg `2.1395` n `945`
- 1h: commodity avg `0.4427` n `12`; crypto_alt avg `-0.9084` n `234`; crypto_major avg `-1.1026` n `8`; equity avg `-0.8771` n `141`; fx avg `0.0415` n `6`; index avg `-0.1275` n `26`; metal avg `-0.2201` n `20`; unknown avg `4.2827` n `937`
- 4h: commodity avg `0.5498` n `12`; crypto_alt avg `-0.0152` n `234`; crypto_major avg `0.0196` n `8`; equity avg `-0.8893` n `141`; fx avg `0.045` n `6`; index avg `-0.1476` n `26`; metal avg `-0.1299` n `20`; unknown avg `5.4954` n `921`
- 24h: commodity avg `0.809` n `12`; crypto_alt avg `-4.5596` n `234`; crypto_major avg `-3.8611` n `8`; equity avg `-2.7585` n `140`; fx avg `0.0027` n `6`; index avg `-0.493` n `26`; metal avg `-0.4987` n `20`; unknown avg `587.7604` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
