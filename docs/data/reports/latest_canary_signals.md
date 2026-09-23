# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T01:07:30.779422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `12`; crypto_alt avg `0.1479` n `234`; crypto_major avg `0.1903` n `8`; equity avg `-0.0805` n `140`; fx avg `0.0311` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0958` n `20`; unknown avg `-0.1236` n `943`
- 1h: commodity avg `0.0606` n `12`; crypto_alt avg `0.05` n `234`; crypto_major avg `0.6113` n `8`; equity avg `-0.0652` n `140`; fx avg `0.0077` n `6`; index avg `-0.0453` n `26`; metal avg `-0.1205` n `20`; unknown avg `-0.0602` n `943`
- 4h: commodity avg `0.1092` n `12`; crypto_alt avg `1.2739` n `234`; crypto_major avg `0.7563` n `8`; equity avg `0.0091` n `140`; fx avg `-0.0233` n `6`; index avg `-0.0441` n `26`; metal avg `-0.0684` n `20`; unknown avg `-0.0137` n `936`
- 24h: commodity avg `0.1033` n `12`; crypto_alt avg `3.1518` n `234`; crypto_major avg `1.6726` n `8`; equity avg `0.4345` n `140`; fx avg `-0.1664` n `6`; index avg `0.0105` n `26`; metal avg `0.0757` n `20`; unknown avg `1.1402` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
