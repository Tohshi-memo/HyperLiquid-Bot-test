# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T12:52:28.669668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `12`; crypto_alt avg `0.1125` n `234`; crypto_major avg `0.1124` n `8`; equity avg `0.0154` n `140`; fx avg `0.0031` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.1196` n `942`
- 1h: commodity avg `0.0089` n `12`; crypto_alt avg `0.0458` n `234`; crypto_major avg `0.1212` n `8`; equity avg `0.0256` n `140`; fx avg `-0.011` n `6`; index avg `0.0149` n `26`; metal avg `0.0051` n `20`; unknown avg `0.2964` n `934`
- 4h: commodity avg `0.0052` n `12`; crypto_alt avg `0.9124` n `234`; crypto_major avg `0.3283` n `8`; equity avg `0.0229` n `140`; fx avg `0.0012` n `6`; index avg `0.0032` n `26`; metal avg `0.0268` n `20`; unknown avg `0.7123` n `934`
- 24h: commodity avg `0.098` n `12`; crypto_alt avg `4.1279` n `234`; crypto_major avg `3.9972` n `8`; equity avg `0.7455` n `140`; fx avg `-0.0197` n `6`; index avg `0.06` n `26`; metal avg `-0.0395` n `20`; unknown avg `2.9596` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
