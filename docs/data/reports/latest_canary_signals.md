# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T19:52:28.308130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.216` n `234`; crypto_major avg `0.0845` n `8`; equity avg `0.0192` n `140`; fx avg `0.0016` n `6`; index avg `0.0028` n `26`; metal avg `0.0058` n `20`; unknown avg `7.0929` n `943`
- 1h: commodity avg `0.0366` n `12`; crypto_alt avg `0.7553` n `234`; crypto_major avg `0.6224` n `8`; equity avg `0.081` n `140`; fx avg `-0.0051` n `6`; index avg `-0.0024` n `26`; metal avg `0.0159` n `20`; unknown avg `6.7654` n `941`
- 4h: commodity avg `0.0103` n `12`; crypto_alt avg `2.1255` n `234`; crypto_major avg `1.4043` n `8`; equity avg `0.1804` n `140`; fx avg `-0.0267` n `6`; index avg `0.0281` n `26`; metal avg `0.0048` n `20`; unknown avg `8.2897` n `871`
- 24h: commodity avg `0.418` n `12`; crypto_alt avg `0.3026` n `234`; crypto_major avg `-0.2733` n `8`; equity avg `-0.0743` n `140`; fx avg `-0.0333` n `6`; index avg `-0.0391` n `26`; metal avg `-0.0288` n `20`; unknown avg `3.7805` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
