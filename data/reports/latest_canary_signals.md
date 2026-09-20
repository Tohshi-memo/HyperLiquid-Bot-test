# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T07:22:25.428876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.1238` n `234`; crypto_major avg `-0.03` n `8`; equity avg `-0.0084` n `140`; fx avg `-0.0002` n `6`; index avg `-0.0008` n `26`; metal avg `0.0003` n `20`; unknown avg `0.195` n `943`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.2573` n `234`; crypto_major avg `-0.0161` n `8`; equity avg `0.0004` n `140`; fx avg `0.0003` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0048` n `20`; unknown avg `1.9767` n `941`
- 4h: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.4704` n `234`; crypto_major avg `-0.1883` n `8`; equity avg `-0.0861` n `140`; fx avg `-0.0064` n `6`; index avg `-0.018` n `26`; metal avg `0.0175` n `20`; unknown avg `17.8238` n `895`
- 24h: commodity avg `0.2215` n `12`; crypto_alt avg `-0.3137` n `234`; crypto_major avg `-1.7889` n `8`; equity avg `-0.228` n `140`; fx avg `-0.0725` n `6`; index avg `-0.0753` n `26`; metal avg `0.0004` n `20`; unknown avg `4.741` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
