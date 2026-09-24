# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T22:22:30.803415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0384` n `12`; crypto_alt avg `-0.3339` n `234`; crypto_major avg `-0.3003` n `8`; equity avg `-0.0335` n `141`; fx avg `-0.0121` n `6`; index avg `-0.0017` n `26`; metal avg `-0.026` n `20`; unknown avg `2.4041` n `906`
- 1h: commodity avg `-0.1662` n `12`; crypto_alt avg `-0.6609` n `234`; crypto_major avg `-0.6162` n `8`; equity avg `-0.0087` n `141`; fx avg `-0.0132` n `6`; index avg `0.0012` n `26`; metal avg `-0.014` n `20`; unknown avg `4.9075` n `904`
- 4h: commodity avg `-0.2384` n `12`; crypto_alt avg `0.031` n `234`; crypto_major avg `-0.5551` n `8`; equity avg `0.0795` n `141`; fx avg `-0.0377` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0265` n `20`; unknown avg `7.5379` n `829`
- 24h: commodity avg `0.6038` n `12`; crypto_alt avg `3.1567` n `234`; crypto_major avg `0.4373` n `8`; equity avg `-0.4204` n `141`; fx avg `0.0141` n `6`; index avg `-0.1464` n `26`; metal avg `-0.152` n `20`; unknown avg `21.0176` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
