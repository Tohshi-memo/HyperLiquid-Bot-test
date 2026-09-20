# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T07:37:31.249442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `-0.1546` n `234`; crypto_major avg `-0.0471` n `8`; equity avg `0.0129` n `140`; fx avg `0.0153` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.3362` n `943`
- 1h: commodity avg `0.0292` n `12`; crypto_alt avg `-0.3052` n `234`; crypto_major avg `-0.06` n `8`; equity avg `0.015` n `140`; fx avg `0.0103` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0048` n `20`; unknown avg `0.296` n `941`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.2251` n `234`; crypto_major avg `0.035` n `8`; equity avg `0.001` n `140`; fx avg `0.0081` n `6`; index avg `-0.0186` n `26`; metal avg `0.0058` n `20`; unknown avg `17.9043` n `895`
- 24h: commodity avg `0.2496` n `12`; crypto_alt avg `-0.2851` n `234`; crypto_major avg `-1.688` n `8`; equity avg `-0.1888` n `140`; fx avg `-0.0464` n `6`; index avg `-0.0599` n `26`; metal avg `0.0002` n `20`; unknown avg `0.5988` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
