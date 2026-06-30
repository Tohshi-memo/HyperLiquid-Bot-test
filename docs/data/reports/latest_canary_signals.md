# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T18:37:43.296070+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.7` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0666` n `12`; crypto_alt avg `-0.3047` n `228`; crypto_major avg `-0.306` n `8`; equity avg `-0.0071` n `88`; fx avg `0.0024` n `6`; index avg `-0.006` n `23`; metal avg `-0.0183` n `20`; unknown avg `-0.0585` n `765`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `-0.131` n `228`; crypto_major avg `0.052` n `8`; equity avg `0.0776` n `88`; fx avg `-0.004` n `6`; index avg `0.0003` n `23`; metal avg `0.0673` n `20`; unknown avg `-0.0176` n `765`
- 4h: commodity avg `-0.3112` n `12`; crypto_alt avg `-0.3478` n `228`; crypto_major avg `-0.1064` n `8`; equity avg `0.2633` n `88`; fx avg `0.0227` n `6`; index avg `0.0707` n `23`; metal avg `-0.3069` n `20`; unknown avg `-0.2461` n `765`
- 24h: commodity avg `0.0372` n `12`; crypto_alt avg `-2.4985` n `228`; crypto_major avg `-2.3012` n `8`; equity avg `1.2272` n `88`; fx avg `0.141` n `6`; index avg `0.3147` n `23`; metal avg `0.1796` n `20`; unknown avg `8.3573` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
