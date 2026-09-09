# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T20:07:29.157456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0391` n `12`; crypto_alt avg `-0.1743` n `233`; crypto_major avg `-0.1327` n `8`; equity avg `-0.0463` n `134`; fx avg `0.0052` n `6`; index avg `-0.004` n `26`; metal avg `-0.0269` n `20`; unknown avg `42.5631` n `767`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `-1.0894` n `233`; crypto_major avg `-0.8099` n `8`; equity avg `-0.1879` n `134`; fx avg `0.0024` n `6`; index avg `-0.0087` n `26`; metal avg `-0.0503` n `20`; unknown avg `41.0319` n `767`
- 4h: commodity avg `-0.0955` n `12`; crypto_alt avg `-1.0475` n `233`; crypto_major avg `-0.9504` n `8`; equity avg `-0.3488` n `134`; fx avg `0.0373` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0741` n `20`; unknown avg `0.9195` n `761`
- 24h: commodity avg `0.1383` n `12`; crypto_alt avg `-1.6353` n `233`; crypto_major avg `-1.0416` n `8`; equity avg `-0.3182` n `134`; fx avg `-0.0358` n `6`; index avg `-0.1362` n `26`; metal avg `0.5083` n `20`; unknown avg `5.4244` n `687`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
