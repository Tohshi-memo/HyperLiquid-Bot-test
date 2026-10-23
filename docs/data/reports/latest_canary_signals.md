# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T17:37:32.351972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.077` n `13`; crypto_alt avg `-0.2358` n `237`; crypto_major avg `-0.1953` n `8`; equity avg `-0.1338` n `152`; fx avg `-0.0077` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0104` n `20`; unknown avg `-0.1525` n `1229`
- 1h: commodity avg `0.0119` n `13`; crypto_alt avg `-0.2734` n `237`; crypto_major avg `-0.2234` n `8`; equity avg `-0.2479` n `152`; fx avg `-0.0318` n `6`; index avg `-0.0543` n `26`; metal avg `-0.0865` n `20`; unknown avg `-0.0821` n `1221`
- 4h: commodity avg `0.302` n `13`; crypto_alt avg `0.2079` n `237`; crypto_major avg `0.0351` n `8`; equity avg `0.9209` n `152`; fx avg `0.0117` n `6`; index avg `0.0892` n `26`; metal avg `-0.0932` n `20`; unknown avg `-0.2567` n `1151`
- 24h: commodity avg `0.3515` n `13`; crypto_alt avg `1.0919` n `237`; crypto_major avg `0.9612` n `8`; equity avg `1.1704` n `152`; fx avg `-0.119` n `6`; index avg `-0.0084` n `26`; metal avg `-0.2518` n `20`; unknown avg `-0.6532` n `1036`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
