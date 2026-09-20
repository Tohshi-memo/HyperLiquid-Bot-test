# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T08:22:27.883638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.1691` n `234`; crypto_major avg `-0.0868` n `8`; equity avg `-0.0068` n `140`; fx avg `-0.0025` n `6`; index avg `0.0025` n `26`; metal avg `-0.0022` n `20`; unknown avg `0.5075` n `943`
- 1h: commodity avg `0.0361` n `12`; crypto_alt avg `-0.1829` n `234`; crypto_major avg `-0.1236` n `8`; equity avg `0.0089` n `140`; fx avg `0.0024` n `6`; index avg `-0.0015` n `26`; metal avg `0.0062` n `20`; unknown avg `0.3711` n `935`
- 4h: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.3351` n `234`; crypto_major avg `0.021` n `8`; equity avg `-0.0112` n `140`; fx avg `0.001` n `6`; index avg `-0.0152` n `26`; metal avg `0.0214` n `20`; unknown avg `8.6036` n `895`
- 24h: commodity avg `0.2457` n `12`; crypto_alt avg `-0.9888` n `234`; crypto_major avg `-2.1331` n `8`; equity avg `-0.2419` n `140`; fx avg `-0.0557` n `6`; index avg `-0.0459` n `26`; metal avg `0.0121` n `20`; unknown avg `0.5822` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
