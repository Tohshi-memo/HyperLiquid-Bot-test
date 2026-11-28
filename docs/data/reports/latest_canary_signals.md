# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T12:37:29.471934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.62` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `-0.2042` n `239`; crypto_major avg `-0.0884` n `8`; equity avg `-0.0135` n `168`; fx avg `0.0036` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0017` n `20`; unknown avg `2.051` n `1267`
- 1h: commodity avg `0.0031` n `13`; crypto_alt avg `-0.031` n `239`; crypto_major avg `0.0953` n `8`; equity avg `-0.0046` n `168`; fx avg `0.0045` n `6`; index avg `0.0038` n `27`; metal avg `0.005` n `20`; unknown avg `8.6639` n `1255`
- 4h: commodity avg `-0.0401` n `13`; crypto_alt avg `-0.3455` n `239`; crypto_major avg `-0.2711` n `8`; equity avg `-0.0634` n `168`; fx avg `0.0098` n `6`; index avg `-0.0086` n `27`; metal avg `0.0218` n `20`; unknown avg `327.9947` n `1223`
- 24h: commodity avg `-0.4452` n `13`; crypto_alt avg `-3.5232` n `239`; crypto_major avg `-3.0339` n `8`; equity avg `0.0168` n `168`; fx avg `-0.0925` n `6`; index avg `0.0284` n `27`; metal avg `-0.0701` n `20`; unknown avg `191.8913` n `1087`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
