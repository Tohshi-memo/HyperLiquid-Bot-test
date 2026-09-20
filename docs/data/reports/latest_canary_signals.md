# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T12:07:25.815330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `0.1245` n `234`; crypto_major avg `0.0599` n `8`; equity avg `0.0026` n `140`; fx avg `-0.0024` n `6`; index avg `0.003` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.1717` n `935`
- 1h: commodity avg `0.0171` n `12`; crypto_alt avg `0.3207` n `234`; crypto_major avg `0.3409` n `8`; equity avg `0.0359` n `140`; fx avg `-0.0153` n `6`; index avg `0.0195` n `26`; metal avg `-0.0108` n `20`; unknown avg `0.1638` n `935`
- 4h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.1843` n `234`; crypto_major avg `0.1678` n `8`; equity avg `-0.0239` n `140`; fx avg `0.0117` n `6`; index avg `0.0161` n `26`; metal avg `-0.0276` n `20`; unknown avg `0.4199` n `935`
- 24h: commodity avg `0.2848` n `12`; crypto_alt avg `-2.1756` n `234`; crypto_major avg `-2.1203` n `8`; equity avg `-0.2551` n `140`; fx avg `-0.0388` n `6`; index avg `-0.0472` n `26`; metal avg `-0.0266` n `20`; unknown avg `0.1111` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
